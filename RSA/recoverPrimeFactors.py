from ..utilities import *
import random

# This implementation was taken from https://gist.github.com/ddddavidee/b34c2b67757a54ce75cb
# It was originally found from this stack overflow post which explains the algorithm https://crypto.stackexchange.com/questions/16122/rsa-finding-p-q

"""
name: recover_prime_factors
description: attempts to find p and q given n, e, and d
arguments: n, e, d
returns: p, q
note: if primes are not found, function will return -1, -1
"""

def recover_prime_factors(n, e, d):
    k = d * e - 1

    if k % 2 == 1: # d and e do not meet the primary assumption
        return -1, -1
    else:
        t = 0
        r = k
        while(r % 2 == 0):
            r = int(r // 2)
            t += 1
        for i in range(1, 101):
            g = random.randint(0, n) # finds a random g between [0, n-1]
            y = pow(g, r, n)
            if y == 1 or y == n-1:
                continue
            else:
                for j in range(1, t): # j between [1, t-1]
                    x = pow(y, 2, n)
                    if x == 1:
                        p = GCD(y-1, n)
                        q = int(n // p)
                        if p > q:
                            return q, p
                        return p, q
                    elif x == n - 1:
                        continue
                    y = x
                    x = pow(y, 2, n)
                    if x == 1:
                        p = GCD(y-1,n)
                        q = int(n // p)
                        if p > q:
                            return q, p
                        return p, q

