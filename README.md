# Earthworm: Code Decomposition Tool

### Background

    This project intends to serve as a educational tool for teaching code
    decomposition in Python. This project has been tested for Python 2.7. and
    Python 3.5.


# Running Program
### Run `decomposer.py` on a File

     python -m src.decomposer <PYTHON-2-FILE>
     python3 -m src.decomposer <PYTHON-3-FILE>

### Running Tests

      ./runtests.sh


# Extended TODO List
### Test Cases to Add

1. List comprehension
      `[i for i in range]`
      `print i`

### Features to Add in Type Checker

1. Variable names (no single letters)
2. Loop with else
3. Redefining scope of variable
      `x = [x for x in [1, 2, 3]]`

### Future Considerations

1. Refactor `generatecfg.py` to not use `current_block`.