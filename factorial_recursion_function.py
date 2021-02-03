

def factorial(n):
    product=1
    for  i in range(n):
        product=product *(i+1)
    return product

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursive(n-1)

n=int(input("Enter the number = "))
f=factorial(n)
print(f)