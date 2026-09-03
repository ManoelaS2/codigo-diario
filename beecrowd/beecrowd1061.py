dia1 = int(input().split()[1])
h1, m1, s1 = map(int, input().split(" : "))

dia2 = int(input().split()[1])
h2, m2, s2 = map(int, input().split(" : "))

segundos1 = (dia1*24*60*60) + (h1*60*60) + (m1*60) + s1
segundos2 = (dia2*24*60*60) + (h2*60*60) + (m2*60) + s2

duracao = segundos2 - segundos1

dias = duracao//(24*60*60)
resto = duracao%(24*60*60)

horas = resto//(60*60)
resto = resto%(60*60)

minutos = resto//(60)
resto = resto%(60)

segundos = resto

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
