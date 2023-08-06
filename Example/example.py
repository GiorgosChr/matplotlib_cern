import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit

import matplotlib_cern

# Generate Data
def signal(x):
        A, alpha, mean, sigma = 0.05, 0.008, 125, 50
        return np.exp(-alpha * x) + A * np.exp(-(x-mean)**2/sigma)
def backgroundSignal(x):
        alpha = 0.008
        return np.exp(-alpha * x)

def fitFunction(x, A, alpha, mean, sigma):
        return np.exp(-alpha * x) + A * np.exp(-(x-mean)**2/sigma)
def fitFunctionBackground(x, alpha):
        return np.exp(-alpha * x)

xMin, xMax, binWidth = 50, 200, 2
x = np.linspace(xMin, xMax, int((xMax - xMin)/binWidth))
y = signal(x) + 0.01 * np.random.random(len(x))
yError = 0.01 * np.random.random(len(x)) 
bkg = backgroundSignal(x) + 0.01 * np.random.random(len(x))
bkgError = 0.01 * np.random.random(len(x))

# Plot Data
popt, pcov = curve_fit(fitFunction, x, y, sigma = yError, p0 = (0.05, 0.008, 125, 50))
plt.plot(x, fitFunction(x, *popt), color = "red", label = "fit")
popt, pcov = curve_fit(fitFunctionBackground, x, bkg, sigma = bkgError, p0 = (0.008))
plt.plot(x, fitFunctionBackground(x, *popt), color = "blue", label = "Bkg fit")
plt.errorbar(x, y, xerr = binWidth, yerr = yError, marker = "o", ls = "", color =  "black", label = "Data")
plt.xlabel(r"GeV/c$ ^2$")
plt.ylabel(r"Events")
plt.legend()
plt.title(r"\textbf{CMS Simulation}")
plt.savefig(os.path.join("Plots", "CMS.png"), dpi = 500)