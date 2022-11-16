import numpy as np
import matplotlib.pyplot as plt


# Return normal distribution array Y from array X
def gauss(mu, sigma, X):
    Y = 1.0 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((X - mu) ** 2) / (2 * sigma ** 2))
    return Y 


# Setting X : range = -8 ~ 8, evenly spaced has 100
X = np.linspace(start=-8, stop=8, num=100 + 1)


# When mu = 0, sigma = 0.5, 1, 2 ========================= figure = 1
plt.figure(1)
plt.plot(X, gauss(0, 0.5, X), color="red", label="sigma=0.5")
plt.plot(X, gauss(0, 1, X), color="blue", label="sigma=1")
plt.plot(X, gauss(0, 2, X), color="green", label="sigma=2")

# Print Legend
plt.legend(loc="best")
# Grid setting : visible
plt.grid(True)
# Setting Title
plt.title("normal_distribution_graph_1")
# Save png file
plt.savefig("HW10/normal_distribution_graph_1.png")
# ===================================================================

# When mu = -2.0, 0.0, +2.0, sigma = 1 =================== figure = 2
plt.figure(2)
plt.plot(X, gauss(-2.0, 1, X), color="red", label="mu=-2.0")
plt.plot(X, gauss(0.0, 1, X), color="blue", label="mu=0.0")
plt.plot(X, gauss(2.0, 1, X), color="green", label="mu=2")

# Print Legend
plt.legend(loc="best")
# Grid setting : visible
plt.grid(True)
# Setting Title
plt.title("normal_distribution_graph_2")
# Save png file
plt.savefig("HW10/normal_distribution_graph_2")
# ===================================================================

# Print on screen
plt.show()
