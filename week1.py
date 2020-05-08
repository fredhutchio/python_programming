#!/usr/bin/env python3

#### Intermediate Python: Programming ####

#### Before class ####

# share URL to hack.md
# check software installation

#### Welcome ####

# instructor introduction
# sign in using link on HackMD page
# overview of fredhutch.io
# overview course philosophy
#   designed for researchers who have some experience with Python but would like to improve robustness of code
#   follow along with coding activities, try the challenges
# pre-requisites: intro to Python (basic syntax including variables and functions, importing data, data types and structures, subsetting data)
# learner introductions and motivation
# course objectives: create fully documented and automated workflows to perform data analysis tasks (loops, conditionals, functions, debugging)

#### Objectives ####

# Today:
#   review: loading data, assigning to variable, basic python syntax
#   numpy: arrays, subsetting, summary stats
#   plotting with matplotlib
#   working with mutliple files
#   for loops to repeat tasks

#### Getting set up ####

# an overview of IDEs
#   there are advantages and disadvantages to each programming approach
#   Jupyter notebooks are sufficient for this course
#   other types of interfaces are available: Atom + Hydrogen, VS Code, Spyder, etc
#   instructor will use Atom because it splits the difference between a notebook and other interfaces
#   notebooks may be insufficient for some practices
#   python scripts are an alternative way to document code
#   can export scripts as notebooks, and notebooks to scripts
# using Atom
#   can be used for other programming languages (text editor)
#   need to have python previous installed
#   requires Hydrogen to interact with Python

# set up project
#   create new directory to hold class materials
#   create new script, week1.py (or notebook, as case may be)
#   .py suffix is required for Atom to interpret as python code
#   use shift + control + p then type hydrogen for help using interface
#   execute code by holding down shift and pressing enter

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
data.dtype
# show shape of data
data.shape
# output is rows, columns; rows are the individual patients, and the columns are their daily inflammation measurements
# arrays have members, or attributes, which use the dot nomenclature because they have the same part-and-whole relationship

## Challenge: import small-01.csv and determine if the type or shape of data differ from data object
small_data = np.loadtxt(fname="data/small-01.csv", delimiter=",")
small_data.shape
small_data.dtype
type(small_data)

#### Manipulating arrays ####
# extract or reference first element in array
data[0, 0] # row index, column index; python index starts at 0
# extract middle value
data[30, 20]
print("middle value in the data:", data[30, 20]) # include in prettier print statement

# slicing data
data[0:4, 0:10] # end bounds not inclusive
# empty values mean beginning or end of data

# perform math on an entire array
doubledata = data * 2.0
doubledata[0:4, 0:10]
# compare with original

# add arrays together
tripledata = doubledata + data
tripledata[0:4, 0:10]

# perform summaries across entire array
np.mean(data)

## Challenge: find max, min, standard deviation across the entire array data, and print with meaningful print statements
print("maximum:", np.max(data))
print("minimum:", np.min(data))
print("standard deviation:", np.std(data))

# multiple assignment: assign multiple variables at a once
maxval, minval, stdval = np.max(data), np.min(data), np.std(data)
stdval

# print max inflammation for one patient
np.max(data[2, :])

# calculate max inflammation for each patient over all days or all patients
# average inflammation for each day over all patients (0 means rows)
np.mean(data, axis=0)
# check shape of output
np.mean(data, axis=0).shape # 40 values, this is number of days
# average inflammation for each patient over all days: axis = 1
np.mean(data, axis=1)

#### Visualizing data ####

# load package
import matplotlib.pyplot as plt

# for notebooks (sometimes)
%matplotlib inline
# % is an iPython magic function, only valid in notebooks

# create heatmap pf data (blue is low value, yellow is high)
plt.imshow(data) # im is image, this is shortcut allowed by interfaces

# plot inflammation over time as average across all patients
ave_inflammation = np.mean(data, axis=0)
plt.plot(ave_inflammation)

## Challenge: plot the maximum and minimum inflammation across all patients
plt.plot(np.max(data, axis=0))
plt.plot(np.min(data, axis=0))

#### Grouping plots ####

# we can plot multiple figures in the same plot as subplots/panels

## Challenge: Add comments to explain the code in exercises/week1_example1.py
# share link to GitHub in HackMD
# will need to select entire chunk to get plots to appear

# load libraries
import numpy as np
import matplotlib.pyplot as plt

# import data
data = np.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

# create space in which to place plot
fig = plt.figure(figsize=(10.0, 3.0))

# place each subplot: total rows of subplots, total columns of subplots, which subplot is this (left-to-right, top-to-bottom)
axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

# title axes for each subplot
axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(np.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0))

# spread out graphs more (can serve to show plot as well in some interfaces)
fig.tight_layout()

# show plot (not necessary in some interfaces)
plt.show()

#### Repeating actions with loops ####

# what if we wanted to repeat plotting across all data files? how many lines of code would it take given the methods used so far?

# for loop: accesses items in a set
word = "alligator"
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
filenames = sorted(glob.glob("data/inflammation*.csv"))
for f in filenames:
    print(f)

    data = np.loadtxt(fname=f, delimiter=",")

    fig_ave = np.mean(data, axis=0)
    ave_plot = plt.plot(fig_ave)
    plt.show() # why is this necessary?

## Challenge: Add comments to explain the code in exercises/week1_example2.py. Which data files are suspicious?

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
