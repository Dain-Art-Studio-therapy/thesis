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

1. Questions: Live Variable Analysis
      - Should suggestions be based on live variable analysis?
          - If so, can I only print suggestions with less than 6 variables?
      - Can live variable analysis ignore anything not defined in the func?
          - Removes function names, etc.
2. Should function names be defined variables?
      - If yes then add recursive tests.
3. How should I handle:
      - Functions inside functions
      - Variables that are referenced but never defined
4. If a variable is out of scope, should it perform "correctly"?
      - Ex. _get_instructions_in_slice --> var init inside loop, print outside


### Features to Add in Type Checker (Linter)

1. Variable names
      - Single letters var names
      - Not meaningful names (ex. XXX)
2. Loop with else
3. Redefining scope of variable
      `x = [x for x in [1, 2, 3]]`
      `print x`
4. Check for unintialized variables.
5. if/else both have return instead of if (return) [code]
6. Poorly tabbed code (or incorrectly tabbed code)
7. Functions inside functions


### Future Considerations

1. Refactor `generatecfg.py` to not use `current_block`.
2. Handle functions within a class.
3. Handle functions within functions (hw4 #31).

