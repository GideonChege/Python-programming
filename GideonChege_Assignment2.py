#Gidoen Chege
#Assignemnt2
#14th Feb 2025

#Question 1
#A program that takes in number of the day and outputs the day of the week to the user.

day_name = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day_number = int(input('Please input the day_number (0-6):'))

if day_number >=0 or day_number <= 6:
    print(f'Day {day_number}: is {day_name[day_number]}')
else:
    print('Please enter a valid number between 0 and 6')




#Question2

# Prompt the user to enter the starting day number (0 to 6)
starting_day_number=int(input('Please enter your starting day between (0 and 6): '))
# Define a list to map day numbers to their corresponding names
day_name = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

if starting_day_number in range(7):
    stay_length= int(input('Enter the number of days you plan to stay'))
    
    # Calculate the return day number using modulo to keep within the range of 0-6
    length = (stay_length+starting_day_number)%7
    print(f'you will return home on: {day_name[length]}')
else:
    print('Please enter a valid number between (0 and 6): ')

'''
#Question3
1. a<=b
2. a<b
3. a<18 or day!=3
4. a<18 or day ==3


#Question4

1. True
2. False
3. False
5. False



#Question 5

p q r | (p and q) |not (p and q) | (not (p and q)) or r

F F F      F           T                      T  
F F T      F           T                      T  
F T F      F           T                      T 
T T T      F           T                      T 
T F F      F           T                      T
T F T      F           T                      T
T T F      T           F                      F
T T T      T           F                      T


'''
#Question 6
#A program which is given an exam mark, and it returns a string — the grade for that mark


grade= float(input("Input your mark"))
if grade<= 100: # check that grade does not exceed 100
    if grade>= 75: # if the grade is entered is beween 75 and 100
    
        print("First")
    elif grade<75 and grade >=70:
        print("Upper Second")
    elif grade<70 and grade >=60:
        print('Second')
    elif grade<60 and grade >=50:
        print('Third')
    elif grade<50 and grade >=45:
        print('FI Supp')
    elif grade<45 and grade >=40:
        print('F2')
    elif grade<40:
        print('F3')
else:
    print("Invalid Grade")
              

#Question7

# Determine square root of 2, multiply it by itself and compare to
# 2.0

a = 2.0 ** 0.5
print(a, a*a)
print(a*a == 2.0)


##when I run the the above program the values are:
##The square root of 2.0 is approximated as: 1.4142135623730951
##When we square this value, we expect to get exactly 2.0,
##but the result is 2.0000000000000004 instead.
##when we compare the squared value to 2.0 the return is False
##because theya re not exacly equal.
##This because 2.0 is stored as a float number in a finite memory
##and when we perform mathematical operations
##some small inaccuracies occurs because  of rounding off inaccuracies.


#Question8

#a program that given the length of three sides of a triangle,
#It will determine whether the triangle is right-angled.

a = float(input('Input the height: '))
b = float(input('Input the lenght: '))
c = float(input('Input the Hypotenuse: '))

lhs = a**2 + b**2
rhs = c**2

if abs(lhs-rhs)<0.00001:
    print('True -  It is a right_angle triangle')
else:
    print('False - It is a NOT a right_angle triangle')
           
























