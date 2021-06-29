items = []
prices = []
new_item = ""
new_price = -1

print(f"\nWelcome to the Shopping Cart Program! ")

action = ""
while action != 5:

      count = -1
      count_price = 0
      print(f"\nPlease select one of the following: \n"
            f"\n1. Add item "
            f"\n2. View cart "
            f"\n3. Remove item "
            f"\n4. Compute total "
            f"\n5. Quit \n")
            
      action = input("Please enter an action: ")
      if action.isdigit():
            action = int(action)
            if action == 1:
                  new_item = input("\nWhat item would you like to add? ")
                  new_price = float(input(f"\nWhat is the price of '{new_item}'? "))      
                  print(f"\n'{new_item}' has been added to the cart. ")
                  items.append(new_item)
                  prices.append(new_price)
                                    
            elif action == 2:
                  print("\nThe contents of the shopping cart are: \n")
                  count = count + 1
                        
                  for item in items:
                        count = count + 1
                        count_price = count_price 
                        price = prices[count_price]
                        count_price += 1
                        print(f"{count}. {item} - ${price:.2f} ")

            elif action == 3:
                  remove_item = int(input("\nWhich item would you like to remove? "))
                  x = remove_item - 1
                  del items[x]
                  del prices[x]
                  print("Item removed. ")

            elif action == 4:
                  sum_list_prices = sum(prices)  
                  print(f"\nThe total price of the items in the shopping cart is {sum_list_prices:.2f}")
                              
            elif action == 5:
                  print("\nThank you. Goodbye. \n")

            else:
                  print("\nInvalid choise. Try again. ")
      else:
            print("\nJust numbers are accepted. Try again.")