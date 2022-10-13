from re import X


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
x= a if a > b else b
max = x if x > c else c
print("Maximum Number is:",max)