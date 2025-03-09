#Name: Gideon Chege
#Due date: Jan 30 2025
#Assign Number = Assignment_1

#Question1
a,b,c,d,e,f,g,h,i,j,k,l = 'All', 'work', 'and', 'no', 'play', 'make', 'Jack', 'a', 'dull', 'boy', 'who\'s', 'tired.'
print(a,b,c,d,e,f,g,h,i,j,k,l)

#Question2
answer=6*1-2
answer=6*(1-2)
print(answer)

#Question3
#bruce+4 (Since bruce is undefined)
bruce=6
print(bruce+4)

#Question4
P=int(10000)
n=int(12)
r=float(0.08)
t=int(input('Input the number of years that the money will be compounded for: '))
#Calculation for the final amount using the fomula provided.
a=n*t
b=r/n
c=1+b
d=c**a
e=P*d
print(f'The final amount after {t} years is: ${e:.2f}')

#Question5

a,b,c,d,e,f=5%2,9%5,15%12,12%15,6%6,0%7
#7%0 (for 7%0 the result is an error since any number divided by zero is : zero divisionerror.)
print(a,b,c,d,e,f)

#Question6
a=2
b=61
c=b%24
d=b//24
e=a+c
if e<=12:
    print(f'the alarm would go off {d} days after alarm was set at excactly {e}:00 PM.')
else:
    print(f'the alarm would go off {d} days after alarm was set at excactly {e-12}:00 AM.')

#Question7
# Get the current time and hours to wait from the user

current_time=int(input('What is the time in hours (Input your time in 24 hour fomart): '))
if current_time<=25:
    a=current_time
    
    waiting_hours=int(input('Input the number of hours you want to wait before your alarm goes off: '))

    # Calculate the day and time when the alarm goes off
    days=(waiting_hours+a)//24 #Number of complete days

    alarm_time =(a+waiting_hours)%24 #Remaining hours in the day
    if alarm_time<=12:
        print(f'The alarm will go off in {days} day(s) after the alarm was set, at exactly {alarm_time}:00AM')
    else:
        alarm_time=alarm_time-12
        print(f'The alarm will go off in {days} day(s) after the alarm was set, at exactly {alarm_time}:00PM')
else:
    print('Sorry the time you input is invalid; please input the correct time.')
   

