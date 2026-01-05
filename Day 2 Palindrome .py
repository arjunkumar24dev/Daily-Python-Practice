# Write a Python program to check whether a given number is a palindrome

num = input("Enter the number:")
# Reverse number
reverse_num = num[::-1]

if num == reverse_num:
  print("The number is a Palindrome")
else:
  print("The number is Not a Palindrome")
