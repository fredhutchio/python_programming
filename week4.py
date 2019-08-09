#### Intermediate Python: Programming ####

#### Objectives ####

# review previous week's objectives
# Today:
#   apply test-driven development to creating new functions

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

# know what program is supposed to do
# writing test cases for scientific software is frequently harder than writing test cases for commercial applications, because if we knew what the output of the scientific code was supposed to be, we wouldn’t be running the software: we’d be writing up our results and moving on to the next program
# in practice:
#   Test with simplified data
#   Test a simplified case
#   Compare to an oracle (something which has trusted results)
#   Check conservation laws
#   Visualize

# find a test case that makes it fail every time
#   make it fail fast: localize failure to specific place in code

# change one thing at a time, for a reason
#   keep track of what you've done (lab notebook, notes, or ideally version control)

# be humble: learn from mistakes, and ask for help
#   a week of hard work can sometimes save you an hour of thought

## Challenge: pair up, introduce error, try to debug with applying principles

#### Command-line programs ####

# download code file: http://swcarpentry.github.io/python-novice-inflammation/code/python-novice-inflammation-code.zip
#   can do this by clicking on link and downloading zip, unzipping, moving code/ to project directory
#   using python code:
import os
import urllib.request
import zipfile
urllib.request.urlretrieve("http://swcarpentry.github.io/python-novice-inflammation/code/python-novice-inflammation-code.zip", "python-novice-inflammation-code.zip")
zipData = zipfile.ZipFile("python-novice-inflammation-code.zip")
zipData.extractall()
# this directory contains example scripts for us to use in exploring how command-line python programs work

# intro to command line: how many folks have experience on command line (Unix/bash)
# differences between interpreter (Atom or Jupyter notebook) and command line
#   interpreter directly interacts with python code
#   command line accesses bash/unix commands and programs
# demo running python from other interfaces
# accessing command line:
#   Mac: terminal
#   Windows: Anaconda prompt
#   alternatively, run all commands from interpreter with ! in front, which indicates the following is a command line, rather than interpreted by python

# print average inflammation per patient for a given file
!python code/readings_04.py --mean data/inflammation-01.csv

# look at the minimum of first four lines
!head -4 data/inflammation-01.csv | python code/readings_06.py --min

# max inflammation of several files
python code/readings_04.py --max data/inflammation-*.csv

# Our scripts should do the following:
#   If no filename is given on the command line, read data from standard input.
#   If one or more filenames are given, read data from them and report statistics for each file separately.
#   Use the --min, --mean, or --max flag to determine what statistic to print.

# create a new text file (in text editor) called sys_version.py
import sys # import system library
print('version is', sys.version) # tell us what version of python we're running

# run program
!python sys_version.py
#!python code//sys_version.py # in teaching materials

# another file called argv_list.py
import sys
print('sys.argv is', sys.argv)

# run program
!python argv_list.py
#!python code/argv_list.py # in teaching materials
# run with multiple arguments
!python argv_list.py first second third
#!python code/argv_list.py first second third

# exporting Jupyter notebooks as script
#   can use drop down menu, but may not preserve line breaks
# add the following code to cell in notebook (at end)
#!jupyter nbconvert --to script name_of_notebook.ipynb
# can also run code in Anaconda prompt (without ! )

#### Wrapping up ####

# review objectives
# preview next week's objectives
