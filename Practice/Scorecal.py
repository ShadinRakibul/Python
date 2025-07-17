name=str(input("Enter your name: "))
print(len(name))# length of the string) 
print("Hello, " + name + "! Welcome to the program.")
age=int(input("Enter your age: "))
print("Your age is:", age)

if age >= 18:
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are an adult.")      
        
    print("You are eligible to vote.")
elif age < 18:
    print("You are not eligible to vote yet.")
    if age < 13:
        print("You are a child.")

Score = int(input("Enter your score: "))
if Score >= 80:
    print("Grade: A+")
elif Score >= 70:
    print("Grade: A")
elif Score >= 65:
    print("Grade: A-")  
elif Score >= 60:
    print("Grade: B")   
elif Score >= 50:
    print("Grade: C")
elif Score >= 40:
    print("Grade: D")
else:
    print("Grade: F")

print("Thank you for using the program, " + name + "!")  # farewell message
print("Have a great day ahead!")  # additional message
print("This program demonstrates nested if conditions and user input handling.")
print("You can modify the code to add more features or change the logic as needed.")
