from math import pi, pow

def vol(raio):
    return (4/3)*pi*pow(raio, 3)


r = float(input("Insira o valor do raio:"))

print(f"O resultado é {r} é {vol(r)}.")