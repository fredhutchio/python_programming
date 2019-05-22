#### [[course and class]] ####

#### Objectives ####

# review previous week's objectives
# Today:
#   use assertions to ensure a program progresses as expected
#   apply test-driven development to creating new functions

#### Defensive programming ####

# are we getting the right answer?
#   Write programs that check their own operation.
#   Write and run tests for widely-used functions.
#   Make sure we know what “correct” actually means.

# assume mistakes will happen and guard against them (defensive programming)

## Assertions

# assertions: statement that something must be true at a certain point in a program
numbers = [1.5, 2.3, 0.7, -0.001, 4.4]
total = 0.0
for n in numbers:
    assert n > 0.0, 'Data should only contain positive values'
    total += n
print('total is:', total)

# types of assertions:
#   precondition is something that must be true at the start of a function in order for it to work correctly.
#   postcondition is something that the function guarantees is true when it finishes.
#   invariant is something that is always true at a particular point inside a piece of code.

# assertions in action: start with code in week4_example1.py
def normalize_rectangle(rect):
    '''Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.
    Input should be of the format (x0, y0, x1, y1).
    (x0, y0) and (x1, y1) define the lower left and upper right corners
    of the rectangle, respectively.'''
    assert len(rect) == 4, 'Rectangles must contain 4 coordinates' # precondition
    x0, y0, x1, y1 = rect
    assert x0 < x1, 'Invalid X coordinates' # precondition
    assert y0 < y1, 'Invalid Y coordinates' # precondition

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dx) / dy # error is here, should be float(dy) / dx
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid' # postcondition
    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid' # postcondition

    return (0, 0, upper_x, upper_y)

# preconditions: add preconditions to function from week4_example1.py
print(normalize_rectangle( (0.0, 1.0, 2.0) )) # missing the fourth coordinate
print(normalize_rectangle( (4.0, 2.0, 1.0, 5.0) )) # X axis inverted

# postconditions: add postconditions to function from week4_example1.py
print(normalize_rectangle( (0.0, 0.0, 1.0, 5.0) )) # normalizing a rectangle that is taller than it is wide seems OK
print(normalize_rectangle( (0.0, 0.0, 5.0, 1.0) )) # assertion triggered by rectangle wider than tall
# this should work! re-check code to see error specified above

# assertions help us:
#   detect errors and debug code
#   understand programs
# "fail early, fail often"
# "turn bugs into assertions or tests"

## Test driven development

# motivation: we need to find where two or more time series overlap
#   data represented as a pair of numbers, start and stop for interval
#   desired output is range of time they all overlap
# diagram: http://swcarpentry.github.io/python-novice-inflammation/08-defensive/index.html

# normal tendency is to do:
#   Write a function range_overlap.
#   Call it interactively on two or three different inputs.
#   If it produces the wrong answer, fix the function and re-run that test.
# better practice is to:
#   Write a short function for each test.
#   Write a range_overlap function that should pass those tests.
#   If range_overlap produces any wrong answers, fix it and re-run the test functions.

#### Debugging ####

# overview practices

## Challenge: pair up, introduce error, try to debug with applying principles

#### Command-line programs ####

# switch to command line
# download code file: http://swcarpentry.github.io/python-novice-inflammation/data/python-novice-inflammation-code.zip


#### Wrapping up ####

# review objectives
# preview next week's objectives
