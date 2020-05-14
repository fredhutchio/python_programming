# Intermediate Python: Programming
# Class 2 Exercises

## Challenge show

In this class, we've noted that `plt.show()` may not be necessary for plots to appear using some Python interpreters. Try removing this line from the following for loop and view the output. How do you explain the results?
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

## Challenge first three

How could you modify the code in the [previous challenge](#challenge-show) so only the first three data files are visualized?

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

## Challenge more vowels

- Write a conditional statement that assesses whether a character is a vowel.
- Include the conditional statement in a for loop that counts the number of vowels in a character string (e.g., "Mary had a little lamb.").
- Test your code on a few individual words and full sentences.

## Challenge fence

You can "add" strings together using `+`,
such as: `"a" + "b"`.
Write a function called `fence` that takes two parameters called `original` and `wrapper` and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:

- input: `print(fence('name', '*'))`
- output: `*name*`

## Challenge test

Write code to test your two new functions (`analyze` and `detect_problems`).

## Challenge ice cream

The following code defines and tests a function to list the best and worst flavor of ice cream. Modify the code to improve its readability, and note what other information a user would need to be able to run the code. *Extra:* Explain the difference between the use of `print` and `return` in the output.

```
def hippopotamus(x,y):
    foo=["chocolate","vanilla","strawberry"]
    print(foo[x])
    return foo[y]
hippopotamus(1,0)
```

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
```

## Challenge outer

If the variable `s` refers to a string, then `s[0]`` is the string’s first character and `s[-1]`` is its last. Write a function called `outer` that returns a string made up of just the first and last characters of its input. A call to your function should look like this:

- input: `print(outer('helium'))`
- output: `hm`
