def function(x = 3, y = 4):
    print(x);
    print(y);
    return x + y
z = function(9, 10)
print(z)
# The syntax in python is loose, you can omit the arguments when calling a function.
z = function()
print(z)