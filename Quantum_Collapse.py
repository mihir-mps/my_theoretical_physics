import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

sigma_before = 2.0
psi_before = np.exp(-(x**2) / (4 * sigma_before**2))

x0 = 2.0
sigma_after = 0.35
psi_after = np.exp(-((x - x0)**2) / (4 * sigma_after**2))

psi_before /= np.sqrt(np.trapezoid(psi_before**2, x))
psi_after /= np.sqrt(np.trapezoid(psi_after**2, x))

plt.figure(figsize=(10, 6))

plt.plot(x, psi_before, label="Before measurement")
plt.plot(x, psi_after, color="red", label="After measurement")

plt.axvline(
    x0,
    linestyle="--",
    alpha=0.6,
    label="Measured position"
)

plt.xlabel("Position x")
plt.ylabel(r"Wave function $\psi(x)$")
plt.title("Illustration of Wave-Function Collapse")
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
