frase=str(input("Insira a frase:"))
quantia=0
for letra in frase:
    if letra in 'aeiouAEIOUãÃíÍóÓúÚáÁéÉàÀüÜ':
        quantia=quantia+1

print(f"O numero de vogais é:{quantia}")