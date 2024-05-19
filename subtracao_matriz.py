# Passo 1: Inicializar as Matrizes
matriz1 = [
    [1.0, 2.0, 3.0, 4.0],
    [5.0, 6.0, 7.0, 8.0],
    [9.0, 10.0, 11.0, 12.0]
]

matriz2 = [
    [12.0, 11.0, 10.0, 9.0],
    [8.0, 7.0, 6.0, 5.0],
    [4.0, 3.0, 2.0, 1.0]
]

# Passo 2: Subtrair as Matrizes
resultado = [
    [0.0, 0.0, 0.0, 0.0],  # linha 1
    [0.0, 0.0, 0.0, 0.0],  # linha 2
    [0.0, 0.0, 0.0, 0.0]   # linha 3
]

for i in range(3):  # Para cada linha
    for j in range(4):  # Para cada coluna
        resultado[i][j] = matriz1[i][j] - matriz2[i][j]

# Passo 3: Exibir o Resultado
print("Resultado da Subtração das Matrizes:")
for linha in resultado:
    print(linha)
