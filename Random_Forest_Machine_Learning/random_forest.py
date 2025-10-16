import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


class TitanicRandomForest:
    def __init__(self, data_path, n_trees=100, test_size=0.3, random_state=42):
        self.data = pd.read_csv(data_path)
        self.n_trees = n_trees
        self.test_size = test_size
        self.random_state = random_state
        self.label_encoders = {}
        self.model = RandomForestClassifier(
            n_estimators=self.n_trees,
            random_state=self.random_state,
            n_jobs=-1
        )

    def preprocess_data(self):
        # Fill missing numeric values with column means
        self.data.fillna(self.data.select_dtypes(include='number').mean(), inplace=True)

        # Separate features (X) and target (y)
        X = self.data.drop('Survived', axis=1)
        y = self.data['Survived']

        # Split the dataset
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state
        )

        # Encode categorical columns (if any)
        for column in X_train.select_dtypes(include=['object']).columns:
            le = LabelEncoder()
            X_train[column] = le.fit_transform(X_train[column])
            X_test[column] = le.transform(X_test[column])
            self.label_encoders[column] = le

        self.X_train, self.X_test = X_train, X_test
        self.y_train, self.y_test = y_train, y_test

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        y_pred = self.model.predict(self.X_test)
        acc = accuracy_score(self.y_test, y_pred)
        print(f"✅ Model Accuracy: {acc * 100:.2f}%")
        print("\n📊 Classification Report:")
        print(classification_report(self.y_test, y_pred))
        print("\n🧮 Confusion Matrix:")
        print(confusion_matrix(self.y_test, y_pred))

    def predict_survival_probability(self, input_data: pd.DataFrame):
        for column, le in self.label_encoders.items():
            if column in input_data:
                input_data[column] = le.transform(input_data[column])
        probabilities = self.model.predict_proba(input_data)[:, 1]
        return probabilities

    def show_feature_importance(self):
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1]
        features = self.X_train.columns

        plt.figure(figsize=(10, 6))
        plt.title("Feature Importances - Titanic Random Forest")
        plt.bar(range(len(importances)), importances[indices], align='center')
        plt.xticks(range(len(importances)), [features[i] for i in indices], rotation=45)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    model = TitanicRandomForest(
        data_path="Machine_Learning_Shared/titanic_synthetic_data.csv",
        n_trees=100
    )
    
    model.preprocess_data()
    model.train_model()
    model.evaluate_model()
    model.show_feature_importance()

    # Example prediction
    new_passenger = pd.DataFrame([{
        "Pclass": 3,
        "Age": 25,
        "SibSp": 1,
        "Parch": 0,
        "Fare": 207.25,
        "DistanceToEvacuationBoats": 4,
        "Speed": 15
    }])

    prob = model.predict_survival_probability(new_passenger)[0]
    print(f"\n🚢 Predicted survival probability: {prob:.2f}")
