#!/usr/bin/env python3

#### Intermediate Python: Programming ####

#### Objectives ####

# review previous week's objectives
# Today:
#   make choices using conditional statements: if, elif, else
#   evaluate expressions containing and and or
#   combine for loops and conditional statements
#   create functions

# link to materials with diagram and full text of exercises: http://swcarpentry.github.io/python-novice-inflammation/06-func/index.html

#### Making choices ####

# tell python to take different actions with if statements
# need to highlight all code to run at once in Atom!
num = 37
if num > 100:
    print("greater")
else:
    print("not greater")
print("done")

# don"t need else; can also do nothing
# need to highlight all code to run at once in Atom!
num = 53
print("before conditional...")
if num > 100:
    print(num," is greater than 100")
print("...after conditional")

# can have multiple alternatives using elif
num = -3

if num > 0:
    print(num, "is positive")
elif num == 0: # double equal sign is necessary; single used to assign values
    print(num, "is zero")
else:
    print(num, "is negative")

# combine tests using and, when both parts must be true
if (1 > 0) and (-1 > 0):
    print("both parts are true")
else:
    print("at least one part is false")

# combine tests using or if at least one part must be true
if (1 < 0) or (-1 < 0):
    print("at least one test is true")
# true and false are booleans

## Challenge: Given the following code, what answer do you expect to be correct?
if 4 > 5:
    print("A")
elif 4 == 5:
    print("B")
elif 4 < 5:
    print("C")
## How would you rewrite the code to get another answer?
# C gets printed because the first two conditions, 4 > 5 and 4 == 5, are not true, but 4 < 5 is true.

# checking for problems in inflammation data
import glob # we'll use this later
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname="data/inflammation-01.csv", delimiter=",")

# find max for two days in the study
max_inflammation_0 = np.max(data, axis=0)[0]
max_inflammation_20 = np.max(data, axis=0)[20]

# we suspect there may be a mistake in data entry (day number accidentally entered as inflammation value)
# check if max equals day number
if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print("Suspicious looking maxima!")

# check if any patients are have zero total inflammation (healthy patient)
if np.sum(np.min(data, axis=0)) == 0:
    print("Minima add up to zero!")

# combine together and test on another data file
data = np.loadtxt(fname="data/inflammation-03.csv", delimiter=",")

max_inflammation_0 = np.max(data, axis=0)[0]
max_inflammation_20 = np.max(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print("Suspicious looking maxima!")
elif np.sum(np.min(data, axis=0)) == 0:
    print("Minima add up to zero!")
else:
    print("Seems OK!")

## Challenge:
# Write a loop that counts the number of vowels in a character string.
# Test it on the sentence "Mary had a little lamb."
vowels = "aeiouAEIOU"
sentence = "Mary had a little lamb."
count = 0
for char in sentence:
    if char in vowels:
        count += 1 # same as count = count + 1

print("The number of vowels in this string is " + str(count))

#### Creating functions ####

# define a function that converts F to C
def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))
# why can"t you print the result instead of return?
# return function causes function to stop

# test function
fahr_to_celsius(32)

# test function with meaningful print statements
print("freezing point of water:", fahr_to_celsius(32), "C")
print("boiling point of water:", fahr_to_celsius(212), "C")

# convert C to K by composing functions: to apply one function to the result of another
def celsius_to_kelvin(temp_c):
    return temp_c + 273.15

print("freezing point of water in Kelvin:", celsius_to_kelvin(0.))

# converting F to K
def fahr_to_kelvin(temp_f):
    temp_c = fahr_to_celsius(temp_f)
    temp_k = celsius_to_kelvin(temp_c)
    return temp_k

print("boiling point of water in Kelvin:", fahr_to_kelvin(212.0))

## Challenge: You can "add" strings together using +, such as:
"a" + "b"
## Write a function called fence that takes two parameters called original and wrapper and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:
# input: print(fence('name', '*'))
# output: *name*
def fence(original, wrapper):
    return wrapper + original + wrapper

print(fence("name", "*"))

## Challenge: What does the following piece of code display when run — and why?
f = 0
k = 0

def f2k(f):
    k = ((f-32)*(5.0/9.0)) + 273.15
    return k

f2k(8)
f2k(41)
f2k(32)

print(k)

# create function to analyze files with data viz
def analyze(filename):

    data = np.loadtxt(fname=filename, delimiter=",")

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel("average")
    axes1.plot(np.mean(data, axis=0))

    axes2.set_ylabel("max")
    axes2.plot(np.max(data, axis=0))

    axes3.set_ylabel("min")
    axes3.plot(np.min(data, axis=0))

    fig.tight_layout()
    plt.show()
# why don't we need to include a return statement?

# create function to detect data errors
def detect_problems(filename):

    data = np.loadtxt(fname=filename, delimiter=",")

    if np.max(data, axis=0)[0] == 0 and np.max(data, axis=0)[20] == 20:
        print("Suspicious looking maxima!")
    elif np.sum(np.min(data, axis=0)) == 0:
        print("Minima add up to zero!")
    else:
        print("Seems OK!")

# use both functions across all files in for loop
filenames = sorted(glob.glob("data/inflammation*.csv"))

for f in filenames[:3]:
    print(f)
    analyze(f)
    detect_problems(f)

## Challenge: Write a function called outer that returns a string made up of just the first and last characters of its input. A call to your function should look like this: "print(outer('helium'))" and you should get "hm"
# Hint:  If the variable s refers to a string, then s[0] is the string’s first character and s[-1] is its last. 
def outer(input_string):
    return input_string[0] + input_string[-1]

print(outer("helium"))

#### Wrapping up ####

# review objectives
# preview next week's objectives
