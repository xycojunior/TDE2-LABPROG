#Escreva um algoritmo que solicite ao usuário um número inteiro positivo. Em seguida, o programa deve calcular e exibir a soma de todos os números inteiros de 1 até o número fornecido pelo usuário.

num = int(input("Digite um valor inteiro: "))
contador = 0
soma = 0
while contador <= num:
        soma += contador
        contador += 1

print("A soma de todos os números inteiros de 1 até", num, "é:", soma)