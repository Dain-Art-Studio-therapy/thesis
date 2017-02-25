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
### Questions

1.  Gen set in a block with same variable assigned twice - should it link to the second assignment, and have first assignment in kill set?
2. Should I make if/elif/else have 1 exit block?
3. *** Should parameters be "defined" not "referenced"?


### Test Cases to Add

1. `test_slice.py`: Broken/uncompilable code
2. `block.py`: Equality `BlockList` and `Block` and `FunctionBlock`.
3. `instruction.py`: Equality `Instruction`.


### Features to Add in Type Checker

1. Variable names (no single letters)
2. Loop with else
3. Redefining scope of variable
      `x = [x for x in [1, 2, 3]]`
      `print x`
4. Check for unintialized variables.
5. if/else both have return instead of if (return) [code]
6. Poorly tabbed code (or incorrectly tabbed code)


### Future Considerations

1. Refactor `generatecfg.py` to not use `current_block`.


### Thoughts When Looking Over Code

1. Missing `return` in a particular path
2. Reassigning saved variables in python (ex. in, dir) - #10
3. Similar lines of code - #11, #15, #2
4. Repeating functions imported by another file - #12
5. Wonky tabbing - #12
6. Repeated code across functions - #12
   (Detect similar CFG structure b/w functions - # degree of similarity)
7. Amount of comments
8. Large if <return> else <block code> - #13
9. Amount of spacing - #14
10. Average length of functions - #18
11. Editing a variable defined in a loop header
