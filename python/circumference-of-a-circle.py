# @Author Oluwapelumi
#Importing math lib
import math
# Getting radius from user
radius = float(input("Enter the radius of a circle: "))
#using the formula
circumference = 2 * math.pi * radius
# I had to cast the radius value to string for concatenation
print("The circumference of a circle with radius" + str(radius) + " is: " , circumference)