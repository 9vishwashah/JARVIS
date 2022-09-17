import math
a=int(input("Enter 1st Number "))
b=input("Select ur operator(*,/,+,-,%,**):")
c=int(input("Enter 2nd Number "))
if b == '**':
    print(math.pow(a,b))

elif b == '+':
    print(a+c)

elif b == '/':
    print(a/c)

elif b == '-':
    print(a-c)

elif b == '*':
    print(a*c)

elif b == '%':
    print(a%c)
else:
    print("Invalid operation")



