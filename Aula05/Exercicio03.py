l1=float(input("Insira o valor do primeiro lado:"))
l2=float(input("Insira o valor do segundo lado:"))
l3=float(input("Insira o valor do terceiro lado:"))

if ((l1+l2)<l3) or ((l2+l3)<l1) or ((l3+l1)<l2):
    print("Não é um triangulo.")
else:
    if (l1 == l2) and (l2 == l3):
        print("Triangulo Equilátero")
    elif (l1 == l2) or (l2 == l3) or (l1 == l3):
        print("Triangulo Isósceles")
    else:
        print("Triangulo Escaleno")