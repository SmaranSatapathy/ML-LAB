x=int(input("Enter Rahul age:"))
y=int(input("Enter Ayush age:"))
z=int(input("Enter Ajay age:"))

if(x>y and x>z):
    print("Rahul is the eldest")
elif(y>x and y>z):
    print("Ayush is the eldest")
else:
    print("Ajay is the eldest")