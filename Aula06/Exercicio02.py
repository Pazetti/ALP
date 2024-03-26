compra=float(input("Insira o valor gasto:"))

if compra<=1000:
    desc=(compra*(10/100))
elif compra<=5000:
    desc=(compra*(20/100))
else:
    desc=(compra*(30/100))

print("O valor do desconto sobre sua compra de",compra, "reais é:",desc,"reais")

