myself = 'Shadin'
friend = 'Sumon'
another_friend = 'Rifat'
print(f"{myself} is a good friend of {friend} and {another_friend}.")

# triple quotes for multi-line strings
apple = '''Sumon is a good friend of Shadin and Rifat 
also he is a good person
and a good student.
He is a good programmer.'''
print(apple)

# Looping through each character in a string
for character in myself:
    print(character)

# indexing and slicing strings
print(myself[0])
print(myself[1:4])  # slicing
print(myself[1:])   # slicing
print(myself[:4])   # slicing
print(myself[-1])  # last character
print(myself[-2])  # second last character
print(myself[-3:])  # last three characters
print(myself[-3:-1])  # slicing with negative indices
print(myself[-4:-1])  # slicing with negative indices
print(myself[-4:])  # slicing with negative indices
print(myself[0:4])  # slicing
print(myself[0:4:2])  # slicing with step
