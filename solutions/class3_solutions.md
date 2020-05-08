# Intermediate Python: Programming
# Class 3 Exercises

## Challenge: given the following function (written in last week's class), add a docstring
def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))


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
