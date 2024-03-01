weekdays={
    0:'SUNDAY',
    1:' MONDAY',
    2:'TUESDAY',
    3:'WEDNESDAY',
    4:'THRUSDAY',
    5:'FRIDAY',
    6:'FRIDAY'
}

n=int(input("Enter week number: "))
print(weekdays.get(n))

future=int(input("Enter future: "))
if(future>=7):
    future=future%7
print(weekdays.get(future))