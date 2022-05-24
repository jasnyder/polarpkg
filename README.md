This is a pip-installable package containing all the code needed to run the cell polarity model, with all the modifications I've made of it.

Code (the bulk of `polarcore.py`) comes from this repo: [https://github.com/juliusbierk/polar](https://github.com/juliusbierk/polar)

# Installation
To download and install this package, you can do:
1. Navigate to an empty folder
2. Run `gh repo clone jasnyder/polarpkg`
3. Run `python3 -m pip install .`

This should install the package. You should then be able to import it in Python by doing
```python
import polaritymodel
```

In the near-ish future (i.e. once I clean the code up enough) I will add this package to [PyPI](https://pypi.org/), at which point it can be installed by simply running
```
python3 -m pip install polaritymodel
```

# Requirements
The code relies essentially on `torch` for the heavy lifitng of the simulation, and benefits greatly from usage of a GPU. If your system does not support CUDA, be sure to run the code with the `device='cpu'` keyword (passed on creation of a `Polar`,`PolarWNT`, or `PolarPDE` object).

`numpy` is needed, as well as `scipy` mainly for its `KDTree` routine. Plotting is done with `plotly` which interacts with data via `pandas` DataFrames. `pickle` is used for data read/write.

# Usage
The basic usage of the code will look something like this
```python
from polaritymodel import PolarPDE, potentials_wnt

x, p, q = initial_conditions()
beta =
eta =
lam =
yield_every =

# set other params
timesteps = 10
yield_every = 10000

# create simulation object
sim = PolarPDE(x, p, q, beta, eta, lam, yield_every)

potential = potentials_wnt.potential_nematic_reweight
runner = sim.simulation(potential, timesteps, yield_every)

for line in itertools.islice(runner, timesteps):
    with open('path/to/data/file.pkl','wb') as fobj:
        pkl.dump(line, fobj)
```