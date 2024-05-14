from funcoes import valida_data

data = input("Insira sua data de nascimento no formato (DD/MM/AAAA):")
nova_data = data.split("/")
dia = int(nova_data[0])
mes = int(nova_data[1])
ano = int(nova_data[2])

if valida_data(ano, mes, dia):
    print(valida_data(ano,mes,dia))
else:
    print("Formato de data invalido. Digite novamente.")
    print(valida_data(ano, mes, dia))