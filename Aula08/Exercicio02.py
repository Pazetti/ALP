nasc=input("Insira sua data de nascimento no formato DD/MM/AAAA:")

inv=nasc.split('/')

print(f"Sua data de nascimento é {inv[2]}/{inv[1]}/{inv[0]}")