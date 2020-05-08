# Intermediate Python: Programming
# Class 2 Exercises

## Challenge: Given the following code, what answer do you expect to be correct?
if 4 > 5:
    print("A")
elif 4 == 5:
    print("B")
elif 4 < 5:
    print("C")
## How would you rewrite the code to get another answer?
# C gets printed because the first two conditions, 4 > 5 and 4 == 5, are not true, but 4 < 5 is true.

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

Challenge: You can "add" strings together using +, such as:
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

## Challenge: If the variable s refers to a string, then s[0] is the string’s first character and s[-1] is its last. Write a function called outer that returns a string made up of just the first and last characters of its input. A call to your function should look like this: "print(outer('helium'))" and you should get "hm"
def outer(input_string):
    return input_string[0] + input_string[-1]

print(outer("helium"))
