# Slide outline

1. **Title:** Prompt Lab — Prompt Engineering Playground
2. **Problem:** Prompt quality is often tested informally and inconsistently.
3. **Solution:** Reusable templates, few-shot packs, and a repeatable evaluation workflow.
4. **Architecture:** Streamlit UI → templates/examples → task set → generator/model adapter → scorer → CSV/chart.
5. **Prompt patterns:** Summarization, classification, JSON, QA, code assistant, tone rewrite.
6. **Evaluation design:** 15 fixed tasks, same input for A and B, explicit rubric.
7. **Live demo 1:** Summarization.
8. **Live demo 2:** Few-shot classification.
9. **Live demo 3:** Structured JSON output.
10. **Results & limitations:** Show actual exported results; clearly label offline simulator scores.
11. **Future work:** Connect a real LLM API, add human review, latency and token-cost tracking.
