# Patient History Summarization System — Project Details

**Week 8 Capstone — Deep Learning & NLP Weekly Project**

---

## 1. Project ka Maqsad (Problem Statement)

Doctors ko lambe aur unstructured patient history notes parhne mein bohat waqt lagta hai.
Yeh project ek NLP system banata hai jo lambi patient history se **mukhtasar (concise) aur clinically
ahem summary** khud-ba-khud generate karta hai. Iske liye ek fine-tuned deep learning
sequence-to-sequence (encoder-decoder) model use hota hai.

---

## 2. Project Status (Kya Mukammal Hai?)

| Hissa | Status | Tafseel |
|-------|--------|---------|
| Dataset | Mukammal | 10 synthetic examples, columns: `id`, `patient_history`, `reference_summary` |
| Preprocessing (`preprocess.py`) | Mukammal | Cleaning, train/val/test split, tokenization |
| Training (`train.py`) | Mukammal | T5-small fine-tuning + ROUGE evaluation |
| Inference (`summarize.py`) | Mukammal | Command-line summary generation |
| Exploration notebook | Code mukammal | Abhi run nahi hua (outputs khali hain) |
| README | Mukammal | Results table abhi khali hai |
| Results (ROUGE scores) | Baqi | Training run karne ke baad bharna hai |

**Nateeja:** Code aur structure ke lihaz se project **mukammal hai**. Sirf training run karke
results README mein bharna baqi hai.

---

## 3. Dataset

- **File:** `data/sample_patient_histories.csv`
- **Size:** 10 rows, koi missing value nahi
- **Columns:** `id`, `patient_history`, `reference_summary`
- **Average lambai:** History ~70 alfaaz, Summary ~27 alfaaz (compression ratio ~0.38)
- **Mawad:** Cardiac, respiratory, GI, neuro, pediatric jaisi common presentations
- **Privacy:** Sara data synthetic hai, koi asli patient data nahi (HIPAA masla nahi)
- **Bara dataset lagane ke liye:** Sirf `patient_history` aur `reference_summary` columns rakh kar
  file badal dein (jaise MTSamples ya MIMIC-III/IV).

---

## 4. Approach

- **Model:** `t5-small` (HuggingFace Transformers), abstractive summarization ke liye fine-tune
- **Alternative:** `facebook/bart-base` (`src/train.py` mein `MODEL_NAME` badlein)
- **Kyun T5/BART:** Pretrained encoder-decoder transformers, chhote data/compute par bhi jaldi fine-tune ho jate hain
- **Metric:** ROUGE-1, ROUGE-2, ROUGE-L

---

## 5. Pipeline

1. **Preprocessing** (`src/preprocess.py`)
   - `clean_text()` — extra whitespace hatata hai
   - `load_dataset()` — CSV load karke text clean karta hai
   - `split_dataset()` — 70% train / 10% val / 20% test (10 rows par: 7 / 1 / 2)
   - `prepare_for_model()` — `"summarize: "` prefix laga kar tokenize karta hai (input max 512, target max 128)
2. **Training** (`src/train.py`)
   - Model: `t5-small`, 8 epochs, learning rate `3e-4`, batch size 4
   - Har epoch ke baad ROUGE evaluate hota hai, best model (`rougeL`) load hota hai
   - Model `outputs/patient-summarizer` mein save hota hai, phir test set par final evaluation
3. **Inference** (`src/summarize.py`)
   - Fine-tuned model load karke beam search (4 beams) se summary banata hai

---

## 6. Project Structure

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
├── README.md
├── PROJECT_DETAILS.md
└── HOW_TO_RUN.md
```

> Uploaded files flat hain. Chalane se pehle unhein upar wali folder structure mein rakh lein.

---

## 7. Dependencies (`requirements.txt`)

`transformers`, `datasets`, `evaluate`, `rouge-score`, `torch`, `pandas`, `scikit-learn`, `sentencepiece`

**Sifarish:** In teen packages ko bhi add karein (neeche section 8 dekhein): `accelerate`, `matplotlib`, `jupyter`.

---

## 8. Mojooda Masail aur Sifarishat (Known Issues)

1. **`accelerate` missing hai:** Naye `transformers` mein `Trainer` ke liye zaroori hai. Bagair iske `ImportError` aa sakta hai.
   Fix: `requirements.txt` mein `accelerate>=0.26.0` add karein.
2. **Notebook ke liye `matplotlib` aur `jupyter` missing hain** requirements mein.
3. **Labels ki padding:** `prepare_for_model()` mein labels `pad_token_id` se pad hote hain, `-100` se nahi,
   is wajah se loss padding par bhi calculate hota hai. Behtar hai ke pad tokens ko `-100` se replace karein.
4. **`tokenizer=tokenizer` in `Seq2SeqTrainer`:** Naye transformers versions (4.46+) mein deprecated hai, aur v5 mein hat gaya hai.
   Naye version par `processing_class=tokenizer` use karein.
5. **`eval_strategy` argument** `transformers>=4.41` mein aaya hai, isliye requirements mein `>=4.41.0` behtar hai.
6. **`data/test.csv` khud nahi banta:** `train.py` yeh file nahi banata. `summarize.py --file data/test.csv` chalane se pehle
   `python src/preprocess.py` chalana zaroori hai.
7. **Bohat chhota dataset:** Sirf 7 training examples hain, isliye ROUGE scores kam aur unstable honge.
   Yeh sirf pipeline demonstrate karta hai. Meaningful results ke liye bara dataset (MTSamples/MIMIC) chahiye.

---

## 9. Results

Training ke baad yeh table bharein:

| Metric   | Score |
|----------|-------|
| ROUGE-1  |       |
| ROUGE-2  |       |
| ROUGE-L  |       |

---

## 10. Limitations

- Dataset synthetic aur bohat chhota hai
- Abstractive model clinical facts galat (hallucinate) bhi kar sakta hai, asli medical use ke liye munasib nahi
- Pehli baar chalane par HuggingFace se model weights download hote hain (internet zaroori)

---

## 11. Future Improvements

- Bare clinical dataset par fine-tuning (MTSamples, MIMIC-III discharge summaries)
- Streamlit/Gradio front-end
- Factual-consistency (hallucination) checks
- Bare ya clinical models: BART-large, ClinicalT5, BioBART
