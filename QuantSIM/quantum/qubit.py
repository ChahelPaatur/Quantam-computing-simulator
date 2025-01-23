import numpy as np

class Qubit:
    def __init__(self, alpha=1, beta=0):
        self.state = np.array([alpha, beta], dtype=complex)
        self.normalize()

    def normalize(self):
        norm = np.linalg.norm(self.state)
        if norm != 0:
            self.state /= norm

    def measure(self):
        prob_0 = np.abs(self.state[0])**2
        return 0 if np.random.random() < prob_0 else 1