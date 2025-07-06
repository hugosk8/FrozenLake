from levels import LEVEL_1, LEVEL_2, LEVEL_3
from environment.frozenlake import FrozenLakeEnv
from rl.q_learning import QLearningAgent
from rl.trainer import train

env = FrozenLakeEnv(LEVEL_1)
agent = QLearningAgent(env.actions, 0.1, 0.99, 1)

train(env, agent, 500)