import math

user_choise = int(input("How many columns and rows do you want in your multiplication table? ")) 

max_number = user_choise * user_choise

range_size = user_choise + 1

#digits = int(math.log10(max_number)) + 1

digits = len(str(max_number)) + 1

for row_number in range (1,range_size):
    
    for column_number in range (1,range_size):

        number = row_number * column_number

        print(f"{number:{digits}}", end=" ")
    
    print()

input() 
