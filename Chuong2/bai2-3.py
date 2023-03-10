import math
print("Nhap hai canh ke cua tam giac vuong: ")
a=int(input())
b=int(input())
x=round(math.sqrt(a**2+b**2),2)
print("Canh ke thu nhat la:",a,end=", ")
print("canh ke thu hai la:",b,end=", ")
print("co canh huyen =",round(x,2))
