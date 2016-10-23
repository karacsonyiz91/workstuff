# Calculator

import sys

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

print ("Hi this is a simple calculator. You can add,divide,subtract or multiply 2 numbers!")
print ("Please enter the first number(or letter to exit): ")
number1 = input()
if number1.isdigit():
	number1 = int(number1)
else:
	sys.exit()

print ("Please enter the operation: ")
operator = input()

print ("Please enter the second number (or letter to exit): ")
number2 = input()
if number2.isdigit():
	number2 = int(number2)
else:
	sys.exit()

if operator == "-":
	print(subtract(number1, number2))
elif operator == "+":
	print(add(number1, number2))
elif operator == "/":
	print(divide(number1, number2))
elif operator == "*":
	print(multiply(number1, number2))
else:
	print ("this is not an option")
	sys.exit()









