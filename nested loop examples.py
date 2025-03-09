'''
for i in range (5):# Gives us the number of rows
    for j in range(3):#Gives us the number of columns 
        print('*', end = ' ')
    print ('\n')


'''

for i in range(1,11):
    for j in range(1,6):
        print(f'{j*i:12}', end = ' ')
    print('\n')
    
'''
#simulation of a clock
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)

for i in range (10,0,-1):
    for j in range(i):
        print(f'{'*':3}', end = " ")
    print('\n')
        


def butler():
    print('At your service, madame!')# Defining a function(void function)
    
butler() # Calling a function.



def butler(name):
    print('At your service', name)
butler ('Sally')

def butler(name):
    print('At your service', name)
    return 'coffee'
table = 'empty'
table = butler ('Joe')

butler ('Joe')
'''
