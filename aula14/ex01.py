def bixo(c,p):
    if (c < p):
        coelhos = int((p - 2 * c) / 2)
        patos = int(c - coelhos)

        print(f"Coelhos: {str(coelhos)}")
        print(f"Patos: {str(patos)}")
    elif (p == c):
        print("Numero invalido")
    else:
        print("Numero invalido")

c = int(input("Digite a quantidade de cabeças: "))
p = int(input("Digite a quantidade de patas: "))

bixo(c,p)
