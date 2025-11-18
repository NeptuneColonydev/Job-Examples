import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, PercentFormatter

def f(n):
    return n/n+10

n_values = np.linspace(0, 30, 400)
f_values = f(n_values)

plt.figure(figsize=(8, 6))
plt.plot(n_values, f_values, label=r"$f(n) = \frac{n}{n+10}$", color="b", linewidth=2)
plt.title("Graph of f(n) = n / (n + 10) for n from 0 to 30", fontsize=14)
plt.xlabel('Number of Keys', fontsize=12)
plt.ylabel('Percentage Chance of Free Chest', fontsize=12)

plt.gca().yaxis.set_major_locator(MultipleLocator(0.05))
plt.gca().xaxis.set_major_locator(MultipleLocator(1.0))
plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.xlim(0, 30)
plt.ylim(0, 1)

plt.legend()
plt.grid(True)
plt.show()