def produto_escalar(matriz, escalar):
    # Inicializa a matriz resultado com o mesmo tamanho da matriz original
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = [[0.0 for _ in range(colunas)] for _ in range(linhas)]
    
    # Percorre cada elemento da matriz e multiplica pelo escalar
    for i in range(linhas):
        for j in range(colunas):
            resultado[i][j] = matriz[i][j] * escalar
            
    return resultado

# Exemplo de uso da função
matriz_exemplo = [
    [1.0, 2.0, 3.0, 4.0],
    [5.0, 6.0, 7.0, 8.0],
    [9.0, 10.0, 11.0, 12.0]
]

escalar = 2.0

resultado = produto_escalar(matriz_exemplo, escalar)

print("Resultado da Multiplicação da Matriz pelo Escalar:")
for linha in resultado:
    print(linha)
