salario = float(input())

if salario <= 400:
    novo = salario + (salario * 0.15)
    reajuste = salario * 0.15
    percentual = 15
elif salario <= 800:
    novo = salario + (salario * 0.12)
    reajuste = salario * 0.12
    percentual = 12  
elif salario <= 1200:
    novo = salario + (salario * 0.10)
    reajuste = salario * 0.10
    percentual = 10
elif salario <= 2000:
    novo = salario + (salario * 0.07)
    reajuste = salario * 0.07
    percentual = 7
else:
    novo = salario + (salario * 0.04)
    reajuste = salario * 0.04
    percentual = 4

print(f"Novo salario: {novo:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")