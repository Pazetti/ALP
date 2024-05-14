import random
from funcoes import exibir_menu
from funcoes import validar_cpf

op = exibir_menu()

if op == 1:
    print("1")
    input("Digite seu nome:")
    input("Digite seu sobrenome:")
    while (not validar_cpf(cpf)):
    cpf=str(input("Insira seu CPF no formato (xxxxxxxxxxx): "))

    input("Insira sua data de nascimento no formato (DD/MM/AAAA): ")

    float(input("Insira sua renda bruta: "))

elif op == 2:
    frases = ["A persistência realiza o impossível", "Seus sonhos não precisam de plateia, eles só precisam de você", "A persistência é o caminho do êxito", "No meio da dificuldade encontra-se a oportunidade"]
    escolhido=random.choice(frases)
    print(escolhido)

elif op == 3:
    print("Bye Bye.")

else:
    print("Opção invalida")
    exibir_menu()
