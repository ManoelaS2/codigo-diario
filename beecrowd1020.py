N = int(input())

# N//365 = ano
ano = N//365 
mes = (N - (365*ano)) // 30
dia = (N - (365*ano)) % 30

print (ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")