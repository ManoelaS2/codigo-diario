A,B,C,D = map(int, input().split())

if A % 2 == 0 and C > 0 and D > 0:
    if B > C and D > A:
        somaCD = C + D
        somaAB = A + B
        if somaCD > somaAB:
            print("Valores aceitos")
        else: 
            print("Valores nao aceitos")
    else:
       print("Valores nao aceitos") 
else:
    print("Valores nao aceitos")