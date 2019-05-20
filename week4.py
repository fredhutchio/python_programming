#### [[course and class]] ####

#### Objectives ####

# review previous week's objectives
# Today:
#   identify types of errors as reported by python
#   correct errors reported in Python

#### Errors and Exceptions ####

# example traceback: execute all at once
def favorite_ice_cream():
    ice_creams = [
        "chocolate",
        "vanilla",
        "strawberry"
    ]
    print(ice_creams[3])

favorite_ice_cream()

# interpreting traceback:
#   determine number of levels by looking for arrows on lefthand side
#   first arrow points to line 8, favorite_ice_cream()
#   second arrow shows code within function, line 6
#   last level shown is where error occurred
#   most of the time you can pay attention to last level!

# three main types of errors

## Syntax errors

# error from defining a function incorrectly
def some_function()
    msg = "hello, world!"
    print(msg)
     return msg
# colon error: add colon to first line
def some_function():
    msg = "hello, world!"
    print(msg)
     return msg
# another error! IntentationError is a type of syntax, but is always about indentation
# correct indentation:
def some_function():
    msg = "hello, world!"
    print(msg)
    return msg
# whitespace: tabs and spaces
# many interpreters correct spaces meant to be tabs, but python doesn't allow you to mix!

## Variable name errors

# try to print a variable
print(octopus)
# NameErrors can be difficult to fix
# common problem is that it's not a variable, but a string you forgot to place quotations around
print("octopus")
# another problem: forgot to create variable before using it:
#count = 0 # add this to fix it
for number in range(10):
    count = count + number
print("The count is:", count)
# if you accidentally include Count = 0 instead, this will also give variable name error!

## Index errors
# accessing an item in a container that doesn't exist
letters = ['a', 'b', 'c']
print("Letter #1 is", letters[0])
print("Letter #2 is", letters[1])
print("Letter #3 is", letters[2])
print("Letter #4 is", letters[3])

## File errors

# trying to read a file that doesn't exist, or is in a different location
file_handle = open('myfile.txt')
file_handle = open("inflammation-01.csv", 'r')
# attempt to write to a file that was opened read-only: UnsupportedOperationError
# also IOErrors or OSErrors, depending on the version of Python

## Challenge:
# This code has an intentional error. Do not type it directly;
# use it for reference to understand the error message below.
def print_message(day):
    messages = {
        "monday": "Hello, world!",
        "tuesday": "Today is tuesday!",
        "wednesday": "It is the middle of the week.",
        "thursday": "Today is Donnerstag in German!",
        "friday": "Last day of the week!",
        "saturday": "Hooray for the weekend!",
        "sunday": "Aw, the weekend is almost over."
    }
    print(messages[day])

def print_friday_message():
    print_message("Friday")

print_friday_message()

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
