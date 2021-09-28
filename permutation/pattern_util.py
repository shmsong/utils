from collections import namedtuple

matrix_pattern = namedtuple("matrix_pattern",["x","y"])

gswizzle_0 = matrix_pattern(
    x   = lambda lane_id : (lane_id >> 3) & 0x3,
    y   = lambda lane_id : ((lane_id ^ (lane_id >> 3)) & 0x3) 
)

def div_pattern(lane_id, contiguous, strided):
        ret_contiguous = lane_id % contiguous
        ret_strided = lane_id // contiguous
        return ret_contiguous, ret_strided

def sswizzle_0_y(lane_id):
    contiguous, strided = div_pattern(lane_id,contiguous=8,strided=4)
    return (strided ^ (contiguous >>1 )) | ((contiguous &1)<<2)

def sswizzle_0_x(lane_id):
    contiguous, strided = div_pattern(lane_id,contiguous=8,strided=4)
    return (contiguous>>1)

sswizzle_0 = matrix_pattern(
    x   = sswizzle_0_x,
    y   = sswizzle_0_y
)