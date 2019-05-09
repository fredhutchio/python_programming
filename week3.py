#!/usr/bin/env python3

#### Intermediate Python: Programming ####

#### Objectives ####

# review previous week's objectives
# Today:
#

#### Creating functions ####

# Objectives: define new functions that takes parameters, return value from function, test and debug, set default values for function parameters

# functions allow us to create a shorthand way to re-execute longer pieces of code
# define function that converts temps from F to C
def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))

# test function
fahr_to_celsius(32)
# we can use this the same way we use other functions
print('freezing point of water:', fahr_to_celsius(32), 'C')
print('boiling point of water:', fahr_to_celsius(212), 'C')

# composing functions
# write a function to convert C to K
def celsius_to_kelvin(temp_c):
    return temp_c + 273.15

print('freezing point of water in Kelvin:', celsius_to_kelvin(0.))

# convert F to K: compose the two functions we have already created (to apply one function to the result of another)
def fahr_to_kelvin(temp_f):
    temp_c = fahr_to_celsius(temp_f)
    temp_k = celsius_to_kelvin(temp_c)
    return temp_k

print('boiling point of water in Kelvin:', fahr_to_kelvin(212.0))

## Challenge: “Adding” two strings produces their concatenation: 'a' + 'b' is 'ab'. Write a function called fence that takes two parameters called original and wrapper and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:
# input: print(fence('name', '*'))
# output: *name*
def fence(original, wrapper):
    return wrapper + original + wrapper

## Challenge: Note that return and print are not interchangeable. print is a Python function that prints data to the screen. It enables us, users, see the data. return statement, on the other hand, makes data visible to the program. Let’s have a look at the following function:
def add(a, b):
    print(a + b)
# What will we see if we execute the following commands?
A = add(7, 3)
print(A)
# Python will first execute the function add with a = 7 and b = 3, and, therefore, print 10. However, because function add does not have a line that starts with return (no return “statement”), it will, by default, return nothing which, in Python world, is called None. Therefore, A will be assigned to None and the last line (print(A)) will print None. As a result, we will see:
#10
#NONE

# make inflammation process easier to read and reuse by defining code as function
def analyze(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

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

# make a function to find the problems we noticed earlier
def detect_problems(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')

# we can run both at once across all files in a for loop
filenames = sorted(glob.glob('inflammation*.csv'))

for f in filenames[:3]:
    print(f)
    analyze(f)
    detect_problems(f)

# testing and documenting
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
# alternatively, add string to function itself, which embeds in help documentation
def offset_mean(data, target_mean_value):
    '''Return a new array containing the original data
       with its mean offset to match the desired value.'''
    return (data - numpy.mean(data)) + target_mean_value
help(offset_mean)
# docstring; triple quotes allows us to break into separate lines (and add example)
def offset_mean(data, target_mean_value):
    '''Return a new array containing the original data
       with its mean offset to match the desired value.
    Example: offset_mean([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - numpy.mean(data)) + target_mean_value
help(offset_mean)

# defining defaults
# pass the filename to loadtxt without the fname=
numpy.loadtxt('inflammation-01.csv', delimiter=',')
# delimiter needs to be there!
numpy.loadtxt('inflammation-01.csv', ',')

# redefine offset mean
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

# readable functions
# show example: http://swcarpentry.github.io/python-novice-inflammation/06-func/index.html

## Challenge: Return vs print


#### Wrapping up ####

# review objectives
# preview next week's objectives
