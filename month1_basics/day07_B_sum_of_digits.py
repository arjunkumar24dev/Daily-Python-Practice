# Day 7(B) : Sum of Digits

num = int(input("Enter a number: "))
total = 0

while num > 0 :
  total += num % 10
  num //= 10

print("Sum of Digits:", total)
