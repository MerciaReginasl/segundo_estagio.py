# Faça um programa que escreva por extenso uma data fornecida no
# formato dd/mm/aaaa. O programa usa duas funções: uma que recebe
# o número do mês e retorna o nome do mês e outra que recebe
# dia, mês e ano, e retorna a data por extenso, usando a função
# descrita anteriormente.

# Função que retorna o mês por extenso
def mes_por_extenso(mes):
meses = "janeiro,fevereiro,março,abril,maio,junho," + \
       "julho,agosto,setembro,outubro,novembro,dezembro"
mes_extenso = meses.split(",")
return mes_extenso[mes-1]

# Função que retorna a data por extenso
def data_por_extenso(dia, mes, ano):
return str(dia)+" de "+mes_por_extenso(mes)+" de "+str(ano)

# Função principal
def principal():
data = input("Informe uma data no formato dd/mm/aaaa: ").\
           split("/")
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
print(data_por_extenso(dia, mes, ano))

# Programa principal
principal()
