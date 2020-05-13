# Intermediate Python: Programming
# Class 1 Solutions

## Challenge small

Import `small-01.csv` (included in your `data/` directory) and determine if these data differ in type or shape from our existing data object.
```
small_data = np.loadtxt(fname="data/small-01.csv", delimiter=",")
print(small_data.shape)
print(small_data.dtype)
type(small_data)
```

## Challenge stats

Find the maximum, minimum, and standard deviation across the entire array `data`, reported with meaningful print statements.
```
print("maximum:", np.max(data))
print("minimum:", np.min(data))
print("standard deviation:", np.std(data))
```

## Challenge data

Plot the maximum and minimum inflammation across all patients for `data`. What can you conclude about the validity of the data based on these plots?
```
plt.plot(np.max(data, axis=0))
plt.plot(np.min(data, axis=0))
```

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

- `plt.figure()` initializes the space into which the plots will be placed,
parameter `figsize` specifies the size of this space.
- `add_subplot` places each subplot into the figure; the first parameter indicates the total rows for subplots, the second paramter indicates columns of subplots, and the third parameter specifies the plot position (left-to-right, top-to-bottom)
- `axes1`, `axes2`, and `axes3` are variables storing each subplot
- `set_ylabel()` adds axis labels (there is also an equivalent for the x axis)
- `fig.tight_layout()` specifies the relative arrangement of subplots

## Challenge vowels

Given the following code, replace `ACTION` with code that will allow you to count the number of vowels.
```
length = 0
for vowel in "aeiou":
    length = length + 1
print("There are", length, "vowels")

# alternate answer
length = 0
for vowel in "aeiou":
    length += 1
print("There are", length, "vowels")
```

## Challenge files

Do all of the `data/inflammation*.csv` files contain the same amount of data (i.e., same number of elements)? Write a for loop that assesses the shape of each file.
```
for f in filenames:
    data = numpy.loadtxt(fname = f, delimiter = ",")
    print("shape of", f, ":", data.shape) #
```

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
the

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
