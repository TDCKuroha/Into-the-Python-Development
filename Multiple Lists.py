bank_accounts = []
balances = []

name_account = None
new_balance = -1
index = -1
index_2 = -1

print("Enter the names and balances of bank accounts (type: quit when done) ")

while name_account != "quit":
   
   name_account = input("What is the name of this account? ")
   
   if name_account != "quit":
        new_balance = float(input("What is the balance? "))
        bank_accounts.append(name_account) 
        balances.append(new_balance)

if name_account == "quit":
    
    print("\nAccount Information: ")
    
    for account in bank_accounts:
        index += 1
        amount = balances[index]
        print(f"{index}. {account} - ${amount}")
        
total_balance = sum(balances)
print(f"\nTotal: ${total_balance:.2f}")
average = total_balance / len(balances)
print(f"Average: ${average:.2f}")

highest_name = None
highest_balance = -1

for i in range(len(bank_accounts)):
    account = bank_accounts[i]
    balance = balances[i]

    if balance > highest_balance:
        highest_balance = balance
        highest_name = account

print(f"Highest balance: {highest_name} - ${highest_balance:.2f}")

change_account = "yes"

while change_account == "yes":
    change_account = input("\nDo you want to update an account? ")
    
    if change_account == "yes":
        index_number = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))

        balances[index_number] = new_amount
  
    print("\nAccount Information: ")

    for account in bank_accounts:
        index_2 += 1
        amount = balances[index_2]
        print(f"{index_2}. {account} - ${amount}")
    
