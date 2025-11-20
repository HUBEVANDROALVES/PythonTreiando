##faca um programa  que leia nome e media de um aluno,
##guardando támbem se aprovado ou nao. NO FINAL MOSTRA O CONTEUDO NA TELA
##
aluno={}#criar um dicionario vazio
resultado=[]#criar uma lista vazia
for c in range(0,3):
    aluno["nome"]=str(input("Nome do Aluno: "))
    aluno["media"]=float(input("Media  do aluno: "))
    if aluno["media"] >= 6:
        aluno["situacao"]="Aprovado"
    else:
        aluno["situacao"]="Reprovado"
    resultado.append(aluno.copy())
for e in resultado:
    for k, v in e.items():
        print(f"O Campo  {k} tem o valor {v}.")
#print(aluno)