# with open("text.txt", "r") as learn:
#     content = learn.read()
#     print(content)

# with open("text.txt", "w") as f:
#     f.write("My name is RY, I am great in everything I do. I am true to myself and my growth. Everything works out for my good.Challenges are just learning phases for me. All is well with me because God is the greatest. God is with me")

# with open("text.txt", "a") as baby:
#     baby.write("\n HEAR ME AND HEAR ME WELL.")

# with open("text.txt", "r") as booboo:
#     content = booboo.read()
#     print(content)

#Write (w) creates a new file for you
# X does the same but it checks if a file with same name exists or not

# with open ("data.csv", "r") as f:
#     c = f.read()
#     print(c)

# with open("data.csv", "a") as D:
#     D.write("\nOla,50,Delta")

# with open("data.csv", "r") as babeO:
#     c = babeO.read()
#     print(c)


### HOW TO USE NUMPY TO READ A FILE


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
