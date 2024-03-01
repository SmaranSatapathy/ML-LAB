x=int(input("Enter 1st number: "))
y=int(input(" Enter 2nd number: "))
rem=-1
while (rem!=0):
    q=int(x/y)
    rem=int(x%y)
    x=y
    y=rem
print(" GCD is: ",int(x))
