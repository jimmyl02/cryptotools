# cryptotools
A set of tools to help with cryptography challenges

## currently implemented attacks and utilities

### attacks

#### RSA
- wiener's attack (wiener_attack) - may work when the e is very small or very large
- recover prime factors (recover_prime_factors) - recovers p and q when given n, e, and d

### utilities

- imports Crypto.Util.number
- least common multiple (LCM)
- repeated XOR (repXor)
- xor (xor)
