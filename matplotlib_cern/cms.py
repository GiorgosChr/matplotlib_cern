import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit

# Fonts and General
plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 20
plt.rcParams["figure.figsize"] = (8, 8)

# Points, Errorbars and Lines
plt.rcParams["errorbar.capsize"] = 3.0
plt.rcParams["lines.markersize"] = 5.5
plt.rcParams["lines.linewidth"] = 2.0

# Ticks
plt.rcParams["xtick.bottom"] = True
plt.rcParams["xtick.top"] = True
plt.rcParams["xtick.major.bottom"] = True
plt.rcParams["xtick.major.top"] = True
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["xtick.major.size"] = 8.0
plt.rcParams["xtick.minor.size"] = 5.0

plt.rcParams["ytick.left"] = True
plt.rcParams["ytick.right"] = True
plt.rcParams["ytick.major.left"] = True
plt.rcParams["ytick.major.right"] = True
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["ytick.major.size"] = 8.0
plt.rcParams["ytick.minor.size"] = 5.0

# Axes
# Legend
# Title

# Generate Data
def signal(x):
        A, alpha, mean, sigma = 0.05, 0.008, 125, 50
        return np.exp(-alpha * x) + A * np.exp(-(x-mean)**2/sigma)

def fitFunction(x, A, alpha, mean, sigma):
        return np.exp(-alpha * x) + A * np.exp(-(x-mean)**2/sigma)

xMin, xMax, binWidth = 50, 200, 2
x = np.linspace(xMin, xMax, int((xMax - xMin)/binWidth))
y = signal(x) + 0.01 * np.random.random(len(x))
yError = 0.01 * np.random.random(len(x)) 

popt, pcov = curve_fit(fitFunction, x, y, sigma = yError, p0 = (0.05, 0.008, 125, 50))
plt.plot(x, fitFunction(x, *popt), color = "red", label = "fit")
plt.errorbar(x, y, xerr = binWidth, yerr = yError, marker = "o", ls = "", color = "black", label = "Data")
plt.xlabel(r"GeV/c$ ^2$")
plt.ylabel(r"Events")
plt.legend()
plt.savefig(os.path.join("Plots", "CMS.pdf"))