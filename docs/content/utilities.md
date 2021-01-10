# Utilities

## Default imports

When solving crpytography tasks, there are common libraries which needs to be imported, cryptotools imports these by default as apart of utilities. The below list are the currently imported packages.
```
Crypto.Util.number
binascii.hexlify
binascii.unhexlify
```

## Least Common Multiple (LCM)

Solves for the least common multiple of two numbers.

Arguments: a:integer, b:integer  
Returns: integer

Example usage
```python
>>> LCM(123, 12)
492
```

## Xor

Takes input bytestrings and xors all arguments with each other. Input must be same length or there will be an error.

Arguments: *bytestring
Returns: bytes of xored data

Example usage
```python
>>> xor(b'\x10\x11\x12', 'abc'.encode())
b'qsq'
```

## Repeated Xor

Repeatedly xors key against input bytestring.

Arguments: inp_str:bytestring, key:bytestring  
Returns: bytes of xored data

Example usage
```python
>>> repXor('abcdefg'.encode(), 'key'.encode())
b'\n\x07\x1a\x0f\x00\x1f\x0c'
```

## Extended GCD

Function which solves the extended GCD problem, `a*u + b*v = gcd(a, b)`, for u,v when given a,b.

Arguments: a:integer, b:integer  
Returns: integer, integer, integer (gcd, u, v)

Example usage
```python
>>> eGCD(15, 26)
(1, 7, -4)
```

## Legendre Symbol

Calculates the result of the legendre symbol, `(a/p)=a^((p-1)/2) mod p`, which can be used to determine whether a number is a quadratic residue.

Arguments: a:integer, p:integer  
Returns: integer [1: a is quadratic residue, -1: a is quadratic non-residue, 0: a % p == 0]

Example usage
```python
>>> legendre(28, 3)
1
```

## Chinese Remainder Theorem

Solves system of congruences using the chinese remainder theorem. Algorithm explanation can be found [here](https://brilliant.org/wiki/chinese-remainder-theorem/).

Arguments: a:[integer], b:[integer]; follows x=a mod n where n_i must be coprime  
Returns: integer which is solution to system of congruences

Example usage
```python
>>> crt([1, 4, 6], [3, 5, 7])
34
```
