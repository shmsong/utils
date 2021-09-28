import matplotlib.pyplot as plt
import numpy as np
from permutation.pattern_visualize import warp_map, gen_laneid_2_warpmap
from permutation.matrix_util import matrix_coord,make_grid
from permutation.pattern_util import gswizzle_0, sswizzle_0


if __name__ == "__main__":
    gen_laneid_2_warpmap(gswizzle_0,name="gswizzle0.png")
    gen_laneid_2_warpmap(sswizzle_0,name="sswizzle0.png")
  
