def seg(h,m,s):
    horas=(h*3600)
    minutos=(m*60)
    segundos=s
    total=horas+minutos+segundos
    return total


h = int(input("Insira a quantia de horas:"))
m = int(input("Insira a quantia de Minutos:"))
s = int(input("Insira a quantia de segundos:"))

print(f"O total de segundos é {seg(h,m,s)}")