# You are allowed to use both single or double quotes to enclose a string.
string = 'Hello World'
print(string)
# Redefinition is ok.
string = "Goodbye Past"
print(string)
# \ is used as escaping character.
string = "{\"name\" : \"Chen\"}"
print(string)
# r means to print the raw string including the escaping characters.
print(r'\home\chen\Desktop')
# + is for concatenation.
string = 'Hello World' + " Goodbye Past"
print(string)
# * number means duplication
string = "Hello World " * 5
print(string)
# Slice String
string = "Elsa"
print(string[0])
# Print out the last character.
print(string[-1])
# len() is the function to get the length.
print(string[len(string) - 1])
# Get the sub-string just like what java does.
print(string[1:2])
# Anologous to string.substring(0, 2) in java.
print(string[:2])
# Anologous to string.substring(2) in java.
print(string[2:])
# Get the length of a string
print(len(string))
