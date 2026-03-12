print("Digite a largura do retângulo: ", end='', flush=True)
largura = float(input())
print("Digite a altura do retângulo: ", end='', flush=True)
altura = float(input())
area = altura * largura
perimetro = largura * 2 + altura * 2
diagonal = largura ** 2 + altura ** 2 ** 0.5
print("A área do retângulo é de " + str(area) + " --- O perímetro é de " + str(perimetro) + " --- A diagonal é de " + str(diagonal))
