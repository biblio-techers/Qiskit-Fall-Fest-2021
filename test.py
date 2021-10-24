import numpy as np
from qiskit import QuantumCircuit, transpile, QuantumRegister 
from qiskit.circuit.library.basis_change import QFT
from qiskit.visualization import plot_histogram
#from qiskit.providers.aer import QasmSimulator
#print("Use of full:")
#circuit = QFT(5, 7, full=False)
#circuit.append(QFT(2, full=False, name='gate'), [0,1])
#circuit = circuit.decompose(gates_to_decompose='QFT')
q = QuantumRegister(1)
circ = QuantumCircuit(q)

circ.h(q[0])
circ.s(q[0])
circ.x(q[0])
print(circ.data)
quit()

print(circuit.draw())
print("-----")
circuit = circuit.remove_gates()
#circuit.remove_gates(gates_to_remove=([2,3],['x','h']))
#circuit.remove_gates(qubits=[2,3], gates=['4','7'])
print(circuit.data)
print(circuit.draw())
#circuit.remove_gates(qubits=[1,2], include_control=False)
print(circuit.draw())
#print(circuit.draw())
#print(content[::-1])
#circuit.remove_gates(2)

#circuit = QFT(5, 4).decompose()
#print(circuit.draw())
#print("Use of decompose")
#circuit = QFT(5,4)
#print(circuit.draw())
#circuit.full=True
#circuit.append(QFT(3, full=True), [0,2,3])
#circuit.full=True
#print(circuit.draw())
#print(circuit.data)
