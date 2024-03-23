salhora=float(input("Insira o total recebido por hora trabalhada:"))
thora=int(input("Insira o total de horas trabalhadas por mes:"))

salariobruto=(salhora*thora)

if salariobruto<=900:
    ali=0
    impr =0

elif salariobruto<=1500:
    ali=5
    impr =(salariobruto*(ali/100))

elif salariobruto<=2500:
    ali=10
    impr =(salariobruto*(ali/100))
else:
    ali=20
    impr =(salariobruto*(ali/100))

sindi=float(salariobruto*(3/100))

fgts=float(salariobruto*(11/100))

inss=float(salariobruto*(10/100))

salarioliquido=float(salariobruto-impr-inss-sindi+fgts)

print("salario bruto: (",salhora,"*",thora,") : R$:", salariobruto)
print("(-) IR (",ali,"%): R$:",impr)
print("(-)INSS (10%) R$:",inss)
print("(-)Taxa de sindicato (3%) R$:",sindi)
print("(+)FGTS (11%) R$:", fgts)
print("Com isso tudo o valor liquido que voce tem a receber é:",salarioliquido)








