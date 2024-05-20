def calcular_area_triangulo_retangulo(base, altura):
    # Calcula a área do triângulo retângulo
    area = 0.5 * base * altura
    return area

def main():
    # Solicita ao usuário o comprimento da base e da altura do triângulo
    base = float(input("Digite o comprimento da base do triângulo retângulo (em metros): "))
    altura = float(input("Digite a altura do triângulo retângulo (em metros): "))
    
    # Calcula a área
    area = calcular_area_triangulo_retangulo(base, altura)
    
    # Exibe o resultado
    print(f"A área do triângulo retângulo é {area:.2f} metros quadrados")

# Chama a função principal
if __name__ == "__main__":
    main()
