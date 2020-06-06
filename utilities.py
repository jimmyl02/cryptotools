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

    return output

"""
name: xor
description: xors all strings given as arguments
arguments: *string:bytearray
returns bytearray with the xored data
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

    return output

"""
name: LCM
description: returns the least common multiple
arguments: integer, integer
returns: integer
"""

def LCM(a, b):
    return abs(a*b) // GCD(a, b)
