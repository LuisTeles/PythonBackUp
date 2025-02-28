def busca_binaria(vetor, elemento):
    esquerda, direita = 0, len(vetor) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] == elemento:
            return True
        elif vetor[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return False

def main():
    vetor = []
    while True:
        numero = int(input())
        if numero == -1:
            break
        vetor.append(numero)
    
    vetor.sort()  # Garante que a lista esteja ordenada para a busca binária
    id_verificar = int(input())
    
    if busca_binaria(vetor, id_verificar):
        print("Possui acesso")
    else:
        print("Nao possui acesso")

if __name__ == "__main__":
    main()