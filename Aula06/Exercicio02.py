nota1=float(input("Insira a N1:"))
nota2=float(input("Insira a N2:"))
nf=((nota1+nota2)/2)
if nf<=4.0:
    conc= "E"
elif nf<=6.0:
    conc= "D"
elif nf<=7.5:
    conc="C"
elif nf<=9.0:
    conc="B"
else:
    conc="A"
print("Sua nota final é:", nf)
print("Conceito:",conc)