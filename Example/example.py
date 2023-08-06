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
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8), gridspec_kw={'height_ratios': [4, 1]})
popt, pcov = curve_fit(fitFunction, x, y, sigma = yError, p0 = (0.05, 0.008, 125, 50))
ax1.plot(x, fitFunction(x, *popt), color = "red", label = "fit")
popt2, pcov2 = curve_fit(fitFunctionBackground, x, bkg, sigma = bkgError, p0 = (0.008))
ax1.plot(x, fitFunctionBackground(x, *popt2), color = "blue", label = "Bkg fit")
ax1.errorbar(x, y, xerr = binWidth, yerr = yError, marker = "o", ls = "", color =  "black", label = "Data")
ax2.set_xlabel(r"$m_{\gamma\gamma}$ GeV/c$ ^2$")
ax1.set_ylabel(r"Events")
ax1.legend()
ax1.text(75, 0.65, r"$\sqrt{s} = 13.6$ TeV")
ax1.text(75, 0.61, r"$\int \text{d}t L = 20.5$ fb$^{-1}$")
ax1.set_title(r"\textbf{CMS/ATLAS} Simulation")

ax2.set_ylabel(r"Data - Fit", loc = "center")
ax2.axhline(y = 0, color = "black", alpha = 0.3)
ax2.errorbar(x, y - fitFunctionBackground(x, *popt2), xerr = binWidth, yerr = yError, marker = "o", ls = "", color = "black")
path = os.path.join("Plots")
plt.subplots_adjust(hspace=0.0)
if os.path.exists(path):
        plt.savefig(os.path.join("Plots", "CMS.png"), dpi = 500)