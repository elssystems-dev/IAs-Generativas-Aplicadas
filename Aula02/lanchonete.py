produtos = {
    1 : 5.00,
    2 : 3.50,
    3 : 4.80,
    4 : 8.90,
    5 : 7.32
}

codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade de produto a ser comprada: "))
try:
    print(f"O valor total da compra é de {produtos[codigo] * quantidade}")
except KeyError:
    print("Valor inválido. Use 1 a 5.")