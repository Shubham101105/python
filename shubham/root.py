from cmath import sqrt


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
delta=((b**2)-(4*a*c))
solution_1=((-b+sqrt(delta))/(2*a))
solution_2=((-b-sqrt(delta))/(2*a))
print("Delta is",delta)
print("Solution-1 is",solution_1)
print("solution-2 is",solution_2)
