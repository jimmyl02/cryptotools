from Crypto.Util.number import *
from binascii import hexlify, unhexlify

"""
name: repXor
description: repeatedly xors the key against the string
arguments: string:bytearray, key:bytearray
returns: bytearray with the xored data
"""

def repXor(inStr, key):
    pos = 0
    output = bytearray(inStr)

    keyByteArr = bytearray(key)
    for i in range(len(inStr)):
        output[i] ^= keyByteArr[pos]

        pos = (pos + 1) % len(keyByteArr)

    return bytes(output)

"""
name: xor
description: xors all strings given as arguments
arguments: *string:bytearray
returns: bytearray with the xored data
"""

def xor(*inStrs):
    if len(inStrs) == 0:
        return ""

    output = bytearray(inStrs[0])

    for i in range(1, len(inStrs)):
        if len(inStrs[i]) != len(output):
            raise ValueError("String with length " + len(inStrs[i]) +  " is different from the length of the first string " +len(inStrs[0]))

        inStrByteArr = bytearray(inStrs[i])
        for j in range(0, len(inStrs[i])):
            output[j] = output[j] ^ inStrByteArr[j]

    return bytes(output)

"""
name: LCM
description: returns the least common multiple
arguments: a:integer, b:integer
returns: integer
"""

def LCM(a, b):
    return abs(a*b) // GCD(a, b)

"""
name: eGCD
description: extended gcd; solves a*u + b*v = gcd(a, b)
arguments: a:integer, b:integer
returns: integer, integer, integer (gcd, u, v)
"""

def eGCD(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u*q, y - v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


"""
name: legendre
description: legendre symbol calculation (a/p)=a^((p-1)/2) mod p
arguemnts: a:integer, p:integer
returns: integer [1: a is quadratic residue, -1: a is quadratic non-residue, 0: a % p == 0]
"""

def legendre(a, p):
    return pow(a,(p-1)//2,p)

"""
name: crt
description: chinese remainder theorem
arguments: a:[integer], n:[integer]; follows x=a mod n where n_i must be coprime
returns: integer which is solution to system of congruences
"""

def crt(a, n):
    N = n[0]
    for i in range(1, len(n)):
        N *= n[i]
    y = []
    for i in range(len(n)):
        y.append(N // n[i])
    z = []
    for i in range(len(n)):
        # calculate y_i^-1 using eGCD as y_i*y_i^-1+n*m=1 because y_i*y_i^-1 minus any multiple of n should be 1
        res = eGCD(y[i], n[i])
        if(res[0] != 1):
            print('[!] Warning: There is some n_i that is not coprime')
        z.append(res[1])
    ans = 0
    for i in range(len(n)):
        ans += a[i]*y[i]*z[i]
    return ans % N
