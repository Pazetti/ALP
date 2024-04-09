frase=input("Insira sua frase:").strip()
palavras=frase.split()
frase1=''
for palavra in palavras:
    frase1=frase1+palavra
frase2=frase1[::-1]
if frase1==frase2:
    pali=True
else:
    pali=False
if pali:
    print("É um palindromo!")
else:
    print("Não é um palindromo")






