# pastamarkers
This is the amazing **pasta marker project** that will allow you to use a lot of the famous italian pasta types.

## Installation
The recommended way to install the stable version of pastamarkers is using pip
```
pip install pastamarkers
```

## Usage
The first thing that we need to do is import the necessary modules:
```
import matplotlib.pyplot as plt
from pastamarkers import markers
```
Then, we can directly pass the markers to matplotlib's functions.
```
plt.scatter(x, y, marker=markers.tortellini, s=500, linewidth=0.2)
```
Note: play with `size` and `linewidth` parameters for a perfect pasta marker!

Below you can see the supported data types. Please open an Issue if you would like new pasta types to be included!

## Examples
See also the `\test` folder for working examples.




## Citation

If you find this code useful in your research, please cite the following paper ([ADS](https://ui.adsabs.harvard.edu/abs/2024arXiv240320314P), [arXiv](https://arxiv.org/abs/2403.20314)):

    @ARTICLE{2024arXiv240320314P,
           author = {{PASTA Collaboration}},
            title = "{pastamarkers: astrophysical data visualization with pasta-like markers}",
          journal = {arXiv e-prints},
         keywords = {Astrophysics - Instrumentation and Methods for Astrophysics},
             year = 2024,
            month = mar,
              eid = {arXiv:2403.20314},
            pages = {arXiv:2403.20314},
              doi = {10.48550/arXiv.2403.20314},
    archivePrefix = {arXiv},
           eprint = {2403.20314},
     primaryClass = {astro-ph.IM},
           adsurl = {https://ui.adsabs.harvard.edu/abs/2024arXiv240320314P},
          adsnote = {Provided by the SAO/NASA Astrophysics Data System}
    }


## Currently supported pasta types

<img src="https://raw.githubusercontent.com/LR-inaf/pasta-marker/main/source/markers.svg" alt="CHIMERA" width=500px>

