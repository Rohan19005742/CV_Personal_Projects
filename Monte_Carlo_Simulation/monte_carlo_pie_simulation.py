import numpy as np

num_simulations = 1_000_000  # number of random points
inside_circle = 0

for _ in range(num_simulations):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside_circle += 1

pi_estimate = (inside_circle / num_simulations) * 4
print(f"Estimated value of pi after {num_simulations} simulations: {pi_estimate}")
