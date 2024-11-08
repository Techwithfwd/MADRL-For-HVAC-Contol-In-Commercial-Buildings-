def train_agents(env, agents, config):
    for episode in range(config["num_episodes"]):
        state = env.reset()
        episode_reward = 0

        for step in range(config["max_steps"]):
            actions = [agent.act(state[i]) for i, agent in enumerate(agents)]
            next_state, reward, done, _ = env.step(actions)
            episode_reward += sum(reward)

            for i, agent in enumerate(agents):
                agent.update((state[i], actions[i], reward[i], next_state[i]))

            state = next_state
            if done:
                break

        print(f"Episode {episode} Reward: {episode_reward}")
