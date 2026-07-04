# 💳 UPI Fraud Detection using Machine Learning

## 📌 Project Overview

This project uses Machine Learning to detect fraudulent UPI transactions based on transaction details. The goal is to classify transactions as **Fraudulent** or **Legitimate** using various ML algorithms and provide predictions through a Streamlit web application.

---

## 🚀 Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Multiple Machine Learning Models
- Model Comparison
- Fraud Prediction
- Streamlit Dashboard
- GitHub Version Control

---

## 📂 Project Structure

```
UPI-Fraud-Detection/
│
├── app/                 # Streamlit application
├── data/
│   ├── raw/             # Original dataset (ignored in Git)
│   └── processed/       # Cleaned dataset (ignored in Git)
│
├── models/              # Saved ML models
├── notebooks/           # Jupyter notebooks
├── src/                 # Python scripts
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Joblib
- Git & GitHub

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Data Preprocessing
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Saving
10. Streamlit Deployment

---

## 🤖 Models Used

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

The best-performing model will be selected based on evaluation metrics.

---

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/grushamittal05/UPI-Fraud-Detection.git
```

Move into the project folder:

```bash
cd UPI-Fraud-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app/Home.py
```

---

## 📁 Dataset

This project uses the **PaySim** synthetic mobile money transaction dataset.

**Note:** The dataset is **not included** in this repository because it exceeds GitHub's file size limit. Download it separately and place it in:

```
data/raw/
```

---

## 📌 Future Improvements

- SHAP Explainability
- Real-time Fraud Detection
- Risk Score Dashboard
- User Authentication
- Cloud Deployment
- API Integration

---

## 👩‍💻 Author

**Grusha Mittal**

GitHub: https://github.com/grushamittal05