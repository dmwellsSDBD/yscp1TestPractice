print("\nPython Dictionaries")

myDict = {'name': 'David', 'age': 51, 'city': 'Norwood'}

print('My name is: ', myDict['name'])

print('\nAdding/Updating Items in a Dictionary\n')

myDict['country'] = 'USA' # adding a key/value pair

print(myDict)

myDict['age'] = 52

print(myDict)

print('\nRemove Items from a dictionary')

del myDict['country']

print(myDict)

print('\nDelete an item from the Dictionary, and return it\'s value')

rem_value = myDict.pop('age')

print(rem_value)
print(myDict)

print("\nA New Dictionary\n")

dictionary2 = {'fruits': ['apple', 'banana', 'orange'], 'vegetables': ['broccoli', 'brussel sprouts', 'carrots']}

# add another fruit:
dictionary2['fruits'].append('cherry')

#print the dictionary
print(dictionary2)

print(dictionary2['fruits'])
