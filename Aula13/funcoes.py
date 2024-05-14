def valida_data():
    from datetime import datetime
    data = input("Digite sua data de nascimento: (dd/mm/aaaa)")
    nova_data = data.split("/")
    dia = int(nova_data[0])
    mes = int(nova_data[1])
    ano = int(nova_data[2])

    hoje = datetime.now().date()
    data_nasc = datetime(ano, mes, dia).date()
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
    if idade >= 18:
        return True
    else:
        return False


def exibir_menu():
    print('Menu')
    print('1 - Cadastrar')
    print('2 - Exibir Frase')
    print('3 - Sair')
    opcao =int(input('Escolha uma opção do menu: '))
    return opcao

def validar_cpf(cpf = str):
    if len(cpf) == 11 and str.isdigit(cpf):
        soma = 0
        resto = 0

        nove_digitos = cpf[0:9]
        primeiro_verificador = (cpf[9:10])
        segundo_verificador = (cpf[10:11])
        descrescente = 11

        for i in nove_digitos:
            soma_antiga = soma
            descrescente -= 1
            soma += (int(i) * descrescente)

        resto = soma % 11
        if resto < 2 and int(primeiro_verificador) == 0:
            pass
        else:
            if 11-resto == int(primeiro_verificador):
                pass
            else:
                return False

        soma = 0
        resto = 0
        descrescente = 12

        for i in nove_digitos + primeiro_verificador:
            descrescente -= 1
            soma += (int(i) * descrescente)
        resto = soma % 11
        if resto < 2 and int(segundo_verificador) == 0:
            return True
        else:
            if 11-resto == int(segundo_verificador):
                return True

    else:
        return False


