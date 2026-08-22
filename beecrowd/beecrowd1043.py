A, B, C = map(float, input().split())

#Para formar um triângulo cada lado deve ser menor que a soma dos outros dois

if A < B+C and B < A+C and C < A+B:
    print(f'Perimetro = {A+B+C:.1f}')
else:
    print(f'Area = {((A + B)*C)/2:.1f}')