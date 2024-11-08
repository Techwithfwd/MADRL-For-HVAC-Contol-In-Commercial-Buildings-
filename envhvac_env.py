import gym
import numpy as np

class HVACEnv(gym.Env):
    def __init__(self, config):
        self.num_zones = config["num_zones"]
        self.action_space = [gym.spaces.Discrete(3) for _ in range(self.num_zones)] # actions: [0: off, 1: cool, 2: heat]
        self.observation_space = [gym.spaces.Box(low=-1, high=1, shape=(4,)) for _ in range(self.num_zones)]
        self.state = self.reset()

    def reset(self):
        self.state = np.random.uniform(-1, 1, (self.num_zones, 4))
        return self.state

    def step(self, actions):
        reward = self.compute_reward(actions)
        self.state = self.update_state(actions)
        done = self.check_done()
        return self.state, reward, done, {}

    def compute_reward(self, actions):
        # Placeholder: include comfort and energy penalty
        return -np.sum(np.abs(actions))

    def update_state(self, actions):
        # Placeholder: simulate building dynamics
        return self.state

    def check_done(self):
        # Placeholder: define termination criteria
        return False
