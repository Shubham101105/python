import math
from operator import length_hint

#import math


#def main()
angle = eval(input("Enter the value of angler"))
height = eval(input("Enter the value of Height"))
angler = (3.14/180)*angle
length = (height / math.sin(angler))
print("lenght of ladder",length)



