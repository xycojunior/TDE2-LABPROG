#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem casoo valor seja inválido e continue pedindo até que o usuário informe um valor válido
while True: 
    nota = int(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print("Nota válida")
    else: 
        print("Nota inválida, digite novamente!")