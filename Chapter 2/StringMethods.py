# strings are immutable
myself = 'Shadin'
print(len(myself))  # length of the string
print(myself.upper())  # convert to uppercase
print(myself.lower())  # convert to lowercase
print(myself[0])  # first character
print(myself[1:4])  # slicing from index 1 to 3
print(myself[1:])  # slicing from index 1 to end
print(myself[:4])  # slicing from start to index 3
print(myself[-1])  # last character
print(myself[-2])  # second last character
print(myself[-3:])  # last three characters
print(myself[-3:-1])  # slicing with negative indices
print(myself[-4:-1])  # slicing with negative indices
print(myself[-4:])  # slicing with negative indices
print(myself[0:4])  # slicing from start to index 3
print(myself[0:4:2])  # slicing with step of 2
print(myself.rstrip())  # remove trailing spaces
print(myself.lstrip())  # remove leading spaces
print(myself.strip())  # remove leading and trailing spaces
print(myself.replace('Shadin', 'Rakibul'))  # replace 'Shadin' with 'Rakibul
print(myself.find('a'))  # find the first occurrence of 'a
print(myself.index('a'))  # index of the first occurrence of 'a
print(myself.count('a'))  # count occurrences of 'a
print(myself.startswith('S'))  # check if starts with 'S'
print(myself.endswith('n'))  # check if ends with 'n'
print(myself.split('a'))  # split the string by 'a'
print(myself.split())  # split the string by whitespace
print(myself.isalpha())  # check if all characters are alphabetic   
print(myself.isdigit())  # check if all characters are digits
print(myself.isalnum())  # check if all characters are alphanumeric
print(myself.islower())  # check if all characters are lowercase
print(myself.isupper())  # check if all characters are uppercase
print(myself.capitalize())  # capitalize the first character
print(myself.title())  # capitalize the first character of each word
print(myself.swapcase())  # swap case of all characters
print(myself.center(20, '*'))  # center the string with '*' padding
print(myself.zfill(10))  # pad the string with zeros to a width of

# 10 characters
print(myself.expandtabs(4))  # expand tabs to 4 spaces
print(myself.startswith('Sha'))  # check if starts with 'Sha'   
print(myself.endswith('din'))  # check if ends with 'din'
print(myself.partition('a'))  # partition the string at 'a' 
print(myself.rpartition('a'))  # partition the string at 'a' from the right
print(myself.splitlines())  # split the string into lines
print(myself.join(['Hello', 'World']))  # join a list of strings with 'myself' as the separator
print(myself.casefold())  # casefold the string for case-insensitive comparisons


# string concatenation
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
print(myself[0])  # first character

print(myself[1:4])  # slicing from index 1 to 3
print(myself[1:])  # slicing from index 1 to end
print(myself[:4])  # slicing from start to index 3
print(myself[-1])  # last character
print(myself[-2])  # second last character