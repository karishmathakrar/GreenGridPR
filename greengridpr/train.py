import torch
import numpy as np
from collections import deque

def train(agent, environment, num_episodes, max_timesteps, epsilon_start=1.0, epsilon_end=0.01, epsilon_decay=0.995):
    """Train the RL agent in the given environment."""
    scores = []                        # List to store scores from each episode
    scores_window = deque(maxlen=100)  # Last 100 scores
    epsilon = epsilon_start            # Initialize epsilon for epsilon-greedy policy

    for i_episode in range(1, num_episodes+1):
        state = environment.reset()
        score = 0
        for t in range(max_timesteps):
            action = agent.select_action(state, epsilon)
            next_state, reward, done, _ = environment.step(action)
            agent.step(state, action, reward, next_state, done)
            state = next_state
            score += reward
            if done:
                break
        scores_window.append(score)
        scores.append(score)
        epsilon = max(epsilon_end, epsilon_decay*epsilon)  # Decrease epsilon

        print(f'\rEpisode {i_episode}\tAverage Score: {np.mean(scores_window):.2f}', end="")
        if i_episode % 100 == 0:
            print(f'\rEpisode {i_episode}\tAverage Score: {np.mean(scores_window):.2f}')

    return scores

def evaluate(agent, environment, num_episodes):
    """Evaluate the RL agent in the given environment."""
    scores = []
    for i_episode in range(1, num_episodes+1):
        state = environment.reset()
        score = 0
        while True:
            action = agent.select_action(state, epsilon=0)  # Choose the best action
            state, reward, done, _ = environment.step(action)
            score += reward
            if done:
                break
        scores.append(score)
        print(f'Episode {i_episode}\tScore: {score}')

    return scores