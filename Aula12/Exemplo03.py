from math import pi, pow
def area_circ(raio):
    area=pi*pow(raio,2)
    return area

r=float(input("Digite o raio:"))
print(f"A área do circulo de raio {r} é igual a {area_circ(r)}")