data = []

with open("life-expectancy.csv", "r+") as f:
        data = f.readlines()[1:19029]
        

        lst = []
       
for n in range(19029):
        lst.append(data)
print(max(lst))
   
        