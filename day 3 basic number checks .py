# Day 3: Basic Number Checks 
#---------------------------------------------
# Program 1: Check if a number is even or odd
# Program 2: Check number type


# Program 1: Check if a number is even or odd 
num = int(input("Enter a number: "))

if num % 2 == 0:
  print("Even number")
else:
  print("Odd number")

#----------------------------------------------

# Program 2: Check number types 
num = int(input("Enter a number: "))

if num > 0:
  print("Positive")
elif num < 0:
  print("Negative")
else:
  print("Zero")
