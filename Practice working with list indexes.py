items = []
new_item = None

print("\nPlease enter the items of the shopping list (type: quit to finish): \n")
    
while new_item != "quit":
  
    new_item = input("Item: ")
    if new_item != "quit":
        items.append(new_item)
  
if new_item  == "quit":
    print("\nThe shopping list is: ")
    for item in items:
        print (item)
        
    print("\nThe shopping list with indexes is: ")
    for i in range(len(items)):
        item = items[i]
        print(f"{i}. {item}")

change_item = int(input("\nWhich item would you like to change?  "))   
new_name = input("What is the new item? ")      

items[change_item] = new_name

print("\nThe shopping list with indexes is: ")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")