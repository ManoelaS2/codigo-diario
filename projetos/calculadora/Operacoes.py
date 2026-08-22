import math
class Operacoes:
    def calcular_soma(self, a,b):
        return a+b

    def calcular_subtracao(self, a,b):
        return a-b

    def calcular_multiplicacao(self, a,b):
        return a*b

    def calcular_divisao(self, a,b):
        if b == 0:
            raise ValueError("Não é possível dividir por 0") #Mostra q é um erro e n uma string comum
        return a/b

    def calcular_potencia(self, a,b):
        resultado = a**b
        return resultado

    def calcular_raiz_quadrada(self, a):
        if a < 0:
            raise ValueError("Não existe raiz de número negativo!")
        return math.sqrt(a)

    def calcular_porcentagem(self, a,b):
        resultado = (a*b)/100
        return resultado

    def calcular_resto(self, a,b):
        resultado = a%b
        return resultado

