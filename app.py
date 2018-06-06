#comments are skipped by the interpreter

#simple calculator program

numberOne = int(input("Please insert number 1: "))
numberTwo = int(input("Please insert number 2: "))

print(f"the sum of the two numbers in {numberOne + numberTwo}")

print(f"the product of the two numbers in {numberOne * numberTwo}")

print(f"the subtraction of the two numbers in {numberOne - numberTwo}")

print(f"the division / of the two numbers in {numberOne / numberTwo}")

print(f"the division // of the two numbers in {numberOne // numberTwo}")

#parentheses (()) can be used for grouping incase of complex calculations

print(f"the remainder from dividing two numbers % {numberOne % numberTwo}")

#it is possible to use the ** operator to calculate powers [1]:

#If a variable is not “defined” (assigned a value), trying to use it will give you an error:

#print(n)

#rounding off numbers using round() function

print(round(7.1234, 2))