def per(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/400)*100
    return p

marks1=[45,78,98,55,45]
per1= per(marks1)

marks2 = [75,98,76,35,85]
per2=per(marks2)

print(per1,per2)
#=============================================
#passing arguments to function

def add(a,b):
    print(a+b)
def mul(a,b):
    print(a*b)
def subsrt(a,b):
    print(a-b)

add(10,20)
mul(20,30)
subsrt(30,15)

#=================---------------
# Passing function as arguments in python

def add(a,b):
    c=a+b
    return c
def mul(a,b):
    c=a*b
    return c
def sub(a,b):
    c=a-b
    return c

x=int(input("Enter 1= "))
y=int(input("Enter 2= "))

result= add(x,y)
result1= mul(x,y)
result2= sub(x,y)
print("Result",result,result1,result2)

#===========================================
# making function return value in python
def add(a,b):
    c=a+b
    return c
def mul(a,b):
    c=a*b
    return c
def sub(a,b):
    c=a-b
    return c

Sum = add(100,200)
Multiply= mul(100,200)
Substract = sub(200,100)
print(Sum,Substract,Multiply)





