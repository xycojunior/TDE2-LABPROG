# Escreva um algoritmo que recebe um inteiro positivo e determina se é primo ou não.
numero = int(input("Digite um número inteiro positivo: "))

if numero <= 1:
    eh_primo = False
else:
    eh_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break

if eh_primo:
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
