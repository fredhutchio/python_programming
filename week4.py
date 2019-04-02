#### [[course and class]] ####

#### Objectives ####

# review previous week's objectives
# Today:
#

#### Errors and Exceptions ####

# example traceback
def favorite_ice_cream():
    ice_creams = [
        "chocolate",
        "vanilla",
        "strawberry"
    ]
    print(ice_creams[3])

favorite_ice_cream()

#syntax errors
# colon
#indentation

# variable name errors

# index errors

# file errors

#### Defensive programming ####

# are we getting the right answer?
#   Write programs that check their own operation.
#   Write and run tests for widely-used functions.
#   Make sure we know what “correct” actually means.

# assume mistakes will happen and guard against them (defensive programming)

# assertions: statement that something must be true at a certain point in a program
numbers = [1.5, 2.3, 0.7, -0.001, 4.4]
total = 0.0
for n in numbers:
    assert n > 0.0, 'Data should only contain positive values'
    total += n
print('total is:', total)
# types:
#   precondition is something that must be true at the start of a function in order for it to work correctly.
#   postcondition is something that the function guarantees is true when it finishes.
#   invariant is something that is always true at a particular point inside a piece of code.

# test driven development
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
