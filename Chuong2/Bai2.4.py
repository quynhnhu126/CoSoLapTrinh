a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
S=(a+b+c)/2
import math
x=math.sqrt(S*(S-a)*(S-b)*(S-c))
print("Dien tich=",float(x),sep="")