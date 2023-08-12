import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit

import matplotlib_cern
matplotlib_cern.set_template()
matplotlib_cern.set_plotstyle(text = "CMS", subtext = "Simulation", lum = "12.3", com = "13.6", plotstyle="regular")

path = os.path.join("Plots")
if os.path.exists(path):
        plt.savefig(os.path.join("Plots", "plotstyle_regular.png"), dpi = 500)

fig, ax1, ax2 = matplotlib_cern.set_plotstyle(text = "CMS", subtext = "Simulation", lum = "12.3", com = "13.6", plotstyle="residuals")
plt.subplots_adjust(hspace=0.0)
if os.path.exists(path):
        plt.savefig(os.path.join("Plots", "plotstyle_residuals.png"), dpi = 500)