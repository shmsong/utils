from collections import namedtuple
import numpy as np

matrix_coord = namedtuple("matrix_coord",["x","y"])
indexed_matrix_coord = namedtuple("indexed_matrix_coord",["idx","x","y"])

def make_grid(coords):
    xmax = max([c.x for c in coords])
    ymax = max([c.y for c in coords])
    return np.ones((xmax+1,ymax+1))*-1
