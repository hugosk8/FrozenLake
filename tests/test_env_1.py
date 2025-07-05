from levels import LEVEL_1
from environment.frozenlake import FrozenLakeEnv

env = FrozenLakeEnv(level=LEVEL_1, reward_hole=-1)

# Vérifie que la carte est bien chargée et que la position de départ est correcte.
assert env.get_map() == LEVEL_1, "La carte n'est pas correctement chargée"
assert env.get_agent_position() == (0, 0), "La position de départ n'est pas correcte"
print("[✔] Test 1 — Initialisation OK")

# Déplacement simple dans la grille
env.reset()
env.move_agent("right")
assert env.get_agent_position() == (1, 0), "Le déplacement à droite ne fonctionne pas"
env.move_agent("down")
assert env.get_agent_position() == (1, 1), "Le déplacement vers le bas ne fonctionne pas"
print("[✔] Test 2 — Déplacement OK")

# Test 3 — Déplacement contre les bords (ne doit pas sortir de la grille)
env.reset()
env.move_agent("left")  # devrait rester sur place
assert env.get_agent_position() == (0, 0), "L'agent sort de la grille par la gauche"
env.move_agent("up")    # idem
assert env.get_agent_position() == (0, 0), "L'agent sort de la grille par le haut"
print("[✔] Test 3 — Limites de la grille OK")

# Test 4 — Lecture de la case couranteenv.reset()
assert env.get_current_cell() == "S", "La case de départ devrait être 'S'"
env.move_agent("right")  # vers "F"
assert env.get_current_cell() == "F", "La case à droite devrait être 'F'"
print("[✔] Test 4 — Lecture de la case actuelle OK")

# Test 5 — Détection des états terminaux
env.agent_pos = (1, 1)  # Position d'un trou
assert env.is_terminal_state() == True, "L'agent est sur un trou, ça devrait être un état terminal"

env.agent_pos = (3, 3)  # Position du goal
assert env.is_terminal_state() == True, "L'agent est sur le but, ça devrait être un état terminal"

env.agent_pos = (0, 1)  # Case normale
assert env.is_terminal_state() == False, "Ce n'est pas un état terminal"
print("[✔] Test 5 — Détection des états terminaux OK")

# Test 6 — Récompenses associées
env.agent_pos = (1, 1)  # Trou
assert env.get_reward() == -1, "Un trou devrait donner une récompense de -1"

env.agent_pos = (3, 3)  # But
assert env.get_reward() == 1, "Le but devrait donner une récompense de +1"

env.agent_pos = (0, 1)  # Case F
assert env.get_reward() == 0, "Une case normale devrait donner une récompense de 0"
print("[✔] Test 6 — Récompenses OK")

print("\n✅ Tous les tests sont passés avec succès.")
