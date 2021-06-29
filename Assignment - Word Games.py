print('\nPlease enter the following:\n')

# Asking for the information that the story need.

adjective = input("Adjetive: ")
animal = input("Animal: ")
verb = input("Verb: ")
exclamation = input("Exclamation: ")
verb = input("Verb: ")
verb = input("Verb: ")

# Printing out the story.

print('\nYour story is: ')

print(f'\nThe other day, I was really in trouble. It all started when'
f'I saw a very \n{adjective.lower()} {animal.lower()} {verb.lower()} down the' 
f'hallway. "{exclamation.capitalize()}!" I yelled. But all \nI could think to' 
f'do was to {verb.lower()} over and over. Miraculously, \nthat caused it to stop,' 
f'but not before it tried to {verb.lower()} \nright in front of my family.\n')

# It is used to keep the program open until I press enter.

input()
