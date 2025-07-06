from levels import LEVEL_1
from environment.frozenlake import FrozenLakeEnv
from graphics.renderer import render

env = FrozenLakeEnv(level=LEVEL_1)
env_map = env.get_map()

render(env)

