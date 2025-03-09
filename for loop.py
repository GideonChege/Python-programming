##for num in (1,2,3,3,4,5,6):
##    print(num)
##for counter in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15):
##    print(counter)
##for fruit in ('Apple', 'strawberry', 'banana'):
##    print(fruit)
##for i in range(1,16):
##    i*=2
##    print(i)
##for i in range(1,2,10):
##    print(i)
##for i in range(1,101):
    #i=i**(1/2)
    #print(i)
##    print(i:=i**(1/2))        
total = 0.0
MAX=10
print('This program calculates the sum of the', MAX, 'numbers you will enter')
for counter in range(MAX):
    number = int(input('Enter a number'))
    total+=number
    print('the total is' , total)
    if str (number=='q'):
        break


    
'''while(score:=int(input('Input your score', )))<0:
    print('The score cannot be negative')'''
