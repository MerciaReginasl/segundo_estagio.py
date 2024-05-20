def imprimir_escada(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')  # Imprime o número sem espaço e sem quebra de linha
        print()  # Quebra de linha após cada degrau

def main():
    # Lê o valor de n
    n = int(input("Digite um número inteiro n (n ≤ 9): "))
    
    # Verifica se n está no intervalo permitido
    if 1 <= n <= 9:
        imprimir_escada(n)
    else:
        print("O número deve estar entre 1 e 9.")

# Chama a função principal
if __name__ == "__main__":
    main()
