#Escreva um algoritmo que recebe um número inteiro positivo, o mesmo deverá retornara soma de todos os pares

numero = int(input("Digite um número: "))
soma = 0
for i in range(2, numero + 1, 2):
        soma += i
print("A soma de todos os números pares até", numero, "é:", soma)