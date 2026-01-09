# Day 5 : Find Factorial of a Number 

num = int(input("Enter the number:"))
fact = 1

for i in range (1, num+1):
  fact *= i

print( "Factorial of", num, "is:", fact)
          
