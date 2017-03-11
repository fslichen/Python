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
# The Break Statement
for i in range(0, 10):
    if i % 2 == 0:
        print(i, 'is an even number.')
        break;
# The Continue Statement
for i in range(0, 10):
    if i % 2 == 0:
        print(i, 'is an even number.')
        continue;
    print(i, 'is an odd number')
