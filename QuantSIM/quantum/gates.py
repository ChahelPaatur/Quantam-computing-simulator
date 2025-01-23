import numpy as np

class QuantumGate:
    def __init__(self, matrix):
        self.matrix = np.array(matrix, dtype=complex)

    def apply(self, qubit):
        qubit.state = np.dot(self.matrix, qubit.state)
        qubit.normalize()

H = QuantumGate([[1/np.sqrt(2), 1/np.sqrt(2)],
                 [1/np.sqrt(2), -1/np.sqrt(2)]])

X = QuantumGate([[0, 1],
                 [1, 0]])

Y = QuantumGate([[0, -1j],
                 [1j, 0]])

Z = QuantumGate([[1, 0],
                 [0, -1]])

CNOT = QuantumGate([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1],
                    [0, 0, 1, 0]])