numeros = list(map(int, input().split()))[:3] #usar map com lista e limmitar ate 3 numeros
originais = numeros.copy() #copia a lista originaç
numeros.sort() #deixa ordenado
for numero in numeros:
    print(numero)

print()

for original in originais:
    print(original)