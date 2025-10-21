'''
This is for a kaggle competition to classify handwritten digits using a neural network. https://www.kaggle.com/c/digit-recognizer
This module implements a neural network for number classification using TensorFlow and Keras.
'''

'''
Ranked Top 500 out of 195,366 entrants in Kaggle Competition - Rohan Desai
https://www.kaggle.com/competitions/digit-recognizer/leaderboard
'''

import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def get_data(path):
    df = pd.read_csv(path)
    return df

def build_cnn_model(input_shape):
    model = keras.Sequential([
        keras.layers.Reshape((28, 28, 1), input_shape=input_shape),
        keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
        keras.layers.MaxPooling2D(pool_size=(2, 2)),
        keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
        keras.layers.MaxPooling2D(pool_size=(2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(256, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def train_model(X_train, y_train, X_val, y_val):
    model = build_cnn_model((28, 28))
    model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
    return model

def predict(model, X):
    predictions = model.predict(X)
    return predictions

def evaluate_model(model, X_test, y_test):
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
    print(f'\nTest accuracy: {test_acc}')

def create_submission_file(predictions, filename="submission.csv"):
    predicted_labels = predictions.argmax(axis=1)
    ids = range(1, len(predicted_labels) + 1)
    submission_df = pd.DataFrame({
        "ImageId": ids,
        "Label": predicted_labels
    })
    submission_df.to_csv(filename, index=False)
    print(f"✅ Submission file saved to: {filename}")


if __name__ == "__main__":
    train_data = get_data("Neural_networks/data/number_classification_train.csv")
    X = train_data.drop(columns=["label"]).values
    y = train_data["label"].values

    # Reshape and scale the data
    X = X.reshape(-1, 28, 28).astype('float32') / 255.0

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    model = train_model(X_train, y_train, X_val, y_val)

    evaluate_model(model, X_test, y_test)
    
    test_data = get_data("Neural_networks/data/number_classification_test.csv")
    X_test = test_data.values.reshape(-1, 28, 28).astype('float32') / 255.0
    predictions = predict(model, X_test)

    create_submission_file(predictions, filename="submission.csv")
