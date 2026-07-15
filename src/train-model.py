from catboost import CatBoostClassifier
import joblib

def train_model(X_train, y_train):

    model = CatBoostClassifier(
        random_state=42,
        verbose=False
    )

    model.fit(X_train, y_train)

    return model


def save_model(model, path):

    joblib.dump(model, path)