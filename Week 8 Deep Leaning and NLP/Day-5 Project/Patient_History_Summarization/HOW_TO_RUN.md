# Project Kaise Run Karein (How to Run)

## Zaroorat (Prerequisites)

- Python 3.10 ya usse naya
- Internet (pehli baar model download ke liye)
- RAM: kam az kam 8 GB (GPU zaroori nahi, `t5-small` CPU par bhi chal jata hai)

---

## Step 1: Folder Structure Tayyar Karein

Files ko is tarah rakhein:

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

Saari commands **project ke root folder** (`Patient_History_Summarization/`) se chalayein.

---

## Step 2: Virtual Environment Banayein (Sifarish kardah)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

---

## Step 3: Dependencies Install Karein

```bash
pip install -r requirements.txt
pip install accelerate matplotlib jupyter
```

> `accelerate` naye transformers ke `Trainer` ke liye zaroori hai, aur `matplotlib`/`jupyter` notebook ke liye.

---

## Step 4: Data Split Karein (Zaroori)

```bash
python src/preprocess.py
```

Yeh `data/train.csv`, `data/val.csv` aur `data/test.csv` banata hai.
Expected output: `Train: 7  Val: 1  Test: 2`

---

## Step 5: (Optional) Notebook Mein Data Explore Karein

```bash
jupyter notebook notebook/exploration.ipynb
```

Isme word count distribution, compression ratio aur split preview milta hai.

---

## Step 6: Model Train Karein

```bash
python src/train.py
```

- Pehli baar `t5-small` download hoga
- 8 epochs chalenge, har epoch ke baad ROUGE print hoga
- Model `outputs/patient-summarizer/` mein save hoga
- Aakhir mein test set ke metrics print honge (`eval_rouge1`, `eval_rouge2`, `eval_rougeL`)

Yeh scores README ke Results table mein likh dein.

---

## Step 7: Summary Generate Karein

**Direct text se:**

```bash
python src/summarize.py --text "Patient is a 60-year-old male with a history of hypertension presenting with chest pain and shortness of breath for 2 days."
```

**Test set ki row se:**

```bash
python src/summarize.py --file data/test.csv --row 0
```

**Kisi aur model folder ke saath:**

```bash
python src/summarize.py --text "..." --model_dir outputs/patient-summarizer
```

Base model (bagair training) test karne ke liye `--model_dir t5-small` use karein.

---

## Aam Masail aur Hal (Troubleshooting)

| Masla | Hal |
|-------|-----|
| `ImportError: ... accelerate` | `pip install "accelerate>=0.26.0"` |
| `TypeError: unexpected keyword argument 'tokenizer'` | `train.py` mein `tokenizer=tokenizer` ko `processing_class=tokenizer` se badlein |
| `unexpected keyword argument 'eval_strategy'` | `pip install -U "transformers>=4.41.0"` |
| `FileNotFoundError: data/test.csv` | Pehle `python src/preprocess.py` chalayein |
| `OSError` model download par | Internet check karein ya proxy/firewall dekhein |
| `ModuleNotFoundError: preprocess` | Command project root se chalayein: `python src/train.py` |
| Notebook mein path error | Notebook `notebook/` folder ke andar se kholein (`../src` aur `../data` use hote hain) |
| Out of memory | `train.py` mein `per_device_train_batch_size` kam karein (jaise 2) |
