import sys
from sympy.solvers import solve
from sympy import Symbol

# This is taken from https://github.com/sourcekris/RsaCtfTool/blob/master/wiener_attack.py
# I am changing the format so that it is not an object but rather a collection of methods

# A reimplementation of pablocelayes rsa-wiener-attack for this purpose
# https://github.com/pablocelayes/rsa-wiener-attack/

def rational_to_contfrac(x, y):
    a = x // y
    if a * y == x:
        return [a]
    else:
        pquotients = rational_to_contfrac(y, x - a * y)
        pquotients.insert(0, a)
        return pquotients

def convergents_from_contfrac(frac):
    convs = []
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0:i]))
    return convs

def contfrac_to_rational(frac):
    if len(frac) == 0:
        return (0, 1)
    elif len(frac) == 1:
        return (frac[0], 1)
    else:
        remainder = frac[1:len(frac)]
        (num, denom) = contfrac_to_rational(remainder)
        return (frac[0] * num + denom, num)

def isqrt(n):
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y

def is_perfect_square(n):
    h = n & 0xF
    if h > 9:
        return -1

    if(h != 2 and h != 3 and h !=5 and h !=6 and h !=7 and h != 8):
        t = isqrt(n)
        if t * t == n:
            return t
        else:
            return -1

    return -1

"""
name: wiener_attack
description: performs wiener's attack for large e values
arguments: n, e
returns: d, p, q
"""

def wiener_attack(n, e):
    sys.setrecursionlimit(100000)
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)

    for (k, d) in convergents:
        if k != 0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            discr = s*s - 4*n
            if(discr >= 0):
                t = is_perfect_square(discr)
                if t != -1 and (s+t)%2 == 0:
                    x = Symbol('x')
                    roots = solve(x**2 - s*x + n, x)
                    if len(roots) == 2:
                        p = roots[0]
                        q = roots[1]
                        return d, p, q
                    break
