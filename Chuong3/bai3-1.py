import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    Dientich= round(math.sqrt(p*(p-a)*(p-b)*(p-c)),3)
print("Dien tich=",Dientich)
else:
print("Khong hop le")