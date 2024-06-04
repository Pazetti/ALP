from random import choice
p1=input("Insira o nome do primeiro jogador:")
p2=input("Insira o nome do segundo jogador:")

pe='Pedra'
t='Tesoura'
pa='Papel'
op=[pe,pa,t]

escolhap1=choice(op)
escolhap2=choice(op)

if escolhap1==pe and escolhap2==pa:
    print(f"{p1} tirou {escolhap1} e {p2} tirou {escolhap2}. {p2} é o vencedor")

elif escolhap1==pe and escolhap2==t:
    print(f"{p1} tirou {escolhap1} e {p2} tirou {escolhap2}. {p1} é o vencedor")

elif escolhap1==pa and escolhap2==pe:
    print(f"{p1} tirou {escolhap1} e {p2} tirou {escolhap2}. {p1} é o vencedor")

elif escolhap1==pa and escolhap2==t:
    print(f"{p1} tirou {escolhap1} e {p2} tirou {escolhap2}. {p2} é o vencedor")

elif escolhap1==t and escolhap2==pa:
    print(f"{p1} tirou {escolhap1} e {p2} tirou {escolhap2}. {p1} é o vencedor")

elif escolhap1==t and escolhap2==pe:
    print(f"{p1} tirou {escolhap1} e {p2} tirou {escolhap2}. {p2} é o vencedor")

elif escolhap1==t and escolhap2==t:
    print(f"{p1} tirou {escolhap1} e {p2} tirou {escolhap2}. Deu empate.")

elif escolhap1==pe and escolhap2==pe:
    print(f"{p1} tirou {escolhap1} e {p2} tirou {escolhap2}. Deu empate.")

elif escolhap1==pa and escolhap2==pa:
    print(f"{p1} tirou {escolhap1} e {p2} tirou {escolhap2}. Deu empate.")


