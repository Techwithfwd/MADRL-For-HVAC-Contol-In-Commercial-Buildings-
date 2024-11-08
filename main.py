import config
from env.hvac_env import HVACEnv
from agents.maddpg_agent import MADDPGAgent
from training.train import train_agents

if __name__ == "__main__":
    # Initialize environment and agents
    env = HVACEnv(config)
    agents = [MADDPGAgent(config, agent_id=i) for i in range(env.num_zones)]
    
    # Train agents
    train_agents(env, agents, config)
