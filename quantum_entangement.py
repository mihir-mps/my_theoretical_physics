import bluequbit
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

bq = bluequbit.init("V0ADIqu8zcW0hjebFL1oPJZMr9s2OuMY")


qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

print("Text Circuit Diagram:")
print(qc.draw(output='text'))

qc.draw(output='mpl')
plt.show()



result = bq.run(qc, device='CPU', shots=100)
print("\nEntanglement Results:", result.get_counts()) 
