while True:
    idade=input("Insira sua idade:")
    if idade.isdigit():
        idade=int(idade)
        break
    else:
        print("ERRO!!!")
        print("Insira somente numeros.")