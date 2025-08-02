i=int(input("Enter a Value: "))
print(f"You entered: {i}")

while i<=10:
    i=int(input("Enter a Value: "))
    print(f"You entered: {i}")
  
print("Loop ended.")
# This code uses a while loop to repeatedly prompt the user for input until the value is greater than 10.
# The loop continues as long as the condition (i <= 10) is true.
# The user is prompted to enter a value, which is then printed.
count= 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
else:
    print("Countdown finished.")
# This code uses a while loop to count down from 5 to 1.    
# The loop continues as long as the condition (count > 0) is true.
# When the condition becomes false, the else block is executed, printing "Countdown finished."