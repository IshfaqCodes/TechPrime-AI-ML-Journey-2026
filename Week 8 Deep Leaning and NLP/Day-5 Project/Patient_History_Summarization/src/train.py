"""
train.py
Fine-tunes a pretrained T5 (or BART) model on the patient history
summarization dataset using HuggingFace Transformers.

Run:
    python src/train.py
"""

import numpy as np
import evaluate
import pandas as pd
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
)

from preprocess import load_dataset, split_dataset, prepare_for_model

MODEL_NAME = "t5-small"  # swap for "facebook/bart-base" if preferred
OUTPUT_DIR = "outputs/patient-summarizer"


def main():
    # 1. Load and split data
    df = load_dataset("data/sample_patient_histories.csv")
    train_df, val_df, test_df = split_dataset(df)

    # Save splits so summarize.py --file data/test.csv works after training
    train_df.to_csv("data/train.csv", index=False)
    val_df.to_csv("data/val.csv", index=False)
    test_df.to_csv("data/test.csv", index=False)

    train_ds = Dataset.from_pandas(train_df)
    val_ds = Dataset.from_pandas(val_df)
    test_ds = Dataset.from_pandas(test_df)

    # 2. Load tokenizer & model
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    tokenize_fn = lambda batch: prepare_for_model(batch, tokenizer)
    train_tok = train_ds.map(tokenize_fn, batched=True, remove_columns=train_ds.column_names)
    val_tok = val_ds.map(tokenize_fn, batched=True, remove_columns=val_ds.column_names)

    data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

    # 3. ROUGE metric for evaluation
    rouge = evaluate.load("rouge")

    def compute_metrics(eval_pred):
        predictions, labels = eval_pred
        predictions = np.where(predictions != -100, predictions, tokenizer.pad_token_id)
        decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
        labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
        decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
        result = rouge.compute(predictions=decoded_preds, references=decoded_labels, use_stemmer=True)
        return {k: round(v, 4) for k, v in result.items()}

    # 4. Training arguments
    training_args = Seq2SeqTrainingArguments(
        output_dir=OUTPUT_DIR,
        eval_strategy="epoch",
        save_strategy="epoch",
        learning_rate=3e-4,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        weight_decay=0.01,
        save_total_limit=1,
        num_train_epochs=8,
        predict_with_generate=True,
        logging_steps=5,
        load_best_model_at_end=True,
        metric_for_best_model="rougeL",
    )

    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=train_tok,
        eval_dataset=val_tok,
        processing_class=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )

    # 5. Train
    trainer.train()

    # 6. Save final model
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print(f"Model saved to {OUTPUT_DIR}")

    # 7. Evaluate on held-out test set
    test_tok = test_ds.map(tokenize_fn, batched=True, remove_columns=test_ds.column_names)
    metrics = trainer.evaluate(eval_dataset=test_tok)
    print("Test set metrics:", metrics)


if __name__ == "__main__":
    main()
