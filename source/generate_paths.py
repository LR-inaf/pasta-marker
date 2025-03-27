# Adapted from TC Markers. Credits to: abrammer
# GitHub repo: https://github.com/abrammer/tc_markers/

# This script reads the SVG file containing the pasta markers and generates a Python file containing the paths for each marker.
# The paths are then used in the main script to draw the markers.
# This script should be run whenever the SVG file is updated and is only for developer use.
# It requires the svgpath2mpl library to parse the SVG paths.

import xml.etree.ElementTree as etree
import pathlib
import numpy as np
from svgpath2mpl import parse_path
from matplotlib.path import Path
import shapely
from itertools import combinations
import pickle
import yaml

SVG_PATH = pathlib.Path(__file__).parent / "./markers_dev.svg"
SALSA_PATH = pathlib.Path(__file__).parent / "./salsa.yaml"
# SVG_PATH = pathlib.Path(__file__).parent / "./pasta-svgrepo-com.svg"


def main():
    # Parse the SVG file
    with open(SVG_PATH, "r") as file:
        tree = etree.parse(file)

    # Create a parent map
    parent_map = {c: p for p in tree.iter() for c in p}
    root = tree.getroot()

    # Find all path elements
    path_elems = root.findall(".//{http://www.w3.org/2000/svg}path")

    # Process each path element
    marks = {
        # path_elem.attrib["id"]: process_path(path_elem)
        path_elem.attrib["id"]: generate_filled_marker(process_path(path_elem))
        for path_elem in path_elems
    }

    # Write the output
    # outpath = pathlib.Path(__file__).parent.parent / "pastamarkers/markers.py"
    outpath = pathlib.Path(__file__).parent.parent / "pastamarkers/markers.pkl"
    # with open(outpath, "wt") as outf:
    with open(outpath, "wb") as outf:
        # outf.write(generate_output(marks))
        pickle.dump(marks, outf)

    # generate also salsa from yaml file
    # salsa_yaml_file = pathlib.Path(__file__).parent.parent / "pastamarkers/salsa.yaml"
    with open(SALSA_PATH, "r") as file:
        salsa = yaml.load(file, Loader=yaml.FullLoader)

    outpath = pathlib.Path(__file__).parent.parent / "pastamarkers/salsa.pkl"
    # with open(outpath, "wt") as outf:
    with open(outpath, "wb") as outf:
        # outf.write(generate_output(marks))
        pickle.dump(salsa, outf)


def generate_filled_marker(marker):
    exploded_polygons_marker = [shapely.Polygon(el) for el in marker.to_polygons()]

    new_polygons = []
    new_codes = []
    for poly in exploded_polygons_marker:
        for i, (x, y) in enumerate(np.array(poly.exterior.coords.xy).T):
            if i == 0:
                new_codes.append(1)
            else:
                new_codes.append(2)
            new_polygons.append([float(x), float(y)])
        new_codes.pop()
        new_codes.append(79)

    for pol1, pol2 in combinations(exploded_polygons_marker, 2):
        if pol1.contains(pol2):
            for i, (x, y) in enumerate(np.array(pol2.exterior.coords.xy).T):
                if i == 0:
                    new_codes.append(1)
                else:
                    new_codes.append(2)
                new_polygons.append([float(x), float(y)])
            new_codes.pop()
            new_codes.append(79)
        elif pol2.contains(pol1):
            for i, (x, y) in enumerate(np.array(poly.exterior.coords.xy).T):
                if i == 0:
                    new_codes.append(1)
                else:
                    new_codes.append(2)
                new_polygons.append([float(x), float(y)])
            new_codes.pop()
            new_codes.append(79)

    new_marker = Path(new_polygons, new_codes)
    return new_marker


def process_path(path_elem):
    p = parse_path(path_elem.attrib["d"])
    verts = p.vertices
    offset = verts.max(axis=0) - (verts.max(axis=0) - verts.min(axis=0)) / 2
    for vert in p._vertices:
        vert[0] -= offset[0]
        vert[1] -= offset[1]
        vert[1] *= -1
    p._vertices = np.round(p.vertices, 2)  # clean up the file
    return p.deepcopy()


def generate_output(marks):
    output = """
# Automatically generated Paths for each pasta marker from the SVG file. 
# Do not edit manually. Edit SVG and regenerate this file. 

from matplotlib.path import Path
from numpy import array, uint8

"""
    for key, path in marks.items():
        output += f"{key} = {path}\n\n"  # relying on the matplotlib.path.Path repr
    return output


if __name__ == "__main__":
    main()
