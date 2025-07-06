def train(env, agent, episodes: int, max_steps=100):
    successes = 0
    
    for episode in range(episodes):
        state = env.reset()
        done = False
        steps = 0
        
        if episode == 100:
            agent.epsilon = 0.8
        elif episode == 200:
            agent.epsilon = 0.6
        elif episode == 300:
            agent.epsilon = 0.4
        elif episode == 400:
            agent.epsilon = 0.
        
        while not done and steps < max_steps:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state, done)
            state = next_state
            steps += 1
    
        cell = env.get_current_cell()
        if cell == "G":
            successes += 1
            print(f"Objectif atteint à l’épisode {episode+1} en {env.get_step_count()} étapes.")
        elif cell == "H":
            print(f"Tombé dans un trou à l’épisode {episode+1} en {env.get_step_count()} étapes.")
        
        if episode != episodes - 1:
            print(f"\nSuccès depuis le debut: {successes}/{episodes}")
        print(f"Épisode {episode+1} | epsilon = {agent.epsilon:.2f}")

    print(f"\nSuccès totaux: {successes}/{episodes}")

