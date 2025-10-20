import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import brier_score_loss
from sklearn.model_selection import GridSearchCV

def get_test_data():
    path = "Credit_Predictor/data/cs-test.csv"
    df = pd.read_csv(path)
    return df

def get_training_data():
    path = "Credit_Predictor/data/cs-training.csv"
    df = pd.read_csv(path)
    return df

def random_forest_model():
    model = RandomForestClassifier(n_estimators=10000, random_state=42)
    return model

def train_model(X, y):
    model = random_forest_model()
    model.fit(X, y)
    return model

def predict(model, X):
    predictions = model.predict_proba(X)
    return predictions

def createsubmission_file(predictions, filename="submission.csv"):
    ids = range(1, len(predictions) + 1)
    submission_df = pd.DataFrame({
        "Id": ids,
        "Probability": predictions[:, 1]
    })
    submission_df.to_csv(filename, index=False)
    print(f"✅ Submission file saved to: {filename}")


def correct_missing_values(df):
    df = df.fillna(df.median())
    return df

def check_results(y_true, y_pred):
    score = roc_auc_score(y_true, y_pred[:, 1])
    print(f"ROC AUC Score: {score}")

    brier = brier_score_loss(y_true, y_pred[:, 1])
    print("Brier score:", brier)

if __name__ == "__main__":
    data = get_training_data()
    data = correct_missing_values(data)
    X = data.drop(columns=["SeriousDlqin2yrs"])
    y = data["SeriousDlqin2yrs"]
    model = train_model(X, y)

    test_data = get_test_data()
    test_data = correct_missing_values(test_data)
    X_test = test_data.drop(columns=["SeriousDlqin2yrs"])
    predictions = predict(model, X_test)

    createsubmission_file(predictions, filename="submission.csv")
