import joblib
import pandas as pd


def load_model(path):

    return joblib.load(path)


def predict(model, input_data):

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)

    probability = model.predict_proba(df)

    return prediction, probability