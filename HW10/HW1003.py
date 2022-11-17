# HW1003.py
"""
Project : Normal distribution graph analysis with numpy module
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 17
Update list:
    - v1.1 : 11 / 17
        Make funtion : gauss()
        Add figure1 : When mu = 0, sigma = 0.5, 1, 2
            Setting figure1 shape : legend, grid, title, savefig
        Add figure2 : When mu = -2.0, 0.0, +2.0, sigma = 1 
            Setting figure2 shape : legend, grid, title, savefig
        plt.show() : for Print on screen
"""
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
