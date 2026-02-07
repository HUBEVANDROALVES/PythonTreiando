#crie um programa que leia nome, ano de nascimento e CTPS.
# Registra como idade
# se CTPS for diferente de zero receber Ano de contratacao e o salario
# calcular idade e com quantos anos vai se aposentar.


from datetime import datetime

dados = dict()
dados['nome']=input("Digite o nome: ")
nasc =int(input("Digite a ano de nascimento (aaaa): "))
dados['idade'] = datetime.now().year - nasc
dados['CTPS']=int(input("Digite o numero da Carteira de trabalho(0 se não tiver):"))

if dados['CTPS'] != 0:
    dados["contratação"] = int(input( 'Ano de Contratação'))
    dados['Salario'] = float(input( 'Salário '))
    dados[ 'Aposetadoria'] = dados['idade']+ ((dados["contratação"]+35) - datetime.now().year)
print("-=" * 30)
for k, v in dados.items():
    print(f' -{k} tem o valor:  {v}')
#print(dados)



