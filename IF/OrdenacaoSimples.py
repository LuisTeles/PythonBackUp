# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
# Entrada

# A entrada contem três números inteiros.
# Saída

# Imprima a saída conforme foi especificado.


# Read three integer values from input
numbers = [int(input("Enter a number: ")) for _ in range(3)]#input an array

# Copy the list to preserve the original order for later display
original_order = numbers[:]

# Bubble sort algorithm to sort the list in ascending order
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            # Swap if the current element is greater than the next
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Print the sorted values
for num in numbers:
    print(num)

# Print a blank line
print()

# Print the original values in the original order
for num in original_order:
    print(num)
