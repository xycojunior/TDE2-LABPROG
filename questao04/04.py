#Escreva um algoritmo que solicite ao usuário que insira uma senha. Se a senha estivercorreta (por exemplo, "senha123"), o programa deve exibir uma mensagem deboas-vindas. Caso contrário, o usuário tem mais duas tentativas. Se a senha estivererrada nas três tentativas, o programa deve exibir uma mensagem de erro e encerrar

senhaCorreta = "senha123"

for tentativas in range(3):
    senhaDigitada = input("Digite a senha de acesso: ")
    if senhaDigitada == senhaCorreta:
        print("Seja bem-vindo!")
        break
    else:
        resto = 2 - tentativas
        if resto > 0:
            print("Senha incorreta, você tem mais", resto, "tentativa(s).")
        else:
            print("Você esgotou o número de tentativas! Acesso negado!")
