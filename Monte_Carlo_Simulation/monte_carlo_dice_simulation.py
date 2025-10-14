'''
I want to know how many times I can get a sum of {x} when rolling a pair of dice {y} times.
'''
import numpy as np

def monte_carlo_dice_sum_simulation(num_simulations, target_sum) -> int:
    count_target_sum = 0

    for _ in range(num_simulations):
        die1 = np.random.randint(1, 7)
        die2 = np.random.randint(1, 7)
        if die1 + die2 == target_sum:
            count_target_sum += 1

    return (count_target_sum * 100) / num_simulations


def monte_carlo_dice_double_simulation(num_simulations) -> int:
    count_double = 0

    for _ in range(num_simulations):
        die1 = np.random.randint(1, 7)
        die2 = np.random.randint(1, 7)
        if die1 == die2:
            count_double += 1

    return (count_double * 100) / num_simulations


if __name__ == "__main__":
    num_simulations = 1000000
    target_sum = 7
    probability = monte_carlo_dice_sum_simulation(num_simulations, target_sum)
    print(f"expected percentage of getting sum {target_sum} in {num_simulations} rolls: {probability:.2f}%")
    probability_double = monte_carlo_dice_double_simulation(num_simulations)
    print(f"expected percentage of getting doubles in {num_simulations} rolls: {probability_double:.2f}%")

