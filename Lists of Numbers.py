number_list = []

numbers = -1

print("Enter a list of numbers, type 0 when finished. ")

while numbers != 0:
    numbers = int(input("Enter number: "))
    if numbers !=0:
        number_list.append(numbers)

sum = 0

for number in number_list:
    sum += number

print(f"The sum is: {sum}")

count = len(number_list)
average = sum / count

print(f"The average is: {average}")

largest_number = -1

for number in number_list:
    if number > largest_number:
        largest_number = number

print(f"The largest number is: {largest_number}")

smallest_number = 99999999999

for number in number_list:
    if number > 0 and number < smallest_number:
        smallest_number = number

print(f"The smallest number is: {smallest_number}")

sorted_list = sorted(number_list)

print("The sorted list is:")
for number in sorted_list:
    print(number)