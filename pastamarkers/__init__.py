import os
import pickle
from collections import namedtuple
from matplotlib.colors import LinearSegmentedColormap
from .utils import *

__ROOT__ = os.path.dirname(__file__)

dir_data = __ROOT__ + "/data/"

# loading _markers
pasta_file_path = __ROOT__ + r"\pasta.pkl"
with open(pasta_file_path, "rb") as pkl_file:
    _markers = pickle.load(pkl_file)

_Marker = namedtuple("Marker", [key for key in _markers.keys()])
pasta = _Marker(*_markers.values())

# loading salsa
salsa_file_path = __ROOT__ + r"\salsa.pkl"
with open(salsa_file_path, "rb") as pkl_file:
    _cmaps = pickle.load(pkl_file)["colormaps"]

_Cmaps = namedtuple("Cmaps", [key for key in _cmaps.keys()])
salsa = _Cmaps(
    *[LinearSegmentedColormap.from_list(key, val) for key, val in _cmaps.items()]
)
