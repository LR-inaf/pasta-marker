import matplotlib as mpl
from matplotlib.path import Path
import yaml
import os

def get_pasta_marker(type: str,
                     rotation: float = 0.0,
                     pasta_dataset: str = os.path.join(os.getcwd(), 
                                                       "pastas.yaml"),
                     ):
    """Function that create the requested pasta marker

    Args:
        type (str): pasta type
        rotation (float, optional): marker rotation Defaults to 0.0.
        pasta_dataset (str, optional): Dataset file to retrieve the data. Defaults to os.path.join(os.getcwd(), "pastas.yaml").

    Returns:
        marker: pasta marker
    """
    with open(pasta_dataset, "r") as pasta_file:
        array = yaml.safe_load(pasta_file)[type]
    
    marker = mpl.markers.MarkerStyle(Path(array))
    marker._transform = marker.get_transform().rotate_deg(rotation)
    
    return marker


