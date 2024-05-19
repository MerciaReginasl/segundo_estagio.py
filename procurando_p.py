#Pergunta - Dada uma string que pode conter a letra p (minúscula). Imprima o índice
#da segunda ocorrência de p. Se a letra p ocorrer apenas uma vez, imprima -1 e, se a
#string não contiver a letra p, imprima -2.
#Resposta:
def indice_segunda_ocorrencia_p(string):
primeira_ocorrencia = string.find('p')
if primeira_ocorrencia == -1:
return -2
segunda_ocorrencia = string.find('p', primeira_ocorrencia + 1)
return segunda_ocorrencia if segunda_ocorrencia != -1 else -1

# Testando a função com uma string de exemplo
string_exemplo = "palavra com duas letras p"
print("Índice da segunda ocorrência de 'p':",
indice_segunda_ocorrencia_p(string_exemplo)).
