# Intermediate Python: Programming
# Class 1 Exercises

## Challenge: import small-01.csv and determine if the type or shape of data differ from data object

```
small_data = numpy.loadtxt(fname="data/small-01.csv", delimiter=",")
print(small_data.shape)
print(small_data.dtype)
type(small_data)
```

## Challenge: find max, min, standard deviation across the entire array data, and print with meaningful print statements

```
print("maximum:", numpy.max(data))
print("minimum:", numpy.min(data))
print("standard deviation:", numpy.std(data))
```

## Challenge: using one line of code, print the maximum inflammation across all patients

```
matplotlib.pyplot.plot(numpy.max(data, axis=0))
```

## Challenge: Look at the code below and include a comment for each new function or argument you see.

```
import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

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
```

- `matplotlib.pyplot.figure()` initializes the space into which the plots will be placed,
parameter `figsize` specifies the size of this space.
- `add_subplot` places each subplot into the figure; the first parameter indicates the total rows for subplots, the second paramter indicates columns of subplots, and the third parameter specifies the plot position (left-to-right, top-to-bottom)
- `axes1`, `axes2`, and `axes3` are variables storing each subplot
- `set_xlabel()` adds axis labels
- `fig.tight_layout()` specifies the relative arrangement of subplots


## Challenge: Are all 12 data files the same shape? (hint: write a for loop)

```
for f in filenames:
    data = numpy.loadtxt(fname = f, delimiter = ",")
    print("shape of", f, ":", data.shape) # more informative print statement
```

## Challenge: Write a comment for each line of code in the following script. Which data files are suspicious?

```
import glob
import numpy
import matplotlib.pyplot

filenames = sorted(glob.glob("data/inflammation*.csv"))
filenames = filenames[0:3]
for f in filenames:
    print(f)

    data = numpy.loadtxt(fname=f, delimiter=",")

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel("average")
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel("max")
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel("min")
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()
```

## Challenge: Plot the difference between the average of the first dataset and the average of the second dataset, i.e., the difference between the leftmost plot of the first two figures.
```
import glob
import numpy
import matplotlib.pyplot

filenames = sorted(glob.glob("data/inflammation*.csv"))

data0 = numpy.loadtxt(fname=filenames[0], delimiter=",")
data1 = numpy.loadtxt(fname=filenames[1], delimiter=",")

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

matplotlib.pyplot.ylabel("Difference in average")
matplotlib.pyplot.plot(numpy.mean(data0, axis=0) - numpy.mean(data1, axis=0))

fig.tight_layout()
matplotlib.pyplot.show()
```
