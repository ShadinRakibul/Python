# Read the correct tea type
T = int(input("Enter correct tea type: "))

# Read the answers of the five contestants
answers = list(map(int, input("Enter guesses of 5 contestants: ").split()))

# Count how many guessed correctly
correct_count = answers.count(T)

# Output the result
print("Correct guesses:", correct_count)
