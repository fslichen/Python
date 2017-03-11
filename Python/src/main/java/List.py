# A list can contain numbers.
list = [23, 45, 90]
print(list)
# A list can also contain strings.
list = ['Hello', 'World']
print(list)
# A list can be contatenated.
list = [34, 23, 90]
list += [45, 23]
print(list)
# A list can also be appended. Only one element is allowed in the append function.
list = [23]
list.append(45)
print(list)
# A list can also be sliced
list = [34, 28, 15, 43]
print(list[1:2])
print(list[:2])
print(list[2:])
print(list[:])