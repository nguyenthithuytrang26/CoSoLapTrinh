a=int(input("Tieu thu="))
dg1=550
dg2=750
dg3=950
dg4=1350
if a<=100:
    tiendien= a*dg1
elif a<=150:
    tiendien= 100*dg1+(a-100)*dg2
elif a<=200:
    tiendien= 100*dg1+50*dg2+(a-150)*dg3
else:
    tiendien= 100*dg1+50*dg2+50*dg3+(a-200)*dg4
Phaitra= tiendien+(0.1*tiendien)
print("Phai tra=",Phaitra)