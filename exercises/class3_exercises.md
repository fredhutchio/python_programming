# Intermediate Python: Programming
# Class 3 Exercises

## Example 1
```
def s(p):
    a=0
    for v in p:
        a+=v
    m=a/len(p)
    d=0
    for v in p:
        d+=(v-m)*(v-m)
    return numpy.sqrt(d/(len(p)-1))
```

## Example 2
```
def std_dev(sample):
    sample_sum = 0
    for value in sample:
        sample_sum += value

    sample_mean = sample_sum / len(sample)

    sum_squared_devs = 0
    for value in sample:
        sum_squared_devs += (value - sample_mean) * (value - sample_mean)

    return numpy.sqrt(sum_squared_devs / (len(sample) - 1))
```
