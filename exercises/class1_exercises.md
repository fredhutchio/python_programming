# Intermediate Python: Programming
# Class 1 Exercises

## Challenge small

Import `small-01.csv` (included in your `data/` directory) and determine if these data differ in type or shape from our existing data object.

## Challenge stats

Find the maximum, minimum, and standard deviation across the entire array `data`, reported with meaningful print statements.

## Challenge data

Plot the maximum and minimum inflammation across all patients for `data`. What can you conclude about the validity of the data based on these plots?

## Challenge comment

Look at the code below and include a comment for each new function or argument you see.
```
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

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

## Challenge vowels

Given the following code, replace `ACTION` with code that will allow you to count the number of vowels.
```
length = 0
for vowel in "aeiou":
    ACTION
print("There are", length, "vowels")
```

## Challenge files

Do all of the `data/inflammation*.csv` files contain the same amount of data (i.e., same number of elements)? Write a for loop that assesses the shape of each file.
