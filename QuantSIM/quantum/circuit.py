import numpy as np
from .qubit import Qubit
from .gates import QuantumGate, H, X, Y, Z, CNOT

class QuantumCircuit:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.qubits = [Qubit() for _ in range(num_qubits)]
        self.gates = []

    def apply_gate(self, gate, target, control=None):
        if isinstance(gate, QuantumGate):
            if control is None:
                self.gates.append((gate, target))
            else:
                self.gates.append((gate, target, control))
        else:
            raise ValueError("Invalid gate")

    def measure_all(self):
        return [qubit.measure() for qubit in self.qubits]

    def run(self):
        for gate_info in self.gates:
            if len(gate_info) == 2:
                gate, target = gate_info
                gate.apply(self.qubits[target])
            elif len(gate_info) == 3:
                gate, target, control = gate_info
                control_state = self.qubits[control].state
                if np.abs(control_state[1]) > 0:
                    gate.apply(self.qubits[target])

    def get_state_vector(self):
        state = self.qubits[0].state
        for qubit in self.qubits[1:]:
            state = np.kron(state, qubit.state)
        return state