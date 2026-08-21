n1, n2, n3, n4 = map(float, input().split())

media = ((n1*2) + (n2*3) + (n3*4) + n4) / 10

print(f"Media: {media:.1f}")

if media >=7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif media >= 5 and media <=6.9:
    print("Aluno em exame.")
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    media = (media + exame)/2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f'Media final: {media:.1f}')
