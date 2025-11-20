# pedir uma lista e alunos com duas notas, e mostra
# medias. e depois mostras separadamente quando acionado os alynos pedido.
nota1=nota2=media=0
alunos=[]
lista=[]
cont=cont2=1
print("DIGITE O NOME DOS ALUNOS E DUAS NOTAS \n(Digite FIM no nome para encerra)  ")
print("-="*15)
while True:
    aluno=input(f"Digite o nome do {cont}ª aluno:  ").strip().upper()
    cont += 1
    if aluno =="FIM":
        break
    nota1=float(input("Digite a 1ª nota: "))
    nota2=float(input('Digite a 2ª nota:  '))
    media=(nota2+nota1)/2
    alunos.append(aluno)
    alunos.append(media)
    alunos.append(nota1)
    alunos.append(nota2)
    lista.append(alunos[:])
    alunos.clear()

print("\nLista de alunos e médias: ")
print(f"{'Nª':<5}{'Aluno':<15}{'Média':>8}")
print("-" * 30)

for i, aluno in enumerate(lista,start=1):
    print(f"{i:<5}{aluno[0]:<15}{aluno[1]:>8.2f}")
while True:
    faluno=int(input("Mostra a nota de qual aluno ? (999 interromper):"))
    if faluno == 999:
        print("fim ... ")
        break
    if 1 <= faluno <= len(lista):
         print(f"Notas de {lista[faluno-1][0]} são {lista[faluno-1][2]} e {lista[faluno-1][3]}")
    else:
        print("Aluno não encontrado.")


print("fim")