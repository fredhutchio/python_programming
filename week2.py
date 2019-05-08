#### [[course and class]] ####

#### Objectives ####

# review previous week"s objectives
# Today:
#   make choices using conditional statements: if, elif, else
#   evaluate expressions containing and and or
#   combine for loops and conditional statements
#   create functions

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
    print('A')
elif 4 == 5:
    print('B')
elif 4 < 5:
    print('C')
## How would you rewrite the code to get another answer?
# C gets printed because the first two conditions, 4 > 5 and 4 == 5, are not true, but 4 < 5 is true.

# checking for problems in inflammation data
import numpy

data = numpy.loadtxt(fname="data/inflammation-01.csv", delimiter=",")

# find max for two days in the study
max_inflammation_0 = numpy.max(data, axis=0)[0]
max_inflammation_20 = numpy.max(data, axis=0)[20]

# check if max equals day number (indicating error in data entry)
if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print("Suspicious looking maxima!")

# check if any patients are have zero total inflammation (healthy patient)
if numpy.sum(numpy.min(data, axis=0)) == 0:
    print("Minima add up to zero!")

# combine together and test on another data file
data = numpy.loadtxt(fname="inflammation-03.csv", delimiter=",")

max_inflammation_0 = numpy.max(data, axis=0)[0]
max_inflammation_20 = numpy.max(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print("Suspicious looking maxima!")
elif numpy.sum(numpy.min(data, axis=0)) == 0:
    print("Minima add up to zero!")
else:
    print("Seems OK!")

## Challenge:
# Write a loop that counts the number of vowels in a character string.
# Test it on a few individual words and full sentences.
# Once you are done, compare your solution to your neighbor’s. Did you make the same decisions about how to handle the letter ‘y’ (which some people think is a vowel, and some do not)?
vowels = "aeiouAEIOU"
sentence = "Mary had a little lamb."
count = 0
for char in sentence:
    if char in vowels:
        count += 1

print("The number of vowels in this string is " + str(count))

#### Wrapping up ####

# review objectives
# preview next week"s objectives
