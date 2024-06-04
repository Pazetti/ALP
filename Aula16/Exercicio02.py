arquivo=open("idades.txt", "r", encoding="utf-8")

linhas=arquivo.readlines()
idades=[]
sexos=[]

total_idades=0.0
for linha in linhas:
    campos=linha.split(",")
    idade=int(campos[0])
    sexo=campos[1]
    idades.append(idade)
    sexos.append(sexo[0])
    total_idades+=idade
nf=0
nm=0
tif=0
tim=0
for i in range(len(idades)):
    if sexos[i]=='F':
        nf+=1
        tif+=idades[i]
    else:
        nm+=1
        tim+=idades[i]

mediaf=tif/nf
mediam=tim/nm
print(f"o total de mulheres é {nf}, e a media de idade delas é {mediaf}. O total de homens é {nm}, e a media de suas idades é {mediam}.")