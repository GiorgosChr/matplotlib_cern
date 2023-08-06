# matplotlib_cern

A matplotlib template  to generate plots similar to CERN's CMS, ATLAS, LHCb and ALICE with LaTeX fonts.

<p>
  <img src="https://github.com/GiorgosChr/matplotlib_cern/blob/main/Plots/CMS.png" alt="CMS Logo" width="600">
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
## Future work
- Specify experiment, luminosity and center of mass energy
- Specify the type of plot, i.e. regular or regular with residuals