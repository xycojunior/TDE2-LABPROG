#Calcular e mostrar a média aritmética dos números pares compreendidos entre 23 e483

soma = 0 
quantidade = 0

for numero in range(23, 484):
    if numero % 2 == 0:
        soma += numero
        quantidade += 1
if quantidade > 0:
    media = soma / quantidade
    print("A média aritmética dos números pares entre 23 e 483 é:", media)
else:
    print("Não há números pares entre 23 e 483.")
