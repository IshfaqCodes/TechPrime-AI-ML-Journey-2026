# Patient History Summarization System

**Week 8 Capstone — Deep Learning & NLP Weekly Project**

## Problem Statement
Clinicians spend significant time reading through lengthy, unstructured patient
history notes. This project builds an NLP system that automatically generates
concise, clinically relevant summaries from longer patient history text, using
a fine-tuned deep learning sequence-to-sequence model.

## Dataset
- `data/sample_patient_histories.csv` — a small hand-crafted set of realistic
  patient history narratives paired with reference summaries, covering common
  presentations (cardiac, respiratory, GI, neuro, pediatric, etc.).
- Designed as a drop-in replacement point: swap this file for a larger public
  clinical corpus (e.g. **MTSamples**, or **MIMIC-III/IV** with credentialed
  access) by keeping the same two columns: `patient_history`, `reference_summary`.

## Approach
- **Model:** `t5-small` (HuggingFace Transformers), fine-tuned as a
  sequence-to-sequence summarizer. `facebook/bart-base` is a drop-in
  alternative (change `MODEL_NAME` in `src/train.py`).
- **Why T5/BART:** Both are pretrained encoder-decoder transformers well
  suited to abstractive summarization, and small enough to fine-tune quickly
  on limited data/compute — appropriate for a one-week project scope.
- **Evaluation metric:** ROUGE-1 / ROUGE-2 / ROUGE-L, the standard metric for
  comparing generated summaries against reference summaries.

## Pipeline
1. **Preprocessing** (`src/preprocess.py`) — cleans text, splits into
   train/val/test, tokenizes for the model.
2. **Training** (`src/train.py`) — fine-tunes the pretrained model on the
   patient history data, evaluating ROUGE after each epoch.
3. **Inference** (`src/summarize.py`) — loads the fine-tuned model and
   generates a summary for new patient history text via the command line.

## Project Structure
```
Patient_History_Summarization/
├── data/
│   └── sample_patient_histories.csv
├── notebook/
│   └── exploration.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── summarize.py
├── requirements.txt
└── README.md
```

## How to Run
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. (Optional) Preprocess & split data separately
python src/preprocess.py

# 3. Fine-tune the model
python src/train.py

# 4. Generate a summary
python src/summarize.py --text "Patient is a 60-year-old male with..."
# or, using a row from the test set:
python src/summarize.py --file data/test.csv --row 0
```

## Results
_Fill in after running training on your machine:_

| Metric   | Score |
|----------|-------|
| ROUGE-1  |       |
| ROUGE-2  |       |
| ROUGE-L  |       |

**Example:**

> **Input:** Patient is a 54-year-old male presenting with a 3-day history of
> chest pain radiating to the left arm...
>
> **Generated Summary:** _(paste actual model output here)_

## Notes & Limitations
- The sample dataset is small (10 examples) and synthetic — sufficient to
  demonstrate the full pipeline, but a larger real-world corpus (MTSamples/
  MIMIC) is recommended for meaningful generalization.
- No real patient-identifiable data is used, avoiding HIPAA/privacy concerns.
- This repo requires internet access to download the pretrained model weights
  from HuggingFace Hub the first time `train.py` or `summarize.py` is run.

## Future Improvements
- Fine-tune on a larger clinical dataset (MTSamples, MIMIC-III discharge summaries)
- Add a simple Streamlit/Gradio front-end for interactive summarization
- Add factual-consistency checks (hallucination detection) for clinical safety
- Experiment with larger backbones (BART-large, ClinicalT5, BioBART)
