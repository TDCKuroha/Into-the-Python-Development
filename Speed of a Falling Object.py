import math

print("\nWelcome to the velocity calculator. Please enter the following:\n")

#Asking for the info for my variables.

m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
a = float(input("Cross sectional area (in m^2): "))
c = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print()  

C = (1 / 2) * p * a * c
v = math.sqrt(m * g / C) * (1 - math.exp((-math.sqrt(m * g * C) / m) * t))
v_f = math.sqrt(m * g / C)
time_taken = math.sqrt(2 * m * g) / (p * a * c)

print(f"The inner value of c is: {C:.3f}")   
print(f"The velocity after {t} seconds is: {v:.3f} m/s")
print(f"The final velocity is: {v_f:.3f} m/s")     
print(f'The time that takes to reach the "terminal velocity" is: {time_taken:.3f} seg. \n')  

 

input()