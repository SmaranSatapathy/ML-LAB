x=int(input("Enter a number: "))
sum=0

while(x!=0):
    rem=int(x%10)
    sum+=rem
    x=int(x/10)
print(sum)
if(sum%9==0):
    print("Divisible by 9")
else:
    print("Not divisible by 9")