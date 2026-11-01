# Prompt Lab — Evaluation Analysis Template

## Objective
Compare a baseline prompt (A) with a more constrained prompt (B) on a fixed set of 15 tasks.

## Scenarios
- Summarization: T01–T05
- Classification: T06–T10
- Structured JSON: T11–T13
- Question answering: T14
- Code assistant: T15

## Metrics
- Task-specific rubric score
- Average score across tasks
- Difference in percentage points (B − A)
- Per-scenario observations and failure cases

## Interpretation warning
The included offline demo uses deterministic local logic and does not use an LLM. It is suitable for demonstrating the UI and evaluation pipeline, but its scores must not be reported as a real prompt-quality comparison. For a valid A/B study, run both prompts through the same actual model and configuration, save outputs, and score them with a fixed rubric (plus human review where appropriate).

## Results
Run the app's A/B Evaluation section and export `ab_results.csv`. Insert measured results and explain limitations here.
