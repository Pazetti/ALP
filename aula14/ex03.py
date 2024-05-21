n=str(input("Insira um numero:"))

if not n.isdigit() or int(n)<=0:
    print("Numero invalido, por favor, insira um número positivo.")
    exit()
l=list(map(int, n))
soma=0
mult=1
for numero in l:
    soma += numero
for numero in l:
  mult *= numero

print(mult,soma)