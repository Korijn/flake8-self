[![PyPI](https://badge.fury.io/py/flake8-self.svg)](https://badge.fury.io/py/flake8-self) [![Anaconda](https://anaconda.org/conda-forge/flake8-self/badges/version.svg)](https://anaconda.org/conda-forge/flake8-self/) [![Travis](https://travis-ci.org/Korijn/flake8-self.svg?branch=master)](https://travis-ci.org/Korijn/flake8-self/)

# flake8-self

Private member access linting plugin for flake8.

## Example

```
> pipenv run flake8 example.py
example.py:10:1: SF01 Private member access
example.py:11:1: SF01 Private member access
```

example.py:
```python
class Foo(object):
    def __init__(self):
        self.public_thing = "bar"
        self._private_thing = "quux"
        self.__really_private_thing = "quuz"


foo = Foo()
print(foo.public_thing)
print(foo._private_thing)  # SF01 Private member access
print(foo.__really_private_thing)  # SF01 Private member access
print(foo.__dict__)
```
