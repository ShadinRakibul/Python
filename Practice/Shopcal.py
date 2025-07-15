sum = 0
while(True):
    userInput = input("Enter the item price or press q to quit: \n")
    
    if userInput != 'q':
        sum = sum + int(userInput)
        print(f"Your total so far: {sum}")
        print("Last item added to your bill is: " + userInput)
    
    else:
        print(f"Your total bill is {sum}. Thanks for shopping with us")
        break


