# cryptotools
A set of tools to help with cryptography challenges

Some functions require sage and will silently not import if sage is not detected. Additionally, the functions writen in sage will be prefixed with sage_*. They must be preparsed with `sage --preparse {filename}` then moved from `{filename}.sage.py` to `{filename}.py`. Hopefully there will be a script soon to do this automatically 

## Usage
```python
import sys
sys.path.insert(1, '/home/jimmy/ctf/tools')

from cryptotools import * # This must come after pwntools import
```

## Currently implemented attacks and utilities

### Attacks

#### RSA
- wiener's attack (wiener_attack) - may work when the e is very small or very large
- recover prime factors (recover_prime_factors) - recovers p and q when given n, e, and d

#### Utilities

- imports Crypto.Util.number
- imports hexlify and unhexlify from binascii
- least common multiple (LCM)
- repeated XOR (repXor)
- xor (xor)
- extended gcd
- legendre symbol
- chinese remainder theorem

#### Lattice

- gram schmidt 
NOTE: Sage is required for the folowing
- gaussian lattice reduction (gauss_lat_red)

#### Todo
- implement copersmith's attack
