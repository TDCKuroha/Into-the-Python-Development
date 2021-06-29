
loan_large = int(input("\nHow large is the loan? "))
credit_history = int(input("\nHow good is your credit history? "))
income = int(input("\nHow high is your income? "))
down_payment = int(input("\nHow large is your down payment? "))

if loan_large >= 5:
    
    if credit_history >= 7 and income >= 7:
           
            decision = True 
    
    elif credit_history >= 7 or income >= 7:
        
        if down_payment >= 5:
          
             decision = True
        
        else:
            
            decision = False 

                
    else:

        decision = False

else:

    if credit_history < 4:

        decision = False

    else:

        if income  >= 7 or down_payment >= 7:

            decision = True

        elif income >= 4 and down_payment >= 4:

            decision = True
        
        else:

            decision = False

if decision:
    print("\nThe decision is yes. This is a good loan.")

    input()
else:
    print("\nThe decision is no. You should not loan this money.")

    input()