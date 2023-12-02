import random
import numpy as np
from collections import namedtuple, deque

# Experience tuple
Experience = namedtuple("Experience", field_names=["state", "action", "reward", "next_state", "done"])

# Basic Replay Buffer
class ReplayBuffer:
    def __init__(self, capacity):
        self.memory = deque(maxlen=capacity)

    def add(self, state, action, reward, next_state, done):
        experience = Experience(state, action, reward, next_state, done)
        self.memory.append(experience)

    def sample(self, batch_size):
        return random.sample(self.memory, k=batch_size)

    def __len__(self):
        return len(self.memory)

# Prioritized Experience Replay
class PrioritizedReplayBuffer(ReplayBuffer):
    def __init__(self, capacity, alpha=0.6):
        super().__init__(capacity)
        self.priorities = deque(maxlen=capacity)
        self.alpha = alpha

    def add(self, state, action, reward, next_state, done, priority=1.0):
        super().add(state, action, reward, next_state, done)
        self.priorities.append(priority ** self.alpha)

    def sample(self, batch_size, beta=0.4):
        total_priority = sum(self.priorities)
        probabilities = [priority / total_priority for priority in self.priorities]
        
        sampled_indices = np.random.choice(len(self.memory), batch_size, p=probabilities)
        samples = [self.memory[i] for i in sampled_indices]

        # Compute importance-sampling weights
        weights = [(len(self.memory) * probabilities[i]) ** (-beta) for i in sampled_indices]
        max_weight = max(weights)
        normalized_weights = [weight / max_weight for weight in weights]

        return samples, sampled_indices, normalized_weights

    def update_priorities(self, indices, new_priorities):
        for index, priority in zip(indices, new_priorities):
            self.priorities[index] = priority ** self.alpha