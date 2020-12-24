# cryptotools
A set of tools to help with cryptography challenges

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

#### Todo
- implement copersmith's attack
