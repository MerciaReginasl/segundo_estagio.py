def verificar_ordem_crescente(x):
    # Extrai os três dígitos componentes
    digito1 = x // 100  # Centena
    digito2 = (x // 10) % 10  # Dezena
    digito3 = x % 10  # Unidade
    
    # Verifica se os dígitos estão em ordem crescente
    if digito1 < digito2 < digito3:
        return "SIM"
    else:
        return "NÃO"

def main():
    # Lê o número inteiro de três dígitos
    x = int(input("Digite um número inteiro de três dígitos: "))
    
    # Verifica se o número tem exatamente três dígitos e os dígitos são diferentes
    if 100 <= x <= 999:
        # Chama a função para verificar a ordem dos dígitos
        resultado = verificar_ordem_crescente(x)
        print(resultado)
    else:
        print("O número deve ter exatamente três dígitos e todos diferentes.")

# Chama a função principal
if __name__ == "__main__":
    main()
