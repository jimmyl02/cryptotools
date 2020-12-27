from ..utilities import *

import numpy as np

"""
name: gram_schmidt
description: use gram schmidt to calculate orthogonal basis of vectors
arguments: v:[[integer]]; list of vectors
returns: [[integer]] orthogonal basis vectors
"""

def gram_schmidt(v):
    v = [np.array(a).astype('float64') for a in v]
    u = []
    u.append(v[0])
    for i in range(1, len(v)):
        u_i = v[i]
        for j in range(0, i):
            u_i -= np.dot(v[i], u[j])/np.dot(u[j], u[j]) * u[j]
        u.append(u_i)
    return [a.tolist() for a in u]

"""
name: gauss_lat_red
description: apply gaussian lattice reduction algorithm to find V s.t ||V|| is minimized
                NOTE: Works witih 2 dimensions
arguments: v:[integer], u:[integer]; must be of length 2
returns: [integer], [integer] v1, v2 where v1 is shortest vector in L
"""
def gauss_lat_red(v, u):
    v, u = np.array(v), np.array(u)
    while True:
        if np.linalg.norm(u) < np.linalg.norm(v):
            v, u = u, v
        m = np.dot(v, u)//np.dot(v, v)
        if m == 0:
            return v.tolist(), u.tolist()
        u = u - m*v

