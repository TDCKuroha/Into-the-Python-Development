
col = int(input("How many columns and rows do you want in your multiplication table? "))

z = col + 1

for row in range(1, z):
    print(row, end="\t")
print("")
print("_______________________________________________________________________________________________________________________________________________________________________________")
print("")

for columns in range(1, z):
    for k in range (1, z):
        print(f"{columns * k}", end ="\t")
    print("\n")