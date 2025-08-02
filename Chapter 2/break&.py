for i in range(1,101,1):
    print(i, end=" ")
    if(i==20):
        print("Loop break.")  # When the loop reaches 50, it prints "Loop break." and breaks out of the loop.
        break
    
    print()  # This will print a newline after each number.
    
# This code uses a for loop to iterate through numbers from 1 to 100 in steps of 10.
# When the loop reaches 50, it skips the print statement for that iteration and continues with the next iteration.
# The continue statement allows the loop to skip the current iteration and proceed to the next one.
# The print statement will not execute for the value 50, but will execute for all other values in the range.
# The output will show the current number for each iteration except when it is 50.
# The loop will print "Current number: 50" for all other numbers in the range. 