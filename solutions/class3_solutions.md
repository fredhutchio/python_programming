# Intermediate Python: Programming
# Class 3 Exercises

#### Challenge-errors

Using the error message included below the code,
identify the type of error and why it is occurring.

*Code:*
```
def print_message(day):
    messages = {
        "monday": "Hello, world!",
        "tuesday": "Today is tuesday!",
        "wednesday": "It is the middle of the week.",
        "thursday": "Today is Donnerstag in German!",
        "friday": "Last day of the week!",
        "saturday": "Hooray for the weekend!",
        "sunday": "Aw, the weekend is almost over."
    }
    print(messages[day])

def print_friday_message():
    print_message("Friday")

print_friday_message()
```
*Error:*
```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-33-ce8c0be5fdfb> in <module>()
     14     print_message("Friday")
     15
---> 16 print_friday_message()

<ipython-input-33-ce8c0be5fdfb> in print_friday_message()
     12
     13 def print_friday_message():
---> 14     print_message("Friday")
     15
     16 print_friday_message()

<ipython-input-33-ce8c0be5fdfb> in print_message(day)
      9         "sunday": "Aw, the weekend is almost over."
     10     }
---> 11     print(messages[day])
     12
     13 def print_friday_message():

KeyError: 'Friday'
```

#### Challenge-docstring

In our last class, we created a function for temperature conversion.
Add a docstring to document the code:
```
def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))
```

#### Challenge-parameters

What does the following code display when run, and why?

```
def numbers(one, two=2, three, four=4):
    n = str(one) + str(two) + str(three) + str(four)
    return n

print(numbers(1, three=3))
```

*`one` must be defined as an input since it does not have a default value*

#### Challenge-parameters2

What does the following code display when run, and why?

```
def func(a, b=3, c=6):
    print('a: ', a, 'b: ', b, 'c:', c)

func(-1, 2)
```

*Output includes:*
```
a: -1 b: 2 c: 6
```

#### Challenge-pre-post

Suppose you are writing a function called `average` that calculates the average of the numbers in a list. What pre-conditions and post-conditions would you write for it?

```
# a possible pre-condition:
assert len(input_list) > 0, 'List length must be non-zero'
# a possible post-condition:
assert numpy.min(input_list) <= average <= numpy.max(input_list),
'Average should be between min and max of input values (inclusive)'
```
