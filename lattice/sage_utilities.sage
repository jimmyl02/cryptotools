from ..utilities import *

from sage.all import *

"""
name: gauss_lat_red
description: apply gaussian lattice reduction algorithm to find V s.t ||V|| is minimized
                NOTE: Works with 2 dimensions
arguments: v1:vector, v2:vector; must be of length 2
returns: vector, vector; v1, v2 where v1 is shortest vector in L
"""
def gauss_lat_red(v1, v2):
    while True:
        if v2.norm() < v1.norm():
            v1, v2 = v2, v1
        m = round( v1*v2 / v1.norm()^2 )
        if m == 0:
            return (v1, v2)
        v2 = v2 - m*v1
