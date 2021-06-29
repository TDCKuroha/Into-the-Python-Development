#Asking for the information!

meal_price_children = float(input("\nWhat is the price of a child's meal? "))
meal_price_adults = float(input("What is the price of an adult's meal? "))
how_many_children = int(input("How many children are there? "))
how_many_adults = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

#Doing the math.

subtotal = (meal_price_children * how_many_children) + (meal_price_adults * how_many_adults)
formatted_float_subtotal = "${:.2f}".format(subtotal)
sales_tax = (subtotal * tax_rate) / 100
formatted_float_sales_tax = "${:.2f}".format(sales_tax)
total = subtotal + sales_tax
formatted_float_total = "${:.2f}".format(total)

#Printing the receipt.

print(f"\nSubtotal: {formatted_float_subtotal}")
print(f"Sales Tax: {formatted_float_sales_tax}")
print(f"Total: {formatted_float_total}")

#Asking payment amount to know how much money we need to give back to the cx.

payment_amount = float(input("\nWhat is the payment amount? "))
change = payment_amount - total
formatted_float_change = "${:.2f}".format(change)
print(f"Change: {formatted_float_change}\n")

input()