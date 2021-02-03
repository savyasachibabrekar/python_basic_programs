def max(num1,num2,num3):
    if num1>num2:
        if num2>num3:
            return num1
        else:
            return num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3


m= int(input("Enter 1st no= "))
n= int(input("Enter 1st no= "))
o= int(input("Enter 1st no= "))

maximum= max(m,n,o)
print("The value of maximum of three no is :",maximum)

