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
### Current Tasks

Monday: Slicing algorithm

1. Finish reading the paper (until necessary).
2. Rewrite slicing algorithm to copy CFG
3. Test slicing algorithm
4. Run cyclometric complexity on small CFG
5. Create type checker
6. Test type checker

Tuesday: Run experiments

1. Find good and bad samples of code (starting at #20 cast.py)
2. Try finding complexity on each line of code (avg for each sample)
3. Determine experiments to run Tuesday/Wednesday


### Questions

1.  Gen set in a block with same variable assigned twice - should it link to the second assignment, and have first assignment in kill set?


### Features to Add in Type Checker

1. Variable names (no single letters)
2. Loop with else
3. Redefining scope of variable
      `x = [x for x in [1, 2, 3]]`
      `print x`
4. Check for unintialized variables.
5. if/else both have return instead of if (return) [code]


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
