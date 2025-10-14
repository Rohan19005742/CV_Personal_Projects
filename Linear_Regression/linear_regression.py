import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List



def compute_gradients(x: np.ndarray, y: np.ndarray, m: float, b: float) -> Tuple[float, float]:
    n = len(x)
    y_pred = m * x + b
    error = y - y_pred
    dm = (-2 / n) * np.sum(x * error)
    db = (-2 / n) * np.sum(error)
    return dm, db


def gradient_descent(
    x: np.ndarray, y: np.ndarray, learning_rate: float = 1e-4, epochs: int = 20_000
) -> Tuple[float, float, List[float]]:
    m, b = 0.0, 0.0
    cost_history = []

    for _ in range(epochs):
        y_pred = m * x + b
        error = y - y_pred
        cost = np.mean(error ** 2)
        cost_history.append(cost)

        dm, db = compute_gradients(x, y, m, b)
        m -= learning_rate * dm
        b -= learning_rate * db

    return m, b, cost_history


def plot_results(x: np.ndarray, y: np.ndarray, m: float, b: float, cost_history: List[float]) -> None:
    sort_idx = np.argsort(x)
    x_sorted = x[sort_idx]
    y_pred_sorted = m * x_sorted + b

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color="blue", label="Data Points")
    plt.plot(x_sorted, y_pred_sorted, color="red", label="Best Fit Line", linewidth=2)
    plt.title("Years of Experience vs. Salary (Gradient Descent)")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 4))
    plt.plot(cost_history, color="purple")
    plt.title("Cost Function (MSE) Over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("Mean Squared Error")
    plt.show()

def predict(x_new: np.ndarray, m: float, b: float) -> np.ndarray:
    return m * x_new + b



def main() -> None:
    data = pd.read_csv("Machine_Learning_Shared/synthetic_salary_data.csv")
    x = data["YearsExperience"].values
    y = data["Salary"].values

    m, b, cost_history = gradient_descent(x, y, learning_rate=1e-4, epochs=20_000)

    print(f"Final slope (m): {m:.2f}")
    print(f"Final intercept (b): {b:.2f}")
    print(f"Final cost: {cost_history[-1]:.2f}")


    x_new = np.array([3, 5, 8, 100])
    y_pred_new = predict(x_new, m, b)

    for exp, sal in zip(x_new, y_pred_new):
        print(f"Predicted salary for {exp:.1f} years experience: ${sal:,.2f}")


    plot_results(x, y, m, b, cost_history)


if __name__ == "__main__":
    main()
