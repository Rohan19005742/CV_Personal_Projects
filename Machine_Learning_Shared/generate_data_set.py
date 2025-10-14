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


def save_dataset(
    data: pd.DataFrame,
    filename: str = "synthetic_salary_data.csv"
) -> None:
    data.to_csv(filename, index=False)
    print(f"✅ Dataset saved to: {filename}")


def main() -> None:
    data = generate_linear_regression_data(n_samples=100)
    save_dataset(data)


if __name__ == "__main__":
    main()
