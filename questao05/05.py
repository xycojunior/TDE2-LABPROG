#Escreva um programa que leia 10 valores e escreva a soma do maior valor com o menor valor.

valores = []

for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

maior_valor = max(valores)
menor_valor = min(valores)

soma_maior_menor = maior_valor + menor_valor
print(f"A soma do maior valor ({maior_valor}) com o menor valor ({menor_valor}) é: {soma_maior_menor}")
