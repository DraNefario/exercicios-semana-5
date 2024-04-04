nota_valida = False  
while not nota_valida:
    nota = float(input("Digite a nota do aluno: "))  
    if nota >= 7:  
        nota_valida = True  
    else:
        print("A nota inserida não é válida. Por favor, insira uma nota maior que 7.")
print("A nota válida do aluno é:", nota)