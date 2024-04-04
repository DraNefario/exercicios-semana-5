soma = 0  
contador = 0 
continuar = True  
while continuar:
    numero = float(input("Digite um número: ")) 
    if numero <= -1:  
        continuar = False 
    else:
        soma += numero  
        contador += 1   
if contador == 0:
    print("Nenhum número foi fornecido.")
else:
    media = soma / contador  
    print("A média dos números fornecidos é:", media)
