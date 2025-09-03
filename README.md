# FOIA Accelerate

A research prototype accompanying a policy proposal on **conservative, auditable NLP** for FOIA processing.
This repository contains **working code** for four modules:
1. **Routing Classifier** — suggests target office/component.
2. **PII-Aware Redaction** — flags likely PII for *human* review.
3. **Deduplication** — clusters near-duplicate requests.
4. **Summarizer** — lightweight extractive summary for long texts.

> ⚠️ This is a **demonstration** on synthetic/open text. It is **not** a production system and makes no release decisions.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
pytest -q
jupyter notebook notebooks/foia_accelerate_demo.ipynb
```

## Datasets

- `data/sample_requests.csv` — synthetic examples.
- For real-world exploration, see:
  - DOJ Annual FOIA Reports: https://www.justice.gov/oip/available-annual-foia-reports
  - FOIA.gov raw data: https://www.foia.gov/data.html

## Design Notes

- **No automated disclosure**. All outputs are *suggestions* for FOIA officers.
- **Classical ML first** (TF-IDF + Logistic Regression / cosine similarity) to keep dependencies light.
- **Deterministic defaults**: random seeds and simple configs for reproducibility.

## Optional Upgrades

You can swap pieces with transformer models when appropriate (examples sketched in code comments):
- Routing: Hugging Face `AutoModelForSequenceClassification`.
- Summarization: `distilbart-cnn-12-6` via `transformers` pipeline.
- Embeddings: `sentence-transformers` for deduplication.

See inline comments and `requirements-extras.txt`.

## License

MIT — see `LICENSE`.