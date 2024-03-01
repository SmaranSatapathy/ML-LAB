x=int(input("Enter 1st number: "))
y=int(input('Enter 2nd number: '))
count=0
primes=[]
for i in range(x,y+1):
    for j in range(1,i):
        if(i%j==0):
            count+=1
        if(count==2):
            primes.append(i)
    count=0
print(primes)