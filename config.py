config = {
    "learning_rate": 0.001,
    "gamma": 0.99,
    "tau": 0.01,
    "num_episodes": 1000,
    "max_steps": 200,
    "batch_size": 64,
    "replay_buffer_size": 100000,
    "num_zones": 5,            # Number of building zones
    "temperature_range": (18, 24),  # Comfortable temperature range
    # More hyperparameters...
}
