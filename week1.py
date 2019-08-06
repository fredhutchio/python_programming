#!/usr/bin/env python3

#### Intermediate Python: Programming ####

#### Before class ####

# share URL to hack.md
# check software installation

#### Welcome ####

# instructor introduction
# overview of fredhutch.io
# overview course philosophy, how to stay engaged
# pre-requisites: intro to Python (basic syntax including variables and functions, importing data, data types and structures, subsetting data)
# learner introductions and motivation
# sign in
# course objectives: create fully documented and automated workflows to perform data analysis tasks (loops, conditionals, functions, debugging)

#### Objectives ####

# Today:
#   review: loading data, assigning to variable, basic python syntax
#   numpy: arrays, subsetting, summary stats
#   plotting with matplotlib
#   working with mutliple files
#   for loops to repeat tasks

#### Review of pre-requisites and loading data ####

# load library
import os
import urllib.request
import zipfile
import numpy as np

# download data
urllib.request.urlretrieve("http://swcarpentry.github.io/python-novice-inflammation/data/python-novice-inflammation-data.zip", "python-novice-inflammation-data.zip")
# unzip data
zipData = zipfile.ZipFile("python-novice-inflammation-data.zip")
zipData.extractall()

# assign data to variable (so we can recall it later)
data = np.loadtxt(fname="data/inflammation-01.csv", delimiter=",")

# what is in the variable?
print(data)
# what type of thing is data?
print(type(data))
type(data) # shortcut allowed because of this interpreter
# what type of data is contained within the array?
print(data.dtype)
data.dtype
# show shape of data
data.shape
# output is rows, columns; rows are the individual patients, and the columns are their daily inflammation measurements
# arrays have members, or attributes, which use the dot nomenclature because they have the same part-and-whole relationship

## Challenge: import small-01.csv and determine if the type or shape of data differ from data object
small_data = np.loadtxt(fname="data/small-01.csv", delimiter=",")
print(small_data.shape)
print(small_data.dtype)
type(small_data)

#### Manipulating arrays ####
# extract or reference first element in array
data[0, 0] # row index, column index; python index starts at 0
# extract middle value
data[30, 20]
print("middle value in the data:", data[30, 20]) # include in prettier print statement

# slicing data
data[0:4, 0:10] # end bounds not inclusive
data[:3, 36:] # empty values mean beginning or end

# perform math on an entire array
doubledata = data * 2.0
doubledata[0:4, 0:10]
data[0:4, 0:10] # compare with original

# add arrays together
tripledata = doubledata + data
tripledata[0:4, 0:10]

# perform summaries across entire array
print(np.mean(data))

## Challenge: find max, min, standard deviation across the entire array data, and print with meaningful print statements
print("maximum:", np.max(data))
print("minimum:", np.min(data))
print("standard deviation:", np.std(data))

# multiple assignment: assign multiple variables at a once
maxval, minval, stdval = np.max(data), np.min(data), np.std(data)
print(stdval)

# print max inflammation for one patient
print('maximum inflammation for patient 2:', np.max(data[2, :]))

# calculate max inflammation for each patient over all days or all patients
# average inflammation for each day over all patients (0 means rows)
np.mean(data, axis=0)
# check shape of output
print(np.mean(data, axis=0).shape) # 40 values, this is number of days
# average inflammation for each patient over all days: axis = 1
print(np.mean(data, axis=1))

#### Visualizing data ####

import matplotlib.pyplot as plt
%matplotlib inline # for notebooks
image = plt.imshow(data) # im is image, 2D raster
plt.show() # not always needed; shortcut allowed because of interface/interpreter
plt.imshow(data) # another shortcut!

# plot inflammation over time as average across all patients
ave_inflammation = np.mean(data, axis=0)
plt.plot(ave_inflammation)

## Challenge: using one line of code, print the maximum inflammation across all patients
plt.plot(np.max(data, axis=0))

#### Repeating actions with loops ####

# what if we wanted to repeat plotting across all data files? how many lines of code would it take given the methods used so far?

# there are multiple ways to show what is contained in a variable
# create a variable for a word
word = "hutchinson"
word
word[0]
word[7]
# what if we change word?
word = "hutch"
word[0]
#word[7] # index error: there is no index 7 in word now!

# for loop: accesses items in a set
for char in word: # need to execute on top line of for loop in some interpreters!
    print(char) # have to include print statement for values to appear!
# repeats action AND is not length dependent

# importing multiple data files
import glob

glob.glob("data/inflammation*.csv")

# create a list of files (* is a wildcard)
filenames = sorted(glob.glob("data/inflammation*.csv")) # sorted to make filenames appear in numerical order
filenames

# loop across all filenames
for f in filenames:
    print(f)

## Challenge: Are all 12 data files the same shape? (hint: write a for loop)
for f in filenames:
    data = np.loadtxt(fname = f, delimiter = ",")
    print("shape of", f, ":", data.shape) # more informative print statement

# plot average inflammation for each file in a separate plot
import numpy
import matplotlib

filenames = sorted(glob.glob("data/inflammation*.csv"))
for f in filenames:
    print(f)

    data = np.loadtxt(fname=f, delimiter=",")

    fig_ave = np.mean(data, axis=0)
    ave_plot = plt.plot(fig_ave)
    plt.show() # why is this necessary?

## Challenge: Add comments to explain the code in exercises/week1_example.py. Which data files are suspicious?
import glob
import numpy
import matplotlib.pyplot as plt

filenames = sorted(glob.glob("data/inflammation*.csv"))
filenames = filenames[0:3]
for f in filenames:
    print(f)

    data = np.loadtxt(fname=f, delimiter=",")

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel("average")
    axes1.plot(np.mean(data, axis=0))

    axes2.set_ylabel("max")
    axes2.plot(np.max(data, axis=0))

    axes3.set_ylabel("min")
    axes3.plot(np.min(data, axis=0))

    fig.tight_layout()
    plt.show()

## Challenge: Plot the difference between the average of the first dataset and the average of the second dataset, i.e., the difference between the leftmost plot of the first two figures.
import glob
import numpy
import matplotlib.pyplot as plt

filenames = sorted(glob.glob("data/inflammation*.csv"))

data0 = np.loadtxt(fname=filenames[0], delimiter=",")
data1 = np.loadtxt(fname=filenames[1], delimiter=",")

fig = plt.figure(figsize=(10.0, 3.0))

plt.ylabel("Difference in average")
plt.plot(np.mean(data0, axis=0) - np.mean(data1, axis=0))

fig.tight_layout()
plt.show()

#### Wrapping up ####

# make sure work is saved
# review how to get back into work
# review objectives
# preview next week"s objectives
# remind to sign in
