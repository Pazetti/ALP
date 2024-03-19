lado1=float(input("Insira o valor do primeiro lado:"))
lado2=float(input("Insira o valor do segundo lado:"))
lado3=float(input("Insira o valor do terceiro lado:"))

if ((lado1+lado2)<lado3) or ((lado2+lado3)<lado1) or ((lado3+lado1)<lado2):
    print("Não é um triangulo.")
else:
    if(lado1==lado2) and (lado2==lado3):
        print("Triangulo equilatero")
