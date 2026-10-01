"""
summarize.py
Command-line inference script: loads the fine-tuned model and generates
a summary for a given patient history text.

Run:
    python src/summarize.py --text "Patient is a 60-year-old..."
    python src/summarize.py --file data/test.csv --row 0
"""

import argparse
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_DIR = "outputs/patient-summarizer"  # fine-tuned model, or swap for "t5-small" to test the base model


def load_model(model_dir: str = MODEL_DIR):
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
    return tokenizer, model


def summarize(text: str, tokenizer, model, max_input_len=512, max_output_len=128) -> str:
    input_text = "summarize: " + text
    inputs = tokenizer(input_text, return_tensors="pt", max_length=max_input_len, truncation=True)
    summary_ids = model.generate(
        **inputs,
        max_length=max_output_len,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True,
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str, help="Raw patient history text to summarize")
    parser.add_argument("--file", type=str, help="CSV file containing a 'patient_history' column")
    parser.add_argument("--row", type=int, default=0, help="Row index to use if --file is given")
    parser.add_argument("--model_dir", type=str, default=MODEL_DIR)
    args = parser.parse_args()

    tokenizer, model = load_model(args.model_dir)

    if args.text:
        text = args.text
    elif args.file:
        df = pd.read_csv(args.file)
        text = df.iloc[args.row]["patient_history"]
    else:
        raise ValueError("Provide either --text or --file")

    summary = summarize(text, tokenizer, model)
    print("\nOriginal:\n", text)
    print("\nGenerated Summary:\n", summary)


if __name__ == "__main__":
    main()
