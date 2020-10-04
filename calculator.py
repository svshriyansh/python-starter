def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def quotient(a,b):
    return a//b
def remainder(a,b):
    return a%b

choice='y'
while choice!='n':
    inp=int(input("OPERATION\n1:ADDITION\n2:SUBTRACTION\n3:MULTIPLICATION\n4:DIVISION\n5: QUOTIENT\n6: REMAINDER\n"))
    a=int(input("ENTER FIRST NUMBER"))
    b=int(input("ENTER SECOND NUMBER"))
    if inp==1:
        ans=add(a,b)
        print("SUM="+str(ans))
    elif inp==2:
        ans=subtract(a,b)
        print("DIFFERENCE="+str(ans))
    elif inp==3:
        ans=multiply(a,b)
        print("PRODUCT="+str(ans))
    elif inp==4:
        ans=division(a,b)
        print("DIVISION="+str(ans))
    elif inp==5:
        ans=quotient(a,b)
        print("DIVISION="+str(ans))
    elif inp==6:
        ans=remainder(a,b)
        print("DIVISION="+str(ans))
    else:
        print("WRONG INPUT")
    choice=raw_input("CONTINUE(y/n)")
print("THANK YOU")