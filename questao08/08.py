#Imprimir a tabuada de qualquer número n.

num = int(input("Digite um número: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)