# ContraLegal-AI

Project 7: Intelligent Contract Risk Analysis (Milestone 1)

## Team Pipeline Division

This repository is structured to support 3 distinct development lanes to avoid merge conflicts:

1. **Data Pipeline (`src/data_pipeline/`)**: PDF extraction, cleaning, PII masking, and clause segmentation.
2. **ML Pipeline (`src/ml_pipeline/`)**: Target vectorization (TF-IDF), model training (Logistic Regression/Random Forest), and evaluation.
3. **Application & UI (`src/app/`)**: Streamlit user interface, integration of saved `.pkl` models for risk prediction.

## Directory Structure

- `data/`: Raw and processed datasets (ignored by git).
- `models/`: Saved `scikit-learn` `.pkl` models (ignored by git).
- `notebooks/`: Jupyter notebooks for exploratory data analysis.
- `src/`: Core python packages for the pipelines.
