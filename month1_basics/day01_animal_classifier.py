# Day 1 : Animal kingdom Classifier

animal = input("Enter an animal name:").lower()

if animal == "human" or animal == "ape":
  print("category : Mammal")
elif animal == "eagle" or animal == "parrot":
  print("Category: Bird")
elif animal == "shark" or animal == "salmon":
  print("Category: Fish")
else:
  print("Category: other species")
