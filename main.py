from levels import LEVEL_1, LEVEL_2, LEVEL_3
from environment.frozenlake import FrozenLakeEnv
from graphics.renderer import render

env = FrozenLakeEnv(level=LEVEL_1)
env_map = env.get_map()

render(env)

