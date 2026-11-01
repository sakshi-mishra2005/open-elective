# Prompt Lab — Runnable Prompt Engineering Prototype

A small Streamlit app for exploring prompt templates, few-shot examples, and an A/B evaluation harness over 15 tasks.

## Requirements
- Python 3.10+
- Internet only needed to install Python packages. No LLM API key is required for the offline demo.

## Run on Windows
Open Command Prompt or PowerShell in this folder and run:

```bash
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
streamlit run app.py
```

If `py` is not available, use `python` instead.

## Run on macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Streamlit prints a local URL (usually http://localhost:8501). Open it in your browser.

## Features
- 6 prompt templates
- Few-shot example packs
- Playground with selectable templates
- Three core scenarios: summarization, classification, structured JSON
- A/B evaluation using 15 task inputs
- CSV export and chart

## Important evaluation note
This project defaults to an **offline deterministic simulator**. It is designed to run without API credentials and demonstrates the interface, task pipeline, scoring, and exports. Because the simulator does not call an LLM, the A/B scores are not evidence that one natural-language prompt is better than another: both prompts use the same local generator. For a real study, connect an LLM in `evaluate.py`, use the same model/settings for A and B, run all 15 tasks, and record actual outputs. Do not present simulated scores as real LLM performance.

## Project structure
```text
prompt_lab_project/
├── app.py
├── evaluate.py
├── requirements.txt
├── README.md
├── templates/
│   ├── templates.json
│   └── few_shot_examples.json
├── data/
│   └── tasks.json
└── outputs/
```
