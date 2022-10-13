p=int(input("Enter value of P:"))
r=int(input("Enter value of R:"))
t=int(input("Enter value of T:"))
n=int(input("Enter value of N:"))
si=float(p*r*t)/(100)
print("Simple Interest=",si)
co=float (p)*((1+r)/(100*n))**n*t
print("Compound Interest=",co)




