def fibonacci_ate_n(n):
    # Lista para armazenar os números de Fibonacci
    fib_sequence = []
    
    # Os dois primeiros números de Fibonacci
    a, b = 0, 1
    
    # Adiciona os números de Fibonacci à lista até que o próximo número seja maior que n
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    
    return fib_sequence

def main():
    # Lê o valor de n
    n = int(input("Digite um número de Fibonacci n: "))
    
    # Obtém a sequência de Fibonacci até n
    fib_sequence = fibonacci_ate_n(n)
    
    # Imprime a sequência de Fibonacci até n
    print("Sequência de Fibonacci até", n, ":", " ".join(map(str, fib_sequence)))

# Chama a função principal
if __name__ == "__main__":
    main()
