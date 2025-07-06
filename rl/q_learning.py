from collections import defaultdict
from typing import Tuple
import random

class QLearningAgent:
    def __init__(self, actions: list[str], alpha: float, gamma: float, epsilon: float):
        self.q_table = defaultdict(float)
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
    
    def choose_action(self, state: Tuple[int, int]) -> str:
        best_actions = []
        best_value = float('-inf')
        
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        else:
            for action in self.actions:
                value = self.q_table[(state, action)]
                if value > best_value: 
                    best_value = value
                    best_actions = [action]
                elif value == best_value:
                    best_actions.append(action)
                    
            return random.choice(best_actions)
