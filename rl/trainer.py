def train(env, agent, episodes: int, max_steps=100, log_all=False):
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
            
        if log_all or (episode + 1) % 10 == 0 or episode == episodes - 1:
            print("\n")
            print("—" * 50)
            print(f"🎯 Épisode {episode + 1} terminé")
            print(f"  - Cellule finale : {cell}")
            print(f"  - Étapes : {env.get_step_count()}")
            print(f"  - Succès cumulés : {successes}/{episode + 1}")
            print(f"  - Epsilon = {agent.epsilon:.2f}")

    print("\n✅ Entraînement terminé")
    print(f"  - Succès totaux : {successes}/{episodes}")

