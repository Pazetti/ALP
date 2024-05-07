def potencia(numero, expoente = 2):
    resultado = pow(numero, expoente)
    return resultado

n=float(input("Insira o valor do numero:"))
e=int(input("Insira o valor do expoente:"))
print(f"Valor com expoente: {potencia(n,e)}")
print(potencia(expoente = e, numero = n))
print(f"Valor sem o expoente: {potencia(n)}")