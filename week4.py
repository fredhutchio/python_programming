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

# we're going to work through the process of defining and testing a function, while pretending to encounter some of the common errors associated with this process

# normal tendency is to do:
#   Write a function range_overlap.
#   Call it interactively on two or three different inputs.
#   If it produces the wrong answer, fix the function and re-run that test.
# better practice is to:
#   Write a short function for each test.
#   Write a range_overlap function that should pass those tests.
#   If range_overlap produces any wrong answers, fix it and re-run the test functions.

# three test functions for range_overlap:
assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0) # one input
assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0) # two inputs
assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0) # three inputs
# errors are expected! we haven't written the function yet; if tests passed we'd be accidentally using someone else's function
# this implicitly defines what our input and output look like: a list of pairs as input, and produce a single pair as output

# how to test for cases where ranges don't overlap at all?
assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == ???
# fail with an error message, produce a special value like (0.0, 0.0) to signal that there’s no overlap, or something else?
# decision: we will return the special value None when there’s no overlap

# what about when ranges touch at endpoints?
assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == ???
# is this overlap?
# decision: every overlap has to have non-zero width

# complete previous assertions
assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None

# define function:
def range_overlap(ranges):
    '''Return common overlap among a set of [left, right] ranges.'''
    max_left = 0.0
    min_right = 1.0
    for (left, right) in ranges:
        max_left = max(max_left, left)
        min_right = min(min_right, right)
    return (max_left, min_right)

# add assertions to test function
def test_range_overlap():
    assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
    assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None
    assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
    assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([]) == None

# finally test the function call
test_range_overlap()
# first test to produce None fails, we need to correct our function
# we don't know if other tests failed, because the program halts with the first error
# initializing max_left and min_right to 0.0 and 1.0 respectively, regardless of the input values
# another rule of programming: always initialize from data

## Challenge: Fix range_overlap. Re-run test_range_overlap after each change you make.
def range_overlap(ranges):
    '''Return common overlap among a set of [left, right] ranges.'''
    if not ranges:
        # ranges is None or an empty list
        return None
    max_left, min_right = ranges[0]
    for (left, right) in ranges[1:]:
        max_left = max(max_left, left)
        min_right = min(min_right, right)
    if max_left >= min_right:  # no overlap
        return None
    return (max_left, min_right)

#### Debugging ####

# overview practices

## Challenge: pair up, introduce error, try to debug with applying principles

#### Command-line programs ####

# switch to command line
# download code file: http://swcarpentry.github.io/python-novice-inflammation/data/python-novice-inflammation-code.zip


#### Wrapping up ####

# review objectives
# preview next week's objectives
