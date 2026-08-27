def produto_vetorial(a, b, c):
    """
    Calcula (b-a) × (c-a)
    a, b, c = tuplas (x, y)
    
    Retorna:
    > 0 → c está à ESQUERDA de a→b
    < 0 → c está à DIREITA de a→b
    = 0 → pontos são COLINEARES
    """
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

# Definir três pontos como tuplas (x, y)
a = (0, 0)
b = (1, 0)
c = (0, 1)

# Chamar a função
resultado = produto_vetorial(a, b, c)

print(resultado)
# Saída: 1 (positivo → c está à ESQUERDA de a→b)