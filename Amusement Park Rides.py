
ride = False

age_rider_1 = int(input("\nWhat is the age of the first rider? "))
height_rider_1 = int(input("\nWhat is the height of the first rider? "))   

if age_rider_1 >= 12 and age_rider_1 < 18:
    golden_ticket1 = input("\nDoes this rider have a golden passport (yes/no)? ")

options = input("\nIs there a second rider? (Yes / No) : ")

if options.lower() .strip() == "yes":

    age_rider_2 = int(input("\nWhat is the age of the first rider? "))
    height_rider_2 = int(input("\nWhat is the height of the first rider? "))

    if age_rider_2 >= 12 and age_rider_2 < 18:
        golden_ticket2 = input("\nDoes this rider have a golden passport (yes/no)? ")

    if height_rider_1 < 36 or height_rider_2 < 36:

        ride = False
    else:
        
        if age_rider_1 >= 18 or age_rider_2 >= 18 or golden_ticket1.lowes() == "yes" or golden_ticket2.lowes() == "yes":

            ride = True

        else:

            if age_rider_1 >= 18 and height_rider_1 >= 62:
        
                ride = True

            elif age_rider_1 >= 12 and age_rider_2 >= 12 and height_rider_1 >= 52 and height_rider_2 >= 52:

                ride = True
    
            else:
       
                ride = False

    if (age_rider_1 >= 16 and age_rider_2 >= 14) or (age_rider_1 >= 14 and age_rider_1 >= 16):

            ride = True

    else:

            ride = False


else:   

        if (age_rider_1 >= 18 or golden_ticket1.lower() == "yes") and height_rider_1 >= 62:
        
            ride = True
    
        else:
       
            ride = False


if ride:

    print("\nWelcome to the ride. Please be safe and have fun! \n")

    input()

else:

    print("\nSorry, you may not ride. \n")

    input()