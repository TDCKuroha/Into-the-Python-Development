people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 9999
youngest_name = None

for person_line in people:
    parts = person_line.split()
    name = parts[0]
    age = int(parts[1])

    if age < youngest_age:
        # This person is the new "youngest"

        # Save their age as the new youngest
        youngest_age = age

        # Save their name as the youngest name
        youngest_name = name

print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")



# names_list = []
# years_list = []

# for line in people:
#     data = line.split(" ")
#     names = data[0]
#     years = int(data[1])
#     names_list.append(names)
#     years_list.append(years)

#     youngest = min(years_list)
#     place = years_list.index(youngest)

# print(names_list[place])

    