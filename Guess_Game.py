import random

game = "y"

while game.lower() == "y":
    magic_number = random.randint(1,100)
    
    guess = -1
    guess_count = 0

    while guess != magic_number:

        guess = input("\nwhat is your guess? ")
        
        if guess.isdigit():
            guess = int(guess)
            guess_count += 1
        
            if guess > magic_number:
                print("\nLower")

            elif guess < magic_number:  
                print("\nHigher")
            
            else:
                print("\nYou guessed it! ")
        else:
            print("\nDebe digitar un valor numerico. Intenta de nuevo. ")
        
    print(f"\nIt took you {guess_count} guesses. ")

    game = input("\nDo you want to play again (Y / N)?  ")

print ("\nThanks for playing! ")