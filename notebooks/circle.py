
"""
Program: circle.py
Author: Umar Waru
Last date modified: 21/9/26
The purpose of this program is to compute the area of a circle. The input
is an integer or floating-point number representing the radius of the 
circle. The outputs are floating-point numbers labeled as the circumference of the 
circle and the area of the circle.
"""
import math

radius = float(input("Enter the radius of the circle ")) #input is converted into float for compatibility with math module
# calculating the circumference and the area using user input
circum = 2 * math.pi * radius # TODO 
area = math.pi * radius ** 2  # TODO

print('Circumference:', str(circum) , 'Area:',str(area)) 