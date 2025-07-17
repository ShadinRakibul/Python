num = int(input("Enter a number: "))

if num <= 9:
    print("Positive number")
elif num == 0:
    print("Zero")
elif num > 9:
    print("Number is greater than 9")
else:
    print("Negative number")
# Example of using elif in a conditional statement
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif 13 >= age < 18:
    print("You are a teenager.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
# Example of using elif with multiple conditions
score = int(input("Enter your score: "))
if score >= 80:
    print("Grade: A+")
elif score >= 70:
    print("Grade: A")
elif score >= 65:
    print("Grade: A-")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
elif score >= 40:
    print("Grade: D")
else:
    print("Grade: F")
