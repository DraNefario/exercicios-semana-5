numeros_pares = 0
numeros_impares = 0
contador = 0
while contador < 10:
    numero = int(input(f"Digite o {contador+1}º número: "))
    
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
    
    contador += 1
print("Quantidade de números pares:", numeros_pares)
print("Quantidade de números ímpares:", numeros_impares)
