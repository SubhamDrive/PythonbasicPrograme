#Programe for ArthematicOperator

print("1.Addition        (+)")
print("2.Substraction    (-)")
print("3.Division        (/)")
print("4.Multiplication  (*)")
print("5.Modulus         (%)")
print("6.Square Root     (**)")
print("7.Floor Division  (//)")


a= int(input("Enter Your Choice"))

def add():
    a1=int(input("Enter First Number: "))
    b1=int(input("Enter Second Number: "))
    print("Sum is ", a1+b1)
def sub():
    a1=int(input("Enter First Number: "))
    b1=int(input("Enter Second Number: "))
    print("Diffrence is ", a1-b1)

def mul():
    a1=int(input("Enter First Number: "))
    b1=int(input("Enter Second Number: "))
    print("Product is ", a1*b1)

def div():
    a1=int(input("Enter First Number: "))
    b1=int(input("Enter Second Number: "))
    print("Reminder is ", a1/b1)

def mod():
    a1=int(input("Enter First Number: "))
    b1=int(input("Enter Second Number: "))
    print("Modulus is ", a1%b1)

def sqr():
    a1=int(input("Enter First Number: "))
    b1=int(input("Enter Second Number: "))
    print("Square Root is ", a1**b1)

def floor():
    a1=int(input("Enter First Number: "))
    b1=int(input("Enter Second Number: "))
    print("Floor Division is ", a//b1)

def doyouwanttocon():
    y=int(input("If You Want To continue Then Press 1 else Any Button: "))
    if y==1:
        a = int(input("Enter Your Choice"))
        if a == 1:
            add()
            doyouwanttocon()
        elif a == 2:
            sub()
            doyouwanttocon()
        elif a == 3:
            div()
            doyouwanttocon()
        elif a == 4:
            mul()
            doyouwanttocon()
        elif a == 5:
            mod()
            doyouwanttocon()
        elif a == 6:
             sqr()
             doyouwanttocon()
        elif a == 7:
             floor()
             doyouwanttocon()
        else:
            print("Wrong Input Please Try Again!!")
            doyouwanttocon()
    else:
        exit()


if a==1:
      add()
      doyouwanttocon()
elif a==2:
    sub()
    doyouwanttocon()
elif a==3:
    div()
    doyouwanttocon()
elif a==4:
    mul()
    doyouwanttocon()
elif a==5:
    mod()
    doyouwanttocon()
elif a==6:
    sqr()
    doyouwanttocon()
elif a==7:
    floor()
    doyouwanttocon()
else:
     print("Wrong Input Please Try Again!!")
     doyouwanttocon()




