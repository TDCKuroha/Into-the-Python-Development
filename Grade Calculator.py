grade = int(input("\nWhat is your grade percent? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

sign = ""
 
last_digit = grade % 10

if last_digit >= 7:
    sign = "+"

elif last_digit < 3:
    sign = "-"

else:
    sign = ""

if letter == "F":
    sign = ""

print(f"\nYour letter grade is: {letter}{sign}")

if grade >= 70:
    print("\nCongratulations! You passed the class!")
else:
    print("\nStay focused and you'll get it next time!")



print('\nPress "ENTER" to exit.  ')
input()

    