import os
import xml.etree.ElementTree as etree
import pathlib
import numpy as np
from svgpath2mpl import parse_path

SVG_PATH = "/home/luca/Scrivania/pastamarker/pasta-marker/test/flowers-svgrepo-com.svg"


def main(SVG_PATH):
    # Parse the SVG file
    with open(SVG_PATH, "r") as file:
        tree = etree.parse(file)

    # Create a parent map
    parent_map = {c: p for p in tree.iter() for c in p}
    root = tree.getroot()

    # Find all path elements
    path_elems = root.findall(".//{http://www.w3.org/2000/svg}path")
    return path_elems


if __name__ == "__main__":
    path = main(SVG_PATH)
    p = parse_path(path.attrib["d"])
    print(p)
