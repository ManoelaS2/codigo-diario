numeros = []
p = 0
soma = 0
for i in range(6):
    numeros.append(float(input()))
    if numeros[i] > 0:
        p += 1
        soma = (numeros[i] + soma) 

media = soma/p    
print(f'{p} valores positivos')
print(f'{media:.1f}')