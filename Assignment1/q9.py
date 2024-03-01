x=int(input("Enter number from 0 to 1000: "))
sum=0
while(x!=0):
    rem=int(x%10)
    sum+=rem
    x=int(x/10)
print("Sum is: ",sum)