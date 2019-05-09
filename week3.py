#!/usr/bin/env python3

#### Intermediate Python: Programming ####

#### Objectives ####

# review previous week's objectives
# Today:
#   testing and validating complex functions
#   including help documentation within a function
#   defining defaults for a function
#   applying readable code convention to functions


#### Testing and documenting ####

# write a function to offset data (allows to test functions)
def offset_mean(data, target_mean_value):
    return (data - numpy.mean(data)) + target_mean_value

# create test matrix of 0s and offset values using new function (to test it)
z = numpy.zeros((2,2))
print(offset_mean(z, 3))

# use offset function on real data
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
print(offset_mean(data, 0))

# confirm offset has worked
print('original min, mean, and max are:', numpy.min(data), numpy.mean(data), numpy.max(data))
offset_data = offset_mean(data, 0)
print('min, mean, and max of offset data are:',
      numpy.min(offset_data),
      numpy.mean(offset_data),
      numpy.max(offset_data))
# offset isn't exact, but is close

# check standard deviation
print('std dev before and after:', numpy.std(data), numpy.std(offset_data))
# check more precisely
print('difference in standard deviations before and after:',
      numpy.std(data) - numpy.std(offset_data))

# we could add documentation to offset function to describe its purpose using comments

# a better way: add string to function itself, which embeds in help documentation
def offset_mean(data, target_mean_value):
    '''Return a new array containing the original data
       with its mean offset to match the desired value.'''
    return (data - numpy.mean(data)) + target_mean_value

# view help documentation
help(offset_mean)

# docstring; triple quotes aren't necessary, but allow us to break into separate lines (and add example)
def offset_mean(data, target_mean_value):
    '''Return a new array containing the original data
       with its mean offset to match the desired value.
    Example: offset_mean([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - numpy.mean(data)) + target_mean_value
help(offset_mean)

## Challenge:

#### Defining defaults ####

# pass the filename to loadtxt without the fname=
numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
numpy.loadtxt('inflammation-01.csv', delimiter=',')
# delimiter needs to be there!
numpy.loadtxt('inflammation-01.csv', ',')

# redefine offset mean, which makes the default 0.0
def offset_mean(data, target_mean_value=0.0):
    '''Return a new array containing the original data with its mean offset to match the
       desired value (0 by default).
    Example: offset_mean([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - numpy.mean(data)) + target_mean_value

# can still call function with two arguments
test_data = numpy.zeros((2, 2))
print(offset_mean(test_data, 3))

# call it with just one parameter, target_mean_value automatically assigned the default value of 0.0
more_data = 5 + numpy.zeros((2, 2))
print('data before mean offset:')
print(more_data)
print('offset data:')
print(offset_mean(more_data))

# how Python matches values to parameters:
def display(a=1, b=2, c=3):
    print('a:', a, 'b:', b, 'c:', c)

print('no parameters:')
display()
print('one parameter:')
display(55)
print('two parameters:')
display(55, 66)

# override behavior by naming value as it's passed
print('only setting the value of c')
display(c=77)

# interpreting help documentation
help(numpy.loadtxt)
# loadtxt has one parameter called fname that doesn’t have a default value, and eight others that do
# numpy.loadtxt('inflammation-01.csv', ',')
# doesn't work because delimiter isn't the second argument in the help doc, so the function assigns the wrong default argument

## Challenge:

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
    return numpy.sqrt(d/(len(p)-1))

# Example 2
def std_dev(sample):
    sample_sum = 0
    for value in sample:
        sample_sum += value

    sample_mean = sample_sum / len(sample)

    sum_squared_devs = 0
    for value in sample:
        sum_squared_devs += (value - sample_mean) * (value - sample_mean)

    return numpy.sqrt(sum_squared_devs / (len(sample) - 1))

# readable code:
#   meaningful variable names
#   blank spaces

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

## Revise a function you wrote for one of the previous exercises to try to make the code more readable. Then, collaborate with one of your neighbors to critique each other’s functions and discuss how your function implementations could be further improved to make them more readable.

#### Wrapping up ####

# review objectives
# preview next week's objectives
