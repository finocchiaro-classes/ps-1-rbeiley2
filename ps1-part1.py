# Ask the user for the first number, store the value in a variable
number1 = int(input("Enter an integer between 10 and 100: "))

# Ask the user for the second number, store the value in a variable
number2 = int(input("Enter an integer less than 4: "))

# Repeat back the numbers
print ("You entered", str(number1), "and", str(number2))

# Perform calculations. Be careful about string formatting for autograders.
print (str(number1), "+", str(number2), "=", str(number1 + number2))
print (str(number1), "*", str(number2), "=", str(number1*number2))
print (str(number1), "**", str(number2), "=", str(number1**number2))
print (str(number1), "%", str(number2), "=", str(number1%number2))
