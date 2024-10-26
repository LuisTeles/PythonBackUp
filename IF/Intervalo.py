# problem

# Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

# O símbolo ( representa "maior que". Por exemplo:
# [0,25]  indica valores entre 0 e 25.0000, inclusive eles.
# (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000.
# Entrada

# O arquivo de entrada contém um número com ponto flutuante qualquer.
# Saída

# A saída deve ser uma mensagem conforme exemplo abaixo.


# Exemplos de entrada      	
# 25.01 	
# 25.00 	
# 100.00 	 
# -25.02

# Exemplos de saída

# Intervalo (25,50]
# Intervalo (75,100]
# Intervalo [0,25]
# Fora de intervalo

# Read a floating-point number from input
value = float(input("Enter a value: "))

# Check which interval the value belongs to and print the appropriate message
if 0 <= value <= 25:
    print("Intervalo [0,25]")
elif 25 < value <= 50:
    print("Intervalo (25,50]")
elif 50 < value <= 75:
    print("Intervalo (50,75]")
elif 75 < value <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")

