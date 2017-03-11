# Entire Loop
strings = ['Apple', 'Pear', 'Orange']
for string in strings:
    print(string)
    print(len(string))
# Partial Loop
strings = ['Apple', 'Pear', 'Orange', 'Cucumber', 'Banana', 'Tomato', 'Potato']
for string in strings[1 : 3]:
    print(string)
# range(n) function ranges from 0 to n - 1.
for i in range(10):
    print(i)
# range(m, n) ranges from m to n - 1.
for i in range(5, 10):
    print(i)
# Define the increment size as 2. 
for i in range(5, 10, 2):
    print(i)
