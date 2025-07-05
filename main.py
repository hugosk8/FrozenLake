from levels import LEVEL_1
from environment.frozenlake import FrozenLakeEnv

env = FrozenLakeEnv(level=LEVEL_1)
env_map = env.get_map()

print("Carte du niveau :")
for row in env_map:
    print(" ".join(row))

print(f"Position de départ de l’agent : {env.get_agent_position()}")

env.get_current_cell()

