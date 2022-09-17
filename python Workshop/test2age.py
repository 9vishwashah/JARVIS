a=int(input("enter age="))
print("ur age is=",a)

if(a>=18):
    print("valid to vote")
elif(a<18 and a>3):
    print("u cannot vote")
else:
    print("Invalid to vote")