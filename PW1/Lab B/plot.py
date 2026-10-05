import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

LAMBDA = 0.3
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

ax1.scatter(t, observed, color="blue", label="Observed", s=15)
ax1.set_title("Observed Data")
ax1.set_xlabel("Time")
ax1.set_ylabel("Count")
ax1.grid(True)

ax2.plot(t, analytical, color="red", label="Analytical")
ax2.set_title("Analytical Decay")
ax2.set_xlabel("Time")
ax2.grid(True)

plt.tight_layout()

plt.savefig("figure.png")
print("График успешно сохранен в figure.png!")