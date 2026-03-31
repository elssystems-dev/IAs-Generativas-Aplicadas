# Código 1 - Idade em Anos, Meses e Dias

#---- Entrada de dados -------#
dias = int(input("Digite a quantidade de dias: "))

#----Processamento de dados-----#
anos = dias // 365 # Calculo para saber a quantidade de anos
meses = (dias % 365) // 30 # Meses
dias = (dias % 365) % 30 # Dias restantes

#----Saída de Dados----#
print(f"Você possui {anos} anos, {meses} meses e {dias} dias de vida.")

