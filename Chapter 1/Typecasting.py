print("This is the Typecasting script in Chapter 1.")
# Typecasting is the process of converting one data type to another. 

a='1'
# a=1
b='2'
# b=2
print(int(a)+int(b))

# Typecasting examples

#Explicit typecasting where programmer manually convert data types
string='15'
number=7
string_number=int(string)
sum=number+string_number
print("Sum of", number, "and", string_number, "is:", sum)

# Implicit typecasting where Python automatically converts data types
print(7.5 + 2)  # float + int = float
print(3 + 4.0)  # int + float = float
print(2 + 3j)  # int + complex = complex
print(3.5 + 2j)  # float + complex = complex    


fruits_list = ['apple', 'banana', 'cherry', [-8.20], 3.14, True]
print("List:", fruits_list)
colors_tuple = ('red', 'green', 'blue', 42, 3.14, False)
print("Tuple:", colors_tuple)





