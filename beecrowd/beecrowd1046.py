c , f = map(int, input().split())
duracao = 0
if c > f:
   duracao = (f+24) - c
elif f > c:
    duracao = f - c
elif c == f:
    duracao = 24

print(f'O JOGO DUROU {duracao} HORA(S)')