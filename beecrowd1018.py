v = int(input())
print(v)
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0 
notas1 = 0

if v >= 100:
    notas100 = v//100
    v = v%100
if v >=50:
    notas50 = (v%100)//50
    v = v%50
if v >= 20:
    notas20 = v//20
    v = v%20
if v >= 10:
    notas10 = v//10
    v = v%10
if v >= 5:
    notas5 = v//5
    v = v%5
if v >= 2:
    notas2 = v//2
    v = v%2
if v >= 1:
    notas1 = v//1

print(f'{notas100} nota(s) de R$ 100,00')
print(f'{notas50} nota(s) de R$ 50,00')
print(f'{notas20} nota(s) de R$ 20,00')
print(f'{notas10} nota(s) de R$ 10,00')  
print(f'{notas5} nota(s) de R$ 5,00')  
print(f'{notas2} nota(s) de R$ 2,00')
print(f'{notas1} nota(s) de R$ 1,00')