# Função principal do programa
def main():
    # Passo 1: Inicializar e ler o vetor de 20 elementos
    vetor = []
    print("Digite 20 números inteiros:")
    for i in range(20):
        numero = int(input(f"Elemento {i+1}: "))
        vetor.append(numero)
    
    # Passo 2: Ler o valor de N
    N = int(input("Digite um número inteiro N: "))
    
    # Passo 3: Contar os elementos iguais a N
    contagem = 0
    for elemento in vetor:
        if elemento == N:
            contagem += 1
    
    # Passo 4: Mostrar o resultado
    print(f"Existem {contagem} elementos no vetor iguais a {N}.")

# Chamada da função principal
if __name__ == "__main__":
    main()
