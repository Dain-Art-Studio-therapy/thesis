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

1. Test `BlockList` and `Block.get_instructions()`.
2. Test `dataflowanalysis.py`.
3. `test_generatecfg.py`: if without else.
4. List comprehension
      `[i for i in range]`
      `print i`
5. Multiple assignments single line
      `m = n = 1`

### Features to Add in Type Checker

1. Variable names (no single letters)
2. Loop with else
3. Redefining scope of variable
      `x = [x for x in [1, 2, 3]]`
4. Check for unintialized variables.

### Future Considerations

1. Make `BlockInterface` an abstract class using `abc`.
2. Refactor `generatecfg.py` to not use `current_block`.
