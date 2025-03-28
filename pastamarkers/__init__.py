import os
import pickle
from collections import namedtuple
from matplotlib.colors import LinearSegmentedColormap

import sys

__ROOT__ = os.path.dirname(__file__)
sys.path.append(__ROOT__)

from cupboard import *

# dir_data = __ROOT__ + "/data/"
dir_data = os.path.join(__ROOT__, "data")

# loading _markers
# pasta_file_path = __ROOT__ + r"\pasta.pkl"
pasta_file_path = os.path.join(__ROOT__, "pasta.pkl")
with open(pasta_file_path, "rb") as pkl_file:
    _markers = pickle.load(pkl_file)

_Marker = namedtuple("Marker", [key for key in _markers.keys()])
pasta = _Marker(*_markers.values())

# loading salsa
salsa_file_path = os.path.join(__ROOT__, "salsa.pkl")
with open(salsa_file_path, "rb") as pkl_file:
    _cmaps = pickle.load(pkl_file)["colormaps"]

_Cmaps = namedtuple("Cmaps", [key for key in _cmaps.keys()])

salsa = _Cmaps(
    *[LinearSegmentedColormap.from_list(key, val[::-1]) for key, val in _cmaps.items()]
)
