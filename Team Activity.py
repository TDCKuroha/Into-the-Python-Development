# Area of a square

length_square = float(input("What is the length of a side of the square? "))
area_square = length_square ** 2 
print(f"The area of the square is: {area_square}")

# Area of a rectangle

rectangle_length = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
area_rectangle = rectangle_length * rectangle_width
print(f"The area of the rectangle is: {area_rectangle}")

# Area of a circle

circle_radius = float(input("What is the radius of the circle? "))
area_circle = 3.14 * (circle_radius ** 2)
print(f"The area of the circle is: {area_circle}")


# Stretch 1: Using the math library

import math
radius = float(input("What is the radius of the circle? "))
area = math.pi * (radius ** 2) 
print(f"The area of the circle is: {area}")

# Stretch 2: Many areas from one value

value = float(input("What is the value to be used? "))

# Calculate areas

area_square = value ** 2
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
volume_sphere = (4 / 3) * math.pi * (value ** 3)

# Area of a square - cm -> m conversion

side = float(input("What is the length of a side of the square (in cm)? "))
area = side ** 2

print(f"The area of the square is: {area} cm^2")
print(f"The area of the square is: {area / 10000} m^2")

# Area of a rectangle - cm -> m conversion

length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"The area of the rectangle is: {area} cm^2")
print(f"The area of the rectangle is: {area / 10000} m^2")

# Area of a circle - cm -> m conversion

radius = float(input("What is the radius of the circle (in cm)? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area / 10000} m^2")


