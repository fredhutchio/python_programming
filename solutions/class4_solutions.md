# Intermediate Python: Programming
# Class 4 Exercises

#### Challenge-debug

The following code computes the Body Mass Index (BMI) of patients.
BMI is calculated as weight in kilograms divided by the square of height in metres.
The test results indicate all patients appear to have have unusual and identical BMIs,
despite having different physiques.
What suggestions do you have to improve this code?

```python
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patients[0]
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is: %f" % bmi)
```

#### Challenge-range_overlap

Try to resolve the error in `range_overlap`.
Rerun your test after each change you make.
What other errors do you receive?
How could you resolve them?

def range_overlap(ranges):
    '''Return common overlap among a set of [left, right] ranges.'''
    if not ranges: # LAST ASSERTION: no ranges
        return None
    max_left, min_right = ranges[0] # THIRD ASSERTION: initialize with data
    for (left, right) in ranges:
        max_left = max(max_left, left)
        min_right = min(min_right, right)
    if max_left >= min_right:  # FIRST ASSERTION: no overlap
        return None
    return (max_left, min_right)
