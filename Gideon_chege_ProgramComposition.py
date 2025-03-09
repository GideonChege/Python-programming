
#Name: Gideon Wamburu
#Date: 01/21/2025
#Assignment Bonus: program composition, learning to structure program

#Write a program that can compute the area, circumference and volume of a sphere based on any given radius.

#What are the inputs to the code? Radius
radius=input('please input the radius for calaculations')
radius=float(radius)#type conversion from string to float

#Eco back the input (to make sure it was captured)
print('the radius you input is:',radius)
PI = 3.14159

#calculationa: Area
area=PI*radius*radius

#Circumference next
circumference=2*PI*radius

#volume last
volume= 4/3*PI*radius**3

#Now lets fomart the results for printing
#the results should be nice and neat. Cap the decimals to 3dp

#print(f'(The area of a circle with radius of',radius, f'is, {area:.3f}')

print(f'the area of a circle with radius of {radius} is {area:.3f}')
print(f'the circumference of a circle with radius of {radius} is {circumference:.3f}')
print(f'the volume of a circle with radius of {radius} is {volume:.3f}')



