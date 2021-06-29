chosen_year = int(input("\nEnter the year of interest: "))
print("")

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

        if life_expectatancy < min_life:
                        min_life = life_expectatancy
                        countries_from_min = state
                        year_from_min = year

        if life_expectatancy > max_life:
                        max_life = life_expectatancy
                        countries_from_max = state
                        year_from_max = year 

print(f"The overall max life expectancy is: {max_life} from {countries_from_max} in {year_from_max}")
print(f"The overall min life expectancy is: {min_life} from {countries_from_min} in {year_from_min}\n")

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