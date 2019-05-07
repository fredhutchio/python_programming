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
import numpy

# download data
urllib.request.urlretrieve("http://swcarpentry.github.io/python-novice-inflammation/data/python-novice-inflammation-data.zip", "python-novice-inflammation-data.zip")
# unzip data
zipData = zipfile.ZipFile('python-novice-inflammation-data.zip')
zipData.extractall()

# assign data to variable (so we can recall it later)
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

# show the variable's value
print(data)
# what type of thing is data?
print(type(data))
# find type of data contained within array (data)
print(data.dtype)
# show shape of data
print(data.shape)
# output is rows, columns; rows are the individual patients, and the columns are their daily inflammation measurements
# arrays have members, or attributes, which use the dot nomenclature because they have the same part-and-whole relationship

#### Manipulating arrays ####

#### Visualizing data ####

#### Repeating actions with loops ####

#### Wrapping up ####

# make sure work is saved
# review how to get back into work
# review objectives
# preview next week's objectives
# remind to sign in
