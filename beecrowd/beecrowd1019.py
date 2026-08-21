N = int(input())

# N // 60 = minutos
#Se o minuto > 60 eu // 60
#Segundo: N%60
horas = 0
minutos = N//60
if minutos > 60:
    horas = minutos//60
    minutos = minutos % 60

segundos = N % 60

print(f'{horas}:{minutos}:{segundos}')