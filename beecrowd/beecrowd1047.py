# Tempo de Jogo com Minutos
hi, mi, hf, mf = map(int, input().split())
duracaomin = 0
duracaohoras = 0
ihi, mi, hf, mf = map(int, input().split())

duracaomin = 0
duracaohoras = 0

if hf > hi:
    duracaohoras = hf - hi
    if mf < mi:
        duracaohoras = duracaohoras - 1
        duracaomin = (mf + 60) - mi
    else:
        duracaomin = mf - mi
elif hf < hi:
    duracaohoras = (hf + 24) - hi

    if mf < mi:
        duracaohoras = duracaohoras - 1
        duracaomin = (mf + 60) - mi
    else:
        duracaomin = mf - mi
elif hf == hi:
    if mf > mi:
        duracaohoras = 0
        duracaomin = mf - mi
    elif mf < mi:
        duracaohoras = 23
        duracaomin = (mf + 60) - mi
    else:
        duracaohoras = 24
        duracaomin = 0

print(f'O JOGO DUROU {duracaohoras} HORA(S) E {duracaomin} MINUTO(S)')
#Era mais fácil transformar em minutos e depois em horas dnv 