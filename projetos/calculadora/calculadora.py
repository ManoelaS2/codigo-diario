import math

def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b == 0:
        return "Não é possível dividir por 0"
    return a/b

def potencia(a,b):
    resultado = a**b
    return resultado

def raiz_quadrada(a):

    try:
        resultado = math.sqrt(a)
    except:
        resultado = 'Erro'
    return resultado

def porcentagem(a,b):
    resultado = (a*b)/100
    return resultado

def resto(a,b):
    resultado = a%b
    return resultado



print(soma(20,4))
print(divisao(4,0))
print(raiz_quadrada(-4))
print(porcentagem(20,10))
print(resto(10,3))
print(potencia(2,3))