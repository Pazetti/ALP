def par(n):
    if n%2 == 0:
        return True
    return False

x=int(input("Digite um valor:"))
if par(x):
    print("O valor digitado é par")
else:
    print("O valor digitado é Impar!")