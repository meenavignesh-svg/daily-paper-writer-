# Daily Bioinformatics Paper Writer 🧬

A practical research workspace for building a bioinformatics review paper one verified evidence block at a time.

## What it does
- Searches PubMed and OpenAlex for recent literature.
- Deduplicates results using DOI/title matching.
- Builds a literature matrix with methods, datasets, findings and limitations.
- Exports Markdown and BibTeX.
- Creates a daily research brief.
- Optional AI drafting through any OpenAI-compatible API.
- Adds `[NEEDS VERIFICATION]` instead of inventing evidence.
- Includes a GitHub Actions daily run that can commit the research brief automatically.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

No API key is needed for literature search. An LLM key is only required for AI drafting.

## Optional AI setup
Copy `.env.example` to `.env` and set `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_MODEL` for an OpenAI-compatible provider.

## Daily workflow
1. Enter a focused bioinformatics topic and research question.
2. Search and inspect the returned papers.
3. Export the evidence matrix/BibTeX.
4. Generate a constrained draft only from the retrieved evidence.
5. Verify every claim and reference before using it in a manuscript.

## GitHub Actions
The scheduled workflow runs each day and can generate a fresh literature brief from `config/topics.json`. GitHub scheduled workflows use cron and run from the default branch. See GitHub's workflow documentation for scheduling details.

**Scientific rule:** AI is an assistant, not a source. Never submit an AI-generated citation or claim without checking the original paper.
