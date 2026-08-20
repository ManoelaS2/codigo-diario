cod, qtd = map(int, input().split())

if cod == 1:
    saida = f'Total: R$ {qtd*4:.2f}'
elif cod == 2:
    saida = f'Total: R$ {qtd*4.5:.2f}'
elif cod == 3:
    saida = f'Total: R$ {qtd*5:.2f}'
elif cod == 4:
    saida = f'Total: R$ {qtd*2:.2f}'
else:
    saida = f'Total: R$ {qtd*1.5:.2f}'

print(saida)