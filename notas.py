#Feito por André Luis & Gabriel Maciel

#Variavéis
          
lista_nomes = []

tri1 = []

tri2 = []

media = []

mediaR = []

recuperacao = []

Exibir = []

Exibir2 = []

Exibir3 = []

Exibir4 = []

Exibir5 = []

Exibir6 = []

Exibir7 = []

Exibir8 = []

Exibir9 = []

Exibir10 = []

Exibir11 = []

contador = []

#Adicionar dados

#Número de alunos

while True:
    try: 
        alunos = int(input("Número de alunos: "))    #Try e except  são um metodo para tratar erro
        break
    except ValueError:
        print("Digite um valor numérico")

print("")
print("Digite os alunos da chamada: ")
print("")

#Adicionar alunos

while(len(lista_nomes) < alunos):
    addaluno = lista_nomes.append(str(input("Insira um nome: "))), alunos +1 #O appende adiciona algo no fim da lista
else:
    print("")
    print("Digite as notas do 1ºTrimestre")
    print("")


#Adicionar nota1


while(len(tri1) < alunos):
    try:
        for contador in range(alunos):
            addnota =  tri1.append(int(input("Insira a nota do 1ºtri de " + lista_nomes[contador] + ": "))), alunos +1
        break
    except ValueError:
        print("Digite um valor numérico de 1 a 10")

print("")
print("Digite as notas do 2ºTrimestre")
print("")

#Adicionar nota2

while(len(tri2) < alunos):
    try:
        for contador in range(alunos):
            addnota2 = tri2.append(int(input("Insira a nota do 2ºtri de " + lista_nomes[contador] + ": "))), alunos +1
        break
    except ValueError:
        print("Digite um valor numérico de 1 a 10")

#Calculo

while(len(media) < alunos): 
    for contador in range(alunos): #Estrutura de repetição
        ', '.join(map(str, tri1))
        conversor3 = str(tri1[contador]).strip('[]') #Tira os conchetes
        ', '.join(map(str, tri2))
        conversor4 = str(tri2[contador]).strip('[]') #Tira os conchetes
        ntri1 = float(conversor3)
        ntri2 = float(conversor4)
        calculo = (ntri1 + ntri2)/2 #Calcula a média
        media.append(calculo)

#Exibir

for contador in range(alunos):
   tupla=(tri1[contador],tri2[contador])
   Exibir.append(tupla)
   tupla2=(lista_nomes[contador],Exibir[contador])
   Exibir2.append(tupla2)
   tupla3=(Exibir2[contador],media[contador])
   Exibir3.append(tupla3)
   if Exibir3[contador][1] < 6:
        Exibir4.append(Exibir3[contador])
        Exibir11.append(Exibir2[contador])         
   else:
        Exibir5.append(Exibir3[contador])

print("")
print("Pré-Aprovados:")
print("")
print(Exibir5)

print("")
print("Recuperação")
print("")
print(Exibir4)
print("")
   
#Recuperação / Olha porque não está mostrando a tabela de reprovados 

pergunta = str(input("Está ciente de todas as notas e as conferiu? "))
print("")
if "sim" in pergunta: #IF ELSE 1
    alunoR = len(Exibir4)
    pergunta2 = str(input("Deseja adicionar as notas de recuperação? "))
    print("")
    if "sim" in pergunta2: #IF ELSE 2
        for contador in range(alunoR):
            print(Exibir4[contador])
            pergunta3 = str(input("Este aluno fez a recuperação? "))
            print("")
            if "sim" in pergunta3:  #IF ELSE 3
                pergunta4 = recuperacao.insert(contador,str(input("Digite a nota de recuperação: ")))
                print("")
                ', '.join(map(str, tri1))
                conversor6 = str(tri1[contador]).strip('[]') #Tira os conchetes
                ', '.join(map(str, tri2))
                conversor7 = str(tri2[contador]).strip('[]') #Tira os conchetes
                ', '.join(map(str, recuperacao))
                conversor8 = str(recuperacao[contador]).strip('[]') #Tira os conchetes
                ntri3 = float(conversor6)
                ntri4 = float(conversor7)
                nrecuperacao = float(conversor8)
                notaR = (ntri3 + ntri4 + nrecuperacao)/3
                mediaR.append(notaR)
                tupla4 = (Exibir11[contador],recuperacao[contador])
                Exibir6.append(tupla4)
                tupla5 = (Exibir6[contador],mediaR[contador])
                Exibir7.append(tupla5)
                if Exibir7[contador][1] < 6: #IF ELSE 4
                    Exibir8.append(Exibir7[contador])         
                else: #IF ELSE 4
                    Exibir9.append(Exibir7[contador])
            else: #IF ELSE 3
                #Esta parte é só para adicionar itens para o contador não falhar
                recuperacao.append(Exibir4[contador])
                Exibir6.append(Exibir4[contador])
                mediaR.append(Exibir4[contador][1])
                Exibir7.append(Exibir4[contador])
                Exibir8.append(Exibir7[contador])
                print("Proximo aluno")
                print("")
    else: #IF ELSE 2
        print("Até a proxima")
        print("")
        print("Aprovados: ")
        print("")
        print(Exibir5)
        print("")
        print("Reprovados: ")
        print("")
        print(Exibir4)
        print("")
else: #IF ELSE 1
    print("Até a proxima")
    print("")
    print("Aprovados: ")
    print("")
    print(Exibir5)
    print("")
    print("Reprovados: ")
    print("")
    print(Exibir4)
    print("")

print("Aprovados: ")
print("")
print(Exibir5, Exibir9)
print("")
print("Reprovados: ")
print("")
print(Exibir8, Exibir10)
print("")