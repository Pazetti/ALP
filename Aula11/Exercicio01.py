lista=[]

for i in range(10):
    cont=int(input(f"Digite o numero {i+1}:"))
    lista.append(cont)

t=tuple(lista)
print(t[::-1])