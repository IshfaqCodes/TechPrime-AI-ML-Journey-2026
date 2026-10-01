"""
preprocess.py
Loads and cleans the patient history dataset, splits into train/val/test,
and tokenizes text for a seq2seq summarization model.
"""

import re
import pandas as pd
from sklearn.model_selection import train_test_split


def clean_text(text: str) -> str:
    """Basic cleaning: normalize whitespace, strip odd characters."""
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_dataset(csv_path: str) -> pd.DataFrame:
    """Load the patient history CSV and clean the text columns."""
    df = pd.read_csv(csv_path)
    df["patient_history"] = df["patient_history"].apply(clean_text)
    df["reference_summary"] = df["reference_summary"].apply(clean_text)
    return df


def split_dataset(df: pd.DataFrame, test_size: float = 0.2, val_size: float = 0.1, seed: int = 42):
    """Split into train/val/test sets. Works even on very small datasets."""
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=seed)
    train_df, val_df = train_test_split(train_df, test_size=val_size / (1 - test_size), random_state=seed)
    return train_df.reset_index(drop=True), val_df.reset_index(drop=True), test_df.reset_index(drop=True)


def prepare_for_model(examples, tokenizer, max_input_len=512, max_target_len=128, prefix="summarize: "):
    """
    Tokenize a batch of examples for a T5-style model.
    `examples` is a dict-like object with 'patient_history' and 'reference_summary' keys
    (as produced by HuggingFace `datasets.Dataset.map`).
    """
    inputs = [prefix + doc for doc in examples["patient_history"]]
    model_inputs = tokenizer(inputs, max_length=max_input_len, truncation=True, padding="max_length")

    labels = tokenizer(
        text_target=examples["reference_summary"],
        max_length=max_target_len,
        truncation=True,
        padding="max_length",
    )
    # Replace pad tokens with -100 so the loss ignores padding
    model_inputs["labels"] = [
        [(tok if tok != tokenizer.pad_token_id else -100) for tok in seq]
        for seq in labels["input_ids"]
    ]
    return model_inputs


if __name__ == "__main__":
    df = load_dataset("data/sample_patient_histories.csv")
    train_df, val_df, test_df = split_dataset(df)
    print(f"Train: {len(train_df)}  Val: {len(val_df)}  Test: {len(test_df)}")
    train_df.to_csv("data/train.csv", index=False)
    val_df.to_csv("data/val.csv", index=False)
    test_df.to_csv("data/test.csv", index=False)
