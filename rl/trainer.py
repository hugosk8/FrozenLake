def train(env, agent, episodes: int):
    for episode in range(episodes):
        state = env.reset()
        done = False
        
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state, done)
            state = next_state
    
        cell = env.get_current_cell()
        if cell == "G":
            print(f"Objectif atteint à l’épisode {episode+1} en {env.get_step_count()} étapes.")
        elif cell == "H":
            print(f"Tombé dans un trou à l’épisode {episode+1} en {env.get_step_count()} étapes.")

