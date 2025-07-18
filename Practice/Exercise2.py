a=int(input("Enter a time in hours:  "))
b=int(input("Enter a time in minutes:  "))

if a < 0 or b < 0:
    print("Invalid input. Time cannot be negative.")

if a<12:
    print("The time is in the morning.")
elif a < 18:
    print("The time is in the afternoon.")
elif a > 24:
    print("Good night.")


