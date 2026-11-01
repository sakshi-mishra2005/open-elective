import json
import re
from pathlib import Path
import pandas as pd

def load_tasks(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def generate_demo_response(scenario, text, prompt="", examples=None):
    """Deterministic offline demonstration. Replace with a real model adapter for LLM evaluation."""
    s = text.strip()
    if scenario == "Summarization":
        sentences = re.split(r'(?<=[.!?])\s+', s)
        points = [x.strip() for x in sentences if x.strip()]
        return "\n".join(f"- {p}" for p in points[:3]) or "- No input provided."
    if scenario == "Classification":
        lower = s.lower()
        if any(w in lower for w in ["refund", "broken", "late", "complaint", "not working", "bad"]):
            return "complaint"
        if any(w in lower for w in ["thank", "great", "excellent", "happy", "love"]):
            return "positive"
        return "neutral"
    if scenario == "Structured JSON":
        words = s.split()
        return json.dumps({
            "summary": " ".join(words[:12]),
            "word_count": len(words),
            "contains_question": "?" in s
        }, indent=2)
    if scenario == "Question Answering":
        return "Based on the supplied text: " + s[:240]
    if scenario == "Code Assistant":
        return "Suggested approach:\n1. Identify inputs and expected output.\n2. Handle edge cases.\n3. Test with normal and boundary inputs.\n\nInput received: " + s[:180]
    if scenario == "Tone Rewrite":
        return "Hello,\n\n" + s + "\n\nThank you."
    return s

def score_response(task, response, prompt):
    """Small transparent rubric; outputs a score from 0 to 1."""
    r = response.lower()
    expected = task.get("expected", "").lower()
    scenario = task["scenario"]
    checks = []
    if scenario == "Summarization":
        checks.append(bool(response.strip()))
        checks.append(len([x for x in response.splitlines() if x.strip()]) <= 3)
        checks.append(all(term.lower() in r for term in task.get("must_include", [])))
    elif scenario == "Classification":
        checks.append(expected in r)
    elif scenario == "Structured JSON":
        try:
            obj = json.loads(response)
            checks.append(isinstance(obj, dict))
            checks.append(all(k in obj for k in ["summary", "word_count", "contains_question"]))
        except Exception:
            checks.append(False)
    elif scenario == "Question Answering":
        checks.append(bool(response.strip()))
        checks.append(all(term.lower() in r for term in task.get("must_include", [])))
    elif scenario == "Code Assistant":
        checks.append("test" in r)
        checks.append(bool(response.strip()))
    elif scenario == "Tone Rewrite":
        checks.append("thank" in r)
        checks.append(bool(response.strip()))
    else:
        checks.append(bool(response.strip()))
    return round(sum(checks) / len(checks), 4) if checks else 0.0

def run_evaluation(tasks_path, prompt_a, prompt_b):
    tasks = load_tasks(tasks_path)
    rows = []
    for task in tasks:
        # In offline mode the same simulator is used. Prompts are retained for a future LLM adapter.
        out_a = generate_demo_response(task["scenario"], task["input"], prompt_a)
        out_b = generate_demo_response(task["scenario"], task["input"], prompt_b)
        score_a = score_response(task, out_a, prompt_a)
        score_b = score_response(task, out_b, prompt_b)
        rows.append({
            "id": task["id"], "scenario": task["scenario"], "input": task["input"],
            "expected": task["expected"], "output_a": out_a, "score_a": round(score_a*100, 1),
            "output_b": out_b, "score_b": round(score_b*100, 1)
        })
    df = pd.DataFrame(rows)
    summary = {"A": float(df["score_a"].mean()), "B": float(df["score_b"].mean())}
    return df, summary
