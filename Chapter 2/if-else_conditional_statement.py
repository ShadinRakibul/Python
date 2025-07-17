a=int(input("Enter Your Age:"))
print("Your Age is:", a)
#conditional operators
# <,><=,>,>=,==,!=
print(a > 18)  # greater than
print(a < 18)  # less than
print(a >= 18)  # greater than or equal to
print(a <= 18)  # less than or equal to
print(a == 18)  # equal to
print(a != 18)  # not equal to
print(a > 18 and a < 30)  # logical AND
print(a > 18 or a < 30)  # logical OR
print(a != 18 and a < 30)  # logical NOT
print(a == 18 or a < 30)  # logical OR with equality check
print(a != 18 or a < 30)  # logical OR with inequality check
print(a == 18 and a < 30)  # logical AND with equality check
print(a != 18 and a < 30)  # logical AND with inequality check
print(a == 18 or a > 30)  # logical OR with equality and greater than check
print(a != 18 or a > 30)  # logical OR with inequality and greater
# than check
print(a == 18 and a > 30)  # logical AND with equality and greater
# than check
print(a != 18 and a > 30)  # logical AND with inequality and greater
# than check
print(a == 18 or a < 30 and a > 20)  # logical
# OR with equality and AND conditions
print(a != 18 or a < 30 and a > 20)  # logical
# OR with inequality and AND conditions.
if a>18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    