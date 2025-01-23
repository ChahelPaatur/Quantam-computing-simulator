# app/quantum/simulator.py
import numpy as np

class QuantumRegister:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros(2 ** num_qubits, dtype=complex)
        self.state[0] = 1.0

    def apply_gate(self, gate, target, control=None):
        if control is None:
            full_gate = self._expand_gate(gate, target)
        else:
            full_gate = self._create_controlled_gate(gate, control, target)
        self.state = np.dot(full_gate, self.state)

    def measure(self):
        probabilities = np.abs(self.state) ** 2
        result = np.random.choice(len(self.state), p=probabilities)
        return format(result, f'0{self.num_qubits}b')

class QuantumCircuit:
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    X = np.array([[0, 1], [1, 0]])
    CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.register = QuantumRegister(num_qubits)
        self.gates = []

    def add_gate(self, gate_type, target, control=None):
        self.gates.append({'type': gate_type, 'target': target, 'control': control})

    def run(self, shots=1000):
        results = {}
        for _ in range(shots):
            self.register = QuantumRegister(self.num_qubits)
            for gate in self.gates:
                if gate['type'] == 'H':
                    self.register.apply_gate(self.H, gate['target'])
                elif gate['type'] == 'X':
                    self.register.apply_gate(self.X, gate['target'])
                elif gate['type'] == 'CNOT':
                    self.register.apply_gate(self.CNOT, gate['target'], gate['control'])
            measurement = self.register.measure()
            results[measurement] = results.get(measurement, 0) + 1
        return results