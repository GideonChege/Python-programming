'''spam=0
if spam<5:
    print('Hello world')
    spam = spam +5
    
spam=0
while (spam<5):
    print('Hello world')
    spam =spam+1
    
number = 5
while number <11:
    print(number)
    number =number+1
    
keep_going='y'
while keep_going=='y':
    sales=float(input('input the amount oif sales'))
    com_rate=float(input('commision rate'))
    commision =sales *com_rate
    print(commision)
    keep_going=input('Do you want to continue?'
                    'input y for yes and any other to exit')

print('exit the loop')

#Testing out repitation structure

score=int(input('Ester your score test'))
while (score<0 or score>100):
    print('ERROR!! the score cannot be greater than 100')
    print('the score canot be negative')
    score=int(input('Ester your score test'))
    
#A program that can calculate and print powers of 2 upto 100.

##n=2 # n would would hold the powers of 2
##while (n<100):
##    print(n)
##    n*=2
    
# Running total: find the summation total of number from 1 to 30
sum=1
total=0
while (sum<=400):
    total+=sum #Running total
    sum +=1 #allows the loop to stop
    print(total:,)
print('the running total is',total)

#lecture 9 import of modules

# This program the rolling of dice.
import random
# Constants for the minimum and maximum random numbers
MIN = 1
MAX = 6
def main():
    # Create a variable to control the loop.
    again = 'y'
    # Simulate rolling the dice.
    while again == 'y' or again == 'Y':
        print('Rolling the dice . . .')
        print('Their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))
        # Do another roll of the dice?
        again = input('Roll them again? (y = yes): ')
    print ('goodbye')
# Call the main function.
main()
'''

#Functions
def get_name():
    print('Please give me your full names')
    last_name=input('Last name')
    first_name=input('first name')
    return last_name, first_name

def get_input():
    print('Please input 3 intergers')
    num1=int(input('Number 1: '))
    num2=int(input('Number 2: '))
    num3=int(input('Number 3: '))
    return num1, num2, num3
def show_sum(a,b,c):
    sum=num1+num2+num3
    return sum

def is_even(number):
    ''' Boolean function to check if an integer is even or odd
        input: interger number
        output: boolean True or False
    '''
    if number%2==0:
        return True
    else:
        return False
##if (is_even(34)): print('even')
             
def main(): # A function to call the other functions
    last,first = get_name()
    print('welcome to this module', last, first)
    x,y,z=get_input()
    print('The sum is:', x+y+z)
    if (is_even(x) and is_even(y) and is_even(z)):
        print('All inputs are even')
    else:
        print('Atleast one of the inputs is odd')
    
    
if __name__ == "main": #Only run the main if the file is being use currently
    
    main() #call the main function
    
