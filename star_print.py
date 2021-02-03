#=============================================
n=4
for i in range(4):
    print("*"*(i+1))

#=====================================

n=10

for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(""*(n-i-1))

#===============================================

n=int(input("Enter the range="))
for i in range(0,n):
    for j in range(0,i+1):
        print("& ",end="")
    print("\r")
#===============================================

n=int(input("Enter the range="))

k= 2*n-2

for i in range(0,n):
    for j in range(0,k-1):
        print(end=" ")
    k=k-2
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")


#==============================

n=int(input("Enter the range= "))
num=1

for i in range(0,n):
    num=1
    for j in range(0,i+1):
        print(num,end=" ")
        num=num+1
    print("\r")
#=================================================

n= 12
num = 1

for i in range(0, n):
    for j in range(0, i + 1):
        print(num, end=" ")
        num = num + 1

    print("\r")
#=========================================

n=6
for i in range(n):
    print("*"*(n-i))






