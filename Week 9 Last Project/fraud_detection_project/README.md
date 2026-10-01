# Fraud Detection Project

Real-Time Hybrid Credit Card Fraud Detection & Risk Scoring System

## Folder Structure
- data/       -> dataset files (creditcard.csv, data/processed/ splits)
- notebooks/  -> Jupyter notebooks (EDA, training, SHAP, MLflow, monitoring)
- src/        -> main.py (FastAPI), dashboard.py (Streamlit), landing.py (welcome screen)
- models/     -> saved trained models
- tests/      -> API tests

## How to run (Windows / Mac / Linux)

Python 3.12 recommended.

1. Open a terminal in this folder and create a virtual environment:
       python -m venv .venv
       # Windows:  .venv\Scripts\activate
       # Mac/Linux: source .venv/bin/activate

2. Install dependencies:
       pip install -r requirements-dashboard.txt

3. Start the dashboard (opens at http://localhost:8501 with the welcome screen first):
       streamlit run src/dashboard.py

4. (Optional) Start the API in a second terminal (docs at http://127.0.0.1:8000/docs):
       uvicorn src.main:app --reload

5. (Optional) Run tests:
       pip install pytest httpx
       pytest tests

## Run with Docker
       docker compose up --build
   Dashboard -> http://localhost:8501 , API -> http://localhost:8000/docs

## Notebooks
Install everything with `pip install -r requirements.txt`, then open the notebooks in
VS Code or Jupyter. See INSTRUCTIONS.md for the full phase-by-phase history.
