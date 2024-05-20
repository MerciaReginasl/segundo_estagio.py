# Dado um string que pode conter a letra 'p', imprima o índice da
# segunda ocorrência de 'p'. Se a letra 'p' ocorrer apenas uma
# vez, imprima -1. Se a string não contiver a letra 'p' imprima -2.

texto = input("Informe o texto com ou sem letras 'p': ")
posicao = texto.find("p")
if posicao == -1:
    print(-2)
else:
    posicao = posicao + 1
    while posicao != len(texto)-1 and texto[posicao] != "p":
        posicao += 1
    if posicao == len(texto)-1:
        print(-1)
    else:
        print(posicao)
