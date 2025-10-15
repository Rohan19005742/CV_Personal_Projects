'''
this module implements a Markov Chain model for the classic Snake and Ladder game.
'''

import numpy as np
import random
from enum import Enum


class CellType(Enum):
    NORMAL = 0
    SNAKE = 1
    LADDER = 2


class SnakeAndLadderMarkovChain:
    def __init__(self, board_size = 100):
        self.board_size = board_size
        self.current_position = 0
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78, 99: 90}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.transition_matrix = self._create_transition_matrix()
    
    def _create_transition_matrix(self):
        matrix = np.zeros((self.board_size + 1, self.board_size + 1))
        for i in range(self.board_size):
            for dice_roll in range(1, 7):
                next_pos = i + dice_roll
                if next_pos > self.board_size:
                    next_pos = i  # stay in the same position if overshoot
                if next_pos in self.snakes:
                    next_pos = self.snakes[next_pos]
                elif next_pos in self.ladders:
                    next_pos = self.ladders[next_pos]
                matrix[i][next_pos] += 1/6
        matrix[self.board_size][self.board_size] = 1  # absorbing state
        return matrix
    
    def next_move(self):
        rand_val = random.random()
        cumulative_prob = 0.0
        for next_pos, prob in enumerate(self.transition_matrix[self.current_position]):
            cumulative_prob += prob
            if rand_val < cumulative_prob:
                self.current_position = next_pos
                break
        return self.current_position
    
    def simulate_game(self):
        self.current_position = 0
        moves = 0
        while self.current_position < self.board_size:
            self.next_move()
            moves += 1
        return moves
    
if __name__ == "__main__":
    game = SnakeAndLadderMarkovChain()
    num_simulations = 1000
    average_moves = []
    moves = game.simulate_game()
    for i in range(num_simulations):
        moves = game.simulate_game()
        average_moves.append(moves)
        print(f"Game {i+1}: Finished in {moves} moves")
    print(f"Average moves to finish the game over {num_simulations} simulations: {np.mean(average_moves)}")