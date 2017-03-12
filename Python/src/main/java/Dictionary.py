# Dictionary in python is just like json.
json = {'name' : 'Chen', 'age' : 27, 'education' : {'college' : 'UIUC', 'degree' : 'master'}}
print(json)
print(json['name'])
print(json['education'])
for key, value in json.items():
    print(key, value)
