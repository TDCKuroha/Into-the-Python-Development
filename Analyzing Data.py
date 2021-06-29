chosen_year = int(input("\nEnter the year of interest: "))
print("")

# stat_list = []
# code_list = []
# year_list = []
# life_list = []

min_life = 9999
countries_from_min = None
year_from_min = None

max_life = -1
countries_from_max = None
year_from_max = None

with open("life-expectancy.csv") as new_file:
    for data in new_file:
        new_data = data.strip()
        part = new_data.split(",")
        state = part[0]
        code = part[1]
        year = int(part[2])
        life_expectatancy = float(part[3])
#         stat_list.append(state)
#         code_list.append(code)
#         year_list.append(year)
#         life_list.append(life_expectatancy)

        if life_expectatancy < min_life:
                        min_life = life_expectatancy
                        countries_from_min = state
                        year_from_min = year

        if life_expectatancy > max_life:
                        max_life = life_expectatancy
                        countries_from_max = state
                        year_from_max = year 

print(f"The overall max life expectancy is: {max_life} from {countries_from_max} in {year_from_max}")
print(f"The overall min  life expectancy is: {min_life} from {countries_from_min} in {year_from_min}\n")

min_life = 9999
countries_from_min = None
year_from_min = None
suma = 0
count = 0

max_life = -1
countries_from_max = None
year_from_max = None

with open("life-expectancy.csv") as new_file:
    for data in new_file:
        new_data = data.strip()
        part = new_data.split(",")
        state = part[0]
        code = part[1]
        year = int(part[2])
        life_expectatancy = float(part[3])
#         stat_list.append(state)
#         code_list.append(code)
#         year_list.append(year)
#         life_list.append(life_expectatancy)
       
        if year == chosen_year:
                
                count += 1 
                suma += life_expectatancy 
                
                if life_expectatancy < min_life:
                        min_life = life_expectatancy
                        countries_from_min = state
                        year_from_min = year

                if life_expectatancy > max_life:
                        max_life = life_expectatancy
                        countries_from_max = state
                        year_from_max = year 
        
avg = suma / count                 
print(f"For the year {chosen_year}:")
print(f"The average life expectancy across all countries was {avg:.2f}"
      f"\nThe max life expectancy was in {countries_from_max} with {max_life}"
      f"\nThe min life expectancy was in {countries_from_min} with {min_life}\n")

# number_max = -1

# for number in life_list:
#     if number > number_max:
#         number_max = number

# position_max = life_list.index(number_max)

# number_min = 99999999999

# for number in life_list:
#     if number > 0 and number < number_min:
#         number_min = number

# position_min = life_list.index(number_min)

# print(f"The overall max life expectancy is: {number_max} from {stat_list[position_max]} in {year_list[position_max]}")
# print(f"The overall min life expectancy is: {number_min} from {stat_list[position_min]} in {year_list[position_min]}")



