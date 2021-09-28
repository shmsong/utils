# importing modules
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
  

r"""
    Visualize a matrix layout in a warp
"""
def warp_map(data, pixel_plot=None):
    pixel_plot.imshow(data, cmap='coolwarm')
    x,y = data.shape
    pixel_plot.set_xticks(list(range(y)))
    pixel_plot.set_yticks(list(range(x)))
    pixel_plot.invert_yaxis()

    # # label point
    for i,j in product(range(x),range(y)):
        pixel_plot.text(j,i, int(data[i,j]), ha="center",va="center")


r"""
    Reconstruct warp map from laneid function
"""

def gen_laneid_2_warpmap(xy_map,element=np.ones(1), name = "warp_map.png"):
    from permutation.matrix_util import matrix_coord, make_grid
    coords = []
    for lane_id in range(32):
        x=xy_map.x(lane_id)
        y=xy_map.y(lane_id)
        coords.append(matrix_coord(x,y))
        
    grids = []
    for idx,c in enumerate(coords):
        written = False
        for grid in grids:
            if grid[c.x,c.y] == -1:
                grid[c.x,c.y] = idx
                written=True
                break
        if not written:
            grids.append(make_grid(coords))
            grids[-1][c.x,c.y] = idx
    
    grids = [np.kron(g,element) for g in grids]

    fig,axs = plt.subplots(1,len(grids))
    
    if len(grids) > 1:
        for idx,grid in enumerate(grids):    
            warp_map(grid,axs[idx])
    else:
        warp_map(grids[0],axs)
    
    fig.savefig(name)

    