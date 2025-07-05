from environment.frozenlake import FrozenLakeEnv

env = FrozenLakeEnv()
env_map = env.get_map()

print("Carte du niveau :")
for row in env_map:
    print(" ".join(row))

print(f"Position de départ de l’agent : {env.get_agent_position()}")