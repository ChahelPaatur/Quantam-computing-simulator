import numpy as np

class WaveFunction:
    def __init__(self, amplitude, phase):
        self.amplitude = amplitude
        self.phase = phase
        
    def calculate_probability(self):
        return np.abs(self.amplitude) ** 2
        
    def evolve_time(self, time, energy):
        # Schrödinger equation time evolution
        self.phase += energy * time / 1.0545718e-34  # ℏ in SI units
        return self