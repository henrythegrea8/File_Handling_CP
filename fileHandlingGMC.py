import numpy as np

# data = np.genfromtxt("data.csv", dtype=None, delimiter=",", filling_values=0)

# print(data)

with open("loan.csv", "r") as f:
    data =f.read()
   
data = np.genfromtxt("loan.csv", delimiter=",", usecols=8, filling_values = 0)

### Creat a 1D array
array = np.array(data)
print(array)

### Calculate the mean of the array
mean = np.mean(array)
median = np.median(array)
standard_deviation = np.std(array)
maximum = np.max(array)
minimum = np.min(array)
variance = np.var(array)


print(f"The mean is: {mean}")
print(f"The median is: {median}")
print(f"The standard deviation is: {standard_deviation}")
print(f"The Maximum is: {maximum}")
print(f"The Minimum is: {minimum}")
print(f"The variance is: {variance}")
