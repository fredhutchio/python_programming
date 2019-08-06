#!/usr/bin/env python3

#### Intermediate Python: Programming ####

#### Objectives ####

# review previous week's objectives
# Today:
#   testing and validating complex functions
#   including help documentation within a function
#   defining defaults for a function
#   applying readable code convention to functions
#   identify and correct common errors reported by Python

## Challenge: what will be printed if you run this code?
a = 3
b = 7

def swap(a, b):
    temp = a
    a = b
    b = temp

swap(a, b)

print(a, b)
## Challenge: how could you alter this to print the results of swap?

#### Testing and documenting ####

# validating that a function works as expected is an important step in coding
# this section creates a new function that manipulates the data
# difference between testing (verification) and validating:
#   testing/verifying: does code do what we expect?
#   validating: does code meet our need (stated goal)?

import numpy as np

# write a function to offset data by a new user-selected mean value
def offset_mean(data, target_mean_value):
    return (data - np.mean(data)) + target_mean_value

# create test matrix of 0s
z = np.zeros((2,2))
print(z)
# offset values using new function
print(offset_mean(z, 3))

# use offset function on real data
data = np.loadtxt(fname="data/inflammation-01.csv", delimiter=",")
print(offset_mean(data, 0))

# confirm offset has worked
print('original min, mean, and max are:', np.min(data), np.mean(data), np.max(data))
offset_data = offset_mean(data, 0)
print('min, mean, and max of offset data are:',
      np.min(offset_data),
      np.mean(offset_data),
      np.max(offset_data))
# offset isn't exact, but is close

# check standard deviation
print('std dev before and after:', np.std(data), np.std(offset_data))
# check more precisely
print('difference in standard deviations before and after:',
      np.std(data) - np.std(offset_data))

# we could add documentation to offset function to describe its purpose using comments:

# offset_mean(data, target_mean_value)
# return a new array containing the original data with its mean offset to match the desired value.
def offset_mean(data, target_mean_value):
    return (data - np.mean(data)) + target_mean_value

# a better way: add string to function itself, which embeds in help documentation
def offset_mean(data, target_mean_value):
    '''Return a new array containing the original data
       with its mean offset to match the desired value.'''
    return (data - np.mean(data)) + target_mean_value

# view help documentation
help(offset_mean)

# docstring; triple quotes aren't necessary, but allow us to break into separate lines (and add example)
def offset_mean(data, target_mean_value):
    '''Return a new array containing the original data
       with its mean offset to match the desired value.
    Example: offset_mean([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - np.mean(data)) + target_mean_value
help(offset_mean)

## Challenge: given the following function (written in last week's class), add a docstring
def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))

#### Defining defaults ####

# pass the filename to loadtxt without the fname=
np.loadtxt(fname="data/inflammation-01.csv", delimiter=",")
np.loadtxt("data/inflammation-01.csv", delimiter=",")
# delimiter needs to be there! this gives an error:
np.loadtxt("data/inflammation-01.csv", ",")

# redefine offset mean, which makes the default 0.0
def offset_mean(data, target_mean_value=0.0):
    '''Return a new array containing the original data with its mean offset to match the
       desired value (0 by default).
    Example: offset_mean([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - np.mean(data)) + target_mean_value

# can still call function with two arguments
test_data = np.zeros((2, 2))
print(offset_mean(test_data, 3))

# call it with just one parameter, target_mean_value automatically assigned the default value of 0.0
more_data = 5 + np.zeros((2, 2))
print('data before mean offset:', more_data)
print('offset data:', offset_mean(more_data))

# how Python matches values to parameters:
def display(a=1, b=2, c=3):
    print('a:', a, 'b:', b, 'c:', c)

print('no parameters:')
display()
print('one parameter:')
display(55)
print('two parameters:')
display(55, 66)

# parameters are matched left to right
# any without value given by user automatically get default value

# override behavior by naming value as it's passed (entered)
print('only setting the value of c')
display(c=77)

# interpreting help documentation: example from np.loadtxt
help(np.loadtxt)
# loadtxt has one parameter called fname that doesn’t have a default value, and eight others that do
# np.loadtxt('inflammation-01.csv', ',')
# doesn't work because delimiter isn't the second argument in the help doc, so the function assigns the wrong default argument

## Challenge: given the following code, what do you expect to be written? Run it to confirm your answer
def numbers(one, two=2, three, four=4):
    n = str(one) + str(two) + str(three) + str(four)
    return n

print(numbers(1, three=3))
# answer: one must be defined as an input since it does not have a default value

## Challenge: what does the following code display when run?
def func(a, b=3, c=6):
    print('a: ', a, 'b: ', b, 'c:', c)

func(-1, 2)

# answer: a: -1 b: 2 c: 6

#### Readable functions ####

# show examples in exercises/week3_example*.py:

# Example 1
def s(p):
    a=0
    for v in p:
        a+=v
    m=a/len(p)
    d=0
    for v in p:
        d+=(v-m)*(v-m)
    return np.sqrt(d/(len(p)-1))

# Example 2
def std_dev(sample):
    sample_sum = 0
    for value in sample:
        sample_sum += value

    sample_mean = sample_sum / len(sample)

    sum_squared_devs = 0
    for value in sample:
        sum_squared_devs += (value - sample_mean) * (value - sample_mean)

    return np.sqrt(sum_squared_devs / (len(sample) - 1))

# readable code:
#   meaningful variable names
#   blank spaces

## Challenge: Revise a function you wrote for one of the previous exercises to try to make the code more readable. Then, collaborate with one of your neighbors to critique each other’s functions and discuss how your function implementations could be further improved to make them more readable.

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

#### Wrapping up ####

# review objectives
# preview next week's objectives
