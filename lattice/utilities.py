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

