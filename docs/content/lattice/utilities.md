# Lattice utilities

## Gram Schmidt

Uses the Gram-Schmidt algorithm to calculate the orthogonal basis of vectors.

Arguments: v:[[integer]]; list of vectors  
Returns: [[integer]] which represents the orthogonal basis vectors

Example usage
```python
>>> lattice.gram_schmidt([[1, 1, 0], [2, 2, 3]])
[[1.0, 1.0, 0.0], [0.0, 0.0, 3.0]]
```

## Gaussian Lattice Reduction (Requires Sage)

Applies the Guassian Lattice Reduction algorithm to find V s.t. ||V|| is minimized. Only works on 2 dimensions. 

Arguments: v1:vector, v2:vector; must be of length 2  
Returns: vector, vector (v1, v2); where v1 is the shortest vector in L

Example usage
```python
>>> v1 = vector(ZZ, [1, 1337])
>>> v2 = vector(ZZ, [2, 1237])
>>> lattice.gauss_lat_red(v1, v2) 
((-29, 26), (14, 37))
```
