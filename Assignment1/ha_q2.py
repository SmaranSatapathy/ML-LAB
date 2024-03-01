x=n=int(input("Enter number: "))
sum=0

while(n!=0):
    rem=n%10
    sum+=rem
    n=int(n%10)
if(x==sum):
    print("Perfect Number")
else:
    print("Not a perfect Number")