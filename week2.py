#### [[course and class]] ####

#### Objectives ####

# review previous week's objectives
# Today:
#

#### Analyzing data from multiple files ####

# import library to find files/directories
import glob

# get names of all csv files in current directory
print(glob.glob('data/inflammation*.csv'))

# combine previous content together and analyze all files

import numpy
import matplotlib.pyplot

filenames = sorted(glob.glob('data/inflammation*.csv'))
filenames = filenames[0:3]
for f in filenames:
    print(f)

    data = numpy.loadtxt(fname=f, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()

## Challenge: Plot the difference between the average of the first dataset and the average of the second dataset, i.e., the difference between the leftmost plot of the first two figures.
import glob
import numpy
import matplotlib.pyplot

filenames = sorted(glob.glob('data/inflammation*.csv'))

data0 = numpy.loadtxt(fname=filenames[0], delimiter=',')
data1 = numpy.loadtxt(fname=filenames[1], delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

matplotlib.pyplot.ylabel('Difference in average')
matplotlib.pyplot.plot(numpy.mean(data0, axis=0) - numpy.mean(data1, axis=0))

fig.tight_layout()
matplotlib.pyplot.show()

#### Making choices ####

# Objectives: write conditional statements including if, elif, else; evaluate expressions containing and and or

# tell python to take different actions with if statements
num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')

# don't need else; can also do nothing
num = 53
print('before conditional...')
if num > 100:
    print(num,' is greater than 100')
print('...after conditional')

# can have multiple alternatives using elif
num = -3

if num > 0:
    print(num, 'is positive')
elif num == 0: # double equal sign is necessary; single used to assign values
    print(num, 'is zero')
else:
    print(num, 'is negative')

# combine tests using and, when both parts must be true
if (1 > 0) and (-1 > 0):
    print('both parts are true')
else:
    print('at least one part is false')

# combine tests using or if at least one part must be true
if (1 < 0) or (-1 < 0):
    print('at least one test is true')
# true and false are booleans

## Challenge: What do you expect to get from this code?
if 4 > 5:
    print('A')
elif 4 == 5:
    print('B')
elif 4 < 5:
    print('C')
# C gets printed because the first two conditions, 4 > 5 and 4 == 5, are not true, but 4 < 5 is true.

# checking for problems in inflammation data
import numpy # if not already done

# check if max inflammation equals day number (error in data entry)
max_inflammation_0 = numpy.max(data, axis=0)[0]
max_inflammation_20 = numpy.max(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')

# check if mins are all zero (healthy patient)
if numpy.sum(numpy.min(data, axis=0)) == 0:
    print('Minima add up to zero!')

# combine together with data
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

max_inflammation_0 = numpy.max(data, axis=0)[0]
max_inflammation_20 = numpy.max(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')
elif numpy.sum(numpy.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')

## Challenge:
# Write a loop that counts the number of vowels in a character string.
# Test it on a few individual words and full sentences.
# Once you are done, compare your solution to your neighbor’s. Did you make the same decisions about how to handle the letter ‘y’ (which some people think is a vowel, and some do not)?
vowels = 'aeiouAEIOU'
sentence = 'Mary had a little lamb.'
count = 0
for char in sentence:
    if char in vowels:
        count += 1

print("The number of vowels in this string is " + str(count))

#### Wrapping up ####

# review objectives
# preview next week's objectives
