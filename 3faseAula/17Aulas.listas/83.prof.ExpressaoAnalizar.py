expr = str(input("Digite a expressao: "))
#(9*(45/5)(8/(2+2)*9)(7+6))
pilha = []
for simb in expr:
    if simb == "(":
        pilha.append("(")
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressao esta Válida")
else:
    print('Sua expressao esta Inválida')