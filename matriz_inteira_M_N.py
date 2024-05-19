def ler_matriz(M, N):
    # Inicializa a matriz vazia
    matriz = []
    
    # Lê os valores para cada linha da matriz
    for i in range(M):
        linha = input(f"Digite os {N} elementos da linha {i+1}, separados por espaços: ")
        elementos = list(map(int, linha.split()))
        
        # Verifica se a quantidade de elementos digitados é igual a N
        if len(elementos) != N:
            print(f"Erro: você deve digitar exatamente {N} elementos.")
            return None
        
        # Adiciona a linha na matriz
        matriz.append(elementos)
    
    return matriz

# Exemplo de uso da função
def main():
    M = int(input("Digite o número de linhas M da matriz: "))
    N = int(input("Digite o número de colunas N da matriz: "))
    
    matriz = ler_matriz(M, N)
    
    if matriz:
        print("Matriz lida:")
        for linha in matriz:
            print(" ".join(map(str, linha)))

# Chamada da função principal
if __name__ == "__main__":
    main()
