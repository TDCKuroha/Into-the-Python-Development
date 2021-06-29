first = int(input("\nWhat is the first number? "))
second = int(input("What is the second number? "))

if first > second:
    print("The first number is greater")  
if second > first:
    print("The first number is not greater")  
if first != second:
    print("The numbers are not equal")  
if first == second:
    print("The numbers are equal")  
if second < first:
    print("The second number is not greater") 
if first < second:
    print("The second number is greater") 



animal = input("\nWhat is your favorite animal? ")

if animal.lower() == 'bear':
    print("That's my favorite animal too!") 
else:
    print("That's not my favorite animal too!\n") 

input()