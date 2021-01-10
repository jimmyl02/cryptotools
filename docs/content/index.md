# Home

Welcome to [cryptotools](https://github.com/jimmyl02/cryptotools)! Cryptotools is a repository / package which aims to simplify cryptography attacks by providing implementations for common utilities and attacks. This website documents how to use the crytotools library.

## Installation

Installation is as simple as cloning the repository somewhere.

```
cd /home/jimmy/ctf/tools
git clone https://github.com/jimmyl02/cryptotools.git
```

## Usage

The library must then be imported at the start of the Python or Sage file.

```python
import sys
sys.path.insert(1, '/home/jimmy/ctf/tools')

from cryptotools import * # This must come after pwntools import
```

## Notes about Sage

Some functions require sage and will silently not import if sage is not detected. These functions will have `(Requires Sage)` in the title. Additionally, the functions writen in sage will be prefixed with sage_*. They must be preparsed with `sage --preparse {filename}` then moved from `{filename}.sage.py` to `{filename}.py`. Hopefully there will be a script soon to do this automatically
