
N = int(input("Digite um número inteiro positivo: "))
if N <= 0:
    print("O número fornecido não é válido. Por favor, insira um número inteiro positivo.")
else:
  soma = 0
  i = 1
  while i <= N:
        soma += i
        i += 1
  print("O somatório dos", N, "primeiros números inteiros a partir de 1 é:", soma)
