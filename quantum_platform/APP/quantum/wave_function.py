import numpy as np

class WaveFunction:
    def __init__(self, initial_state: np.ndarray):
        self.state = initial_state
        self.time = 0
        
    def evolve(self, hamiltonian: np.ndarray, dt: float):
        """Evolve the wave function according to the Schrödinger equation."""
        # Using the exponential map for time evolution
        evolution_operator = scipy.linalg.expm(-1j * hamiltonian * dt)
        self.state = np.dot(evolution_operator, self.state)
        self.time += dt
        
    def get_probability_density(self) -> np.ndarray:
        """Calculate the probability density of the wave function."""
        return np.abs(self.state) ** 2
        
    def get_expectation_value(self, operator: np.ndarray) -> complex:
        """Calculate the expectation value of an operator."""
        return np.dot(np.conjugate(self.state), np.dot(operator, self.state))