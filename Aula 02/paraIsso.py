# Entrada de Dados
n = int(input("Quantos números você vai digitar? R: "))
# Processamento de dados
for i in range(n):
    numero = int(input("Digite um número: "))
    # Verificar se é IMPAR ou PAR
    if numero < 0:
        print("NEGATIVO")
    elif numero > 0:
        print("POSITIVO")
    else:
        print("NULO")
        continue
    if (numero % 2 == 0):
        print("PAR")
    elif (numero % 2 != 0):
        print("IMPAR")