friends_names = []

new_friends = ""

while new_friends != "end":

    new_friends = input("Type the name of a friend: ")
    if new_friends != "end":
        friends_names.append(new_friends)

print()
print("Your friends are:")
  
for friend_name in friends_names:
    print(friend_name)
    