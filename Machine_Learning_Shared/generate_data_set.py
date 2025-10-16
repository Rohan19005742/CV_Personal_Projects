"""
generate_dataset.py

Creates a synthetic dataset for regression experiments.
Example target: Salary predicted from Years of Experience.
"""

import numpy as np
import pandas as pd
from typing import Tuple


def generate_linear_regression_data(
    n_samples: int = 100,
    noise_std: float = 5_000,
    seed: int = 42
) -> pd.DataFrame:
    np.random.seed(seed)

    years_experience = np.random.uniform(1, 10, n_samples)

    salary = 30_000 + 8_000 * years_experience + np.random.normal(0, noise_std, n_samples)

    return pd.DataFrame({
        "YearsExperience": years_experience,
        "Salary": salary
    })

def generate_titanic_data(
    n_samples: int = 100,
    seed: int = 42
) -> pd.DataFrame:
    np.random.seed(seed)

    pclass = np.random.choice([1, 2, 3], n_samples)
    age = np.random.uniform(0.42, 80, n_samples)
    sibsp = np.random.randint(0, 9, n_samples)
    parch = np.random.randint(0, 7, n_samples)
    fare = np.random.uniform(5, 512, n_samples)
    distance_to_evacuation_boats = np.random.uniform(0.1, 100, n_samples)
    speed = np.random.uniform(0.5, 30, n_samples)
    survived = np.random.choice([0, 1], n_samples)

    return pd.DataFrame({
        "Pclass": pclass,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "DistanceToEvacuationBoats": distance_to_evacuation_boats,
        "Speed": speed,
        "Survived": survived
    })


def save_dataset(
    data: pd.DataFrame,
    filename: str = "synthetic_salary_data.csv"
) -> None:
    data.to_csv(filename, index=False)
    print(f"✅ Dataset saved to: {filename}")


def main() -> None:
    data = generate_titanic_data(n_samples=100)
    save_dataset(data, filename="titanic_synthetic_data.csv")


if __name__ == "__main__":
    main()
