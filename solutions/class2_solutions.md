# Intermediate Python: Programming
# Class 2 Exercises

## Challenge show

In this lesson, we've noted that `plt.show()` may not be necessary for plots to appear using some Python interpreters. Try removing this line from the for loop and view the output. How do you explain the results?
```
import glob
import numpy as np
import matplotlib.pyplot as plt

filenames = sorted(glob.glob("data/inflammation*.csv"))
for filename in filenames:
    print(filename)

    data = np.loadtxt(fname=filename, delimiter=',')

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(np.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(np.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(np.min(data, axis=0))

    fig.tight_layout()
    plt.show()
```
Without that line of code,
the filenames are all printed first, and then all plots are shown after.
Including the line allows the filename to be printed just before the relevant plot.

## Challenge first three

How could you modify the code in the last challenge so only the first three data files are visualized?

Add the following line of code:
```
...
filenames = sorted(glob.glob("data/inflammation*.csv"))
filenames = filenames[0:3]
for filename in filenames:
...
```
Alternatively,
modify the for loop:
```
...
for filename in filenames[0:3]
...
```

## Challenge conditionals

Given the following code, what answer (A, B, or C) do you expect to be correct? How would you rewrite the code to get another answer?

```
if 4 < 5:
    print("A")
elif 4 == 5:
    print("B")
elif 4 < 5:
    print("C")
```

C gets printed because the first two conditions, 4 > 5 and 4 == 5, are not true, but 4 < 5 is true.

## Challenge more vowels

- Write a conditional statement that assesses whether a character is a vowel.
- Include the conditional statement in a for loop that counts the number of vowels in a character string (e.g., "Mary had a little lamb.").
- Test your code on a few individual words and full sentences.

Given the following sentence:
```
sentence = "Mary had a little lamb."
```

One example solution:
```
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1

print("The number of vowels in this string is " + str(count))
```
Other considerations include whether capitalization was included,
and if y is included as a vowel.

Other potential solutions:
```
vowels = 0

for char in sentence:
    if char in ("a", "e", "i", "o", "u", "y"):
        vowels = vowels + 1
    elif char in ("A", "E", "I", "O", "U", "Y"):
        vowels = vowels + 1
    else:
        vowels = vowels
print(vowels)
```

```
count = 0

for char in sentence:
    print(char)
    if char in ("a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"):
        count = count + 1
print("There are ", count, " vowels")
```

```    
count = 0

for letter in string:
    for item in "aeiouyAEIOUY":
        if letter == item:
            count +=1
print("There are", count, "vowels in the string:", string)
```

## Challenge fence

You can "add" strings together using `+`,
such as: `"a" + "b"`.
Write a function called `fence` that takes two parameters called `original` and `wrapper` and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:

- input: `print(fence('name', '*'))`
- output: `*name*`

```
def fence(original, wrapper):
    return wrapper + original + wrapper

print(fence("name", "*"))
```

## Challenge ice cream

The following code defines and tests a function to list the best and worst flavor of ice cream. Modify the code to improve its readability, and note what other information a user would need to be able to run the code. *Extra:* Explain the difference between the use of `print` and `return` in the output.

```
def hippopotamus(x,y):
    foo=["chocolate","vanilla","strawberry"]
    print(foo[x])
    return foo[y]
hippopotamus(1,0)
```

Modified for readability
```
def ice_cream(x,y):
    flavors=["chocolate",
            "vanilla",
            "strawberry"]
    return flavors[y], flavors[x]
ice_cream(1,0)
```
Information to use this function: "The user should enter the best flavor first and the worst flavor second, where 0=chocolate, 1=vanilla, and 3=strawberry"

## Challenge f2k

What does the following piece of code display when run — and why?
```
f = 0
k = 0

def f2k(f):
    k = ((f-32)*(5.0/9.0)) + 273.15
    return k

f2k(8)
f2k(41)
f2k(32)

print(k)
```
The `k` inside the function is a separate variable from the one initialized before the function.

## Challenge swap

Explain the result of the following code:
```
a = 3
b = 7

def swap(a, b):
    temp = a
    a = b
    b = temp

swap(a, b)

print(a, b)

print(swap(a,b))
```

`a` and `b` are defined locally within the function,
and these are independent of the original variables created.
Moreover, no values are returned inside the function,
so the last line has no output to report.

## Challenge outer

If the variable `s` refers to a string, then `s[0]` is the string’s first character and `s[-1]` is its last. Write a function called `outer` that returns a string made up of just the first and last characters of its input. A call to your function should look like this:

- input: `print(outer('helium'))`
- output: `hm`

```
def outer(input_string):
    return input_string[0] + input_string[-1]

print(outer("helium"))
```
