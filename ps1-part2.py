# Write a function that takes two variables and does all the computations asked

def number_fun(a, b):
    print (str(a), "+", str(b), "=", str(a + b))
    print (str(a), "*", str(b), "=", str(a * b))
    print (str(a), "**", str(b), "=", str(a ** b))
    print (str(a), "%", str(b), "=", str(a % b))

# Ask the user for the first number, store the value in a variable

firstnum = int(input("Enter an integer between 10 and 100: "))

# Ask the user for the second number, store the value in a variable

secondnum = int(input("Enter an integer less than 4: "))

# Repeat back the numbers

print ("You entered", str(firstnum), "and", str(secondnum))

# Perform calculations. Be careful about string formatting for autograders.

number_fun(firstnum, secondnum)
