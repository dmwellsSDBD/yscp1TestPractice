# Collect some data from users

name = input("Please enter your first name: ")
age = int(input("Please enter your age: "))
city = input("Please enter your city: ")

user = {"name": name, "age": age, "city": city}
print(user)

for key in user:  # Loops through the keys
    print(key) 

print("Collect Keys and Values:")
for key, value in user.items():
    print(key, value)

print("Data Values: \n")
for value in user.values():
    print(value) 


grades = {
    'Hannah': 90, 
    'Gavin': 45, 
    'Cameron': 87, 
    'Hunter': 91, 
    'Eva': 73, 
    'Connor': 2, 
    'Christian': 98
}

for student, grade in grades.items():
    print(f'{student}: {grade}')