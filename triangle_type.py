a=int(input("enter the lenght of first side: "))
b=int(input("enter the lenght of second side: "))
c=int(input("enter the lenght of third side: "))
if a==b==c:
    print("it is an equalateral triangle")
elif a!=b!=c:
    print("it is a scalene triangle")
else:
    print("it is an isosceles triangle")