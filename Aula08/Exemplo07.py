nome=input("Digite seu nome completo:")
nasc=input('Digite a data do seu nascimento <DD/MM/AAAA>:')
data=nasc.split('/')
palavras=nome.split()
pre_nome=palavras[0]
sobrenome=palavras[1]
print(f"Olá {pre_nome} quero que voce se foda junto com seu sobrenome {sobrenome}")
print(f"Voce nasceu no dia {data[0]} do mês {data[1]}, que merda de data em")