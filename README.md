# matplotlib_cern
[![PyPI Downloads](https://img.shields.io/pypi/dm/matplotlib-cern.svg?label=PyPI%20downloads)](https://pypi.org/project/matplotlib-cern/)

A matplotlib template  to generate plots similar to CERN's CMS, ATLAS, LHCb and ALICE with LaTeX fonts.

<p>
  <img src="https://github.com/GiorgosChr/matplotlib_cern/blob/main/Plots/CMS.png" alt="CMS plot" width="600">
</p>

## Requirements
For this template you will need the following:

```bash
$ sudo apt install python3 texlive-full
$ pip3 install matplotlib
```

## Installation
`matplotlib_cern` is available through `pip3`. To install simply use

```bash
$ pip3 install matplotlib_cern
```

## Usage
You can find a full example [here](https://github.com/GiorgosChr/matplotlib_cern/blob/main/Example/example.py).
Simply import the following packages at the beginning of your script

```python
import matplotlib.pyplot as plt
import matplotlib_cern
```
Currently there are only two functions, `set_template` and `set_plotstyle`. The former sets global matplotlib parameters and the latter creates a plot according to user defined variables.
To set the plot style you can pass the following arguments:
```python
matplotlib.set_plotstyle(text = "CMS", subtext = "Simulation", lum = "12.3", com = "13.6", plotstyle = "regular")
```
The default values are `None` for all except `plotstyle = "regular"`.
The `"regular"` option produces a square 8x8 plot and `"residuals"` produces a square 6x8 plot with a residual plot attached to the bottom of it.

Here are examples of the `"regular"` and `"residuals"` plots:
<p>
  <img src="https://github.com/GiorgosChr/matplotlib_cern/blob/main/Plots/plotstyle_regular.png" alt="regular" height="300">
  <img src="https://github.com/GiorgosChr/matplotlib_cern/blob/main/Plots/plotstyle_residuals.png" alt="residuals" height="300">
</p>

## Future work
- ~~Specify experiment, luminosity and center of mass energy~~
- ~~Specify the type of plot, i.e. regular or regular with residuals~~
