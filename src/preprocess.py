import pandas as pd

def load_data(filepath):
    """Load dataset."""
    return pd.read_csv(filepath)


def preprocess_data(df):
    """Clean and preprocess dataset."""

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna(0)

    return df