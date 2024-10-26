# problem

# Leia 4 valores inteiros A, B, C e D. Então, se B for maior que C e D for maior que A e se a soma de C e D for maior que a soma de A e B e se C e D forem valores positivos e se A for par, escreva a mensagem “Valores aceitos”. Caso contrário, escreva a mensagem “Valores nao aceitos”.
# Entrada

# Quatro números inteiros A, B, C e D.
# Saída

# Mostre a mensagem correspondente após a validação dos valores​​.




# Reading four integer values A, B, C, and D from input
A = int(input("Enter value for A: "))
B = int(input("Enter value for B: "))
C = int(input("Enter value for C: "))
D = int(input("Enter value for D: "))

# Checking the conditions
if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

