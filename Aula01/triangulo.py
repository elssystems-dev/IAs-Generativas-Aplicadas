# Entrada de dados
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if ((a + b) > c and (b + c) > a and (c + a) > b):
    print("Triângulo válido!!!!!!!!!!!!!!!!!!!!!!!!!!")
    perimetro = a + b + c # Processamento de dados 1
    print(f"O perímetro do triângulo é {perimetro}") # Saída de dados 1
else:
    print("Forma trapézio!!!!!!!!!!!!!!!!")
    area = ((a+b) * c) / 2 # Processamento de dados 2
    print(f"A área do trapézio é de {area}") # Saída de dados 2
print("FIM do pogama")

