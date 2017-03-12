def function(x = 3, y = 4):
    print(x);
    print(y);
    return x + y
z = function(9, 10)
print(z)
# The syntax in python is loose, you can omit the arguments when calling a function.
z = function()
print(z)
# If you are providing a part of the arguments, don't forget to give the argument names. 
z = function(y = 5)
print(z)
# A function can take various arguments.
def function(*xs):
    sum = 0
    for x in xs:
        sum += x
    return sum
sum = function(3, 4, 5, 6, 7)
print(sum)
# Variables Unpacking
def function(x, y, z):
    return x + y + z
array = [1, 2, 3]
print(function(*array))

