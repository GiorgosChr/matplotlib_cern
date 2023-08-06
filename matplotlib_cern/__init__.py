# matplotlibcern/__init__.py

import matplotlib.pyplot as plt

def set_matplotlib_cern():
    # Fonts
    plt.rcParams["text.usetex"] = True
    plt.rcParams["text.latex.preamble"] = r"\usepackage{amsmath} \usepackage{amssymb}"
    plt.rcParams["font.size"] = 20
    plt.rcParams["font.family"] =  "serif"
    plt.rcParams["font.serif"] =  "STIXGeneral"
    plt.rcParams["mathtext.fontset"] =  "stix"

    # Figure
    plt.rcParams["figure.figsize"] = (8, 8)
    plt.rcParams["savefig.bbox"] = "tight"

    # Points, Errorbars, Scatter and Lines
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
    plt.rcParams["xaxis.labellocation"] = "right"
    plt.rcParams["yaxis.labellocation"] = "top"

    # Legend
    plt.rcParams["legend.fontsize"] = 20
    plt.rcParams["legend.frameon"] = False

    # Title
    plt.rcParams["axes.titlelocation"] = "left"

# Call the function to set the defaults when the package is imported
set_matplotlib_cern()
