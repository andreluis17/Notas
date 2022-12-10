#Variavéis
          
lista_nomes = []

tri1 = []

tri2 = []

media = []

mediaR = []

Exibir = []

Exibir2 = []

Exibir3 = []

Exibir4 = []

contador = []

#Adicionar dados

#Número de alunos

alunos = int(input("Número de alunos: "))

#Adicionar alunos

while(len(lista_nomes) < alunos):
    lista_nomes.append(input("Insira um nome: ")), alunos +1 #Usar o Apend
    
#Adicionar nota1

while(len(tri1) < alunos): 
    for contador in range(alunos):
        tri1.append(input("Insira a nota do 1ºtri de " + lista_nomes[contador] + ": ")), alunos +1,

#Adicionar nota2
    
while(len(tri2) < alunos):
    for contador in range(alunos):
        resposta2 =tri2.append(input("Insira a nota do 2ºtri de " + lista_nomes[contador] + ": ")), alunos +1

#Calculo

while(len(media) < alunos): 
    for contador in range(alunos):
        #', '.join(tri1)
        ', '.join(map(str, tri1))
        bd2 = str(tri1[contador]).strip('[]')
        #', '.join(tri2)
        ', '.join(map(str, tri1))
        bd = str(tri2[contador]).strip('[]')
        ntri1 = int(bd2)
        ntri2 = int(bd)
        calculo = (ntri1 + ntri2)/2
        media.append(calculo)

#Exibir

for contador in range(alunos):
   tupla=(tri1[contador],tri2[contador])
   Exibir.append(tupla)
   tupla2=(lista_nomes[contador],Exibir[contador])
   Exibir2.append(tupla2)
   tupla3=(Exibir2[contador],media[contador])
   Exibir3.append(tupla3)
   nota = str(Exibir3[contador][1]).strip('[]')
   ', '.join(map(str, Exibir3))
   recuperacao = float(nota)
print(Exibir3)

#Recuperação

pergunta = input("Deseja ver os alunos de recuperação? ")

if "sim" in pergunta:
    for contador in range(alunos):
     if Exibir3[contador][1] < 6:
        print(Exibir3[contador])
     else:
        print("")
else:
    print("Suave")
    