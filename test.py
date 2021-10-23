import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library.basis_change import QFT
from qiskit.visualization import plot_histogram
#from qiskit.providers.aer import QasmSimulator

circuit = QFT(40, 4, full=False)
circuit.full=True
print(circuit.draw())
print(circuit.data)