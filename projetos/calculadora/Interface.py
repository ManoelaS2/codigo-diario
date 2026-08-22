import tkinter as tk
from Operacoes import Operacoes

class Interface:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora")
        self.display = tk.Entry(self.janela, font=("Arial", 20), justify="right" )
        self.display.grid(row=0, column=0, columnspan=4, ipady=15, padx=10, pady=5, sticky="we")
        self.primeiro_numero = None
        self.operacao = None
        self.op = Operacoes() 
        self.criar_botoes() 

    def clicar(self, numero):
        if self.display.get() == "Erro!":
            self.display.delete(0, tk.END)
        self.display.insert(tk.END, str(numero))
        
    def limpar(self):
        self.display.delete(0, tk.END)   
        self.primeiro_numero = None 
        self.operacao = None 

    def formatar_resultado(self, numero):
        if numero == int(numero):  # Se for inteiro
            return str(int(numero))  # Mostra sem .0
        return str(numero)  # Se tiver decimal, mostra normal

    
    #lambda: "atrasa" a execução da função, ela só vai rodar quando o botão for clicado
    #botao1.pack() - empilhar

    def escolher_operacao(self, op):
        
        if self.display.get() == '': #se a pessoa clicar em + não vai dar erro
            return
        self.primeiro_numero = float(self.display.get())  #display.get como um input
        self.operacao = op                            # Guarda qual operação
        self.display.delete(0, tk.END) 

    def calcular(self):     
        try:
            segundo_numero = float(self.display.get())
            if self.operacao == "+":
                resultado = self.op.calcular_soma(self.primeiro_numero, segundo_numero)
            elif self.operacao == "-":
                resultado = self.op.calcular_subtracao(self.primeiro_numero, segundo_numero)
            elif self.operacao == "*":
                resultado = self.op.calcular_multiplicacao(self.primeiro_numero, segundo_numero)
            elif self.operacao == "/":
                resultado = self.op.calcular_divisao(self.primeiro_numero, segundo_numero)
            elif self.operacao == "mod":
                resultado = self.op.calcular_resto(self.primeiro_numero, segundo_numero)
            elif self.operacao == "%":
                resultado = self.op.calcular_porcentagem(self.primeiro_numero, segundo_numero)
            
            self.display.delete(0, tk.END)
            self.display.insert(0, self.formatar_resultado(resultado))
            
        except ValueError as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erro!")

    def apagar(self):
        texto_atual = self.display.get() #pega o texto atual
        novo_texto = texto_atual[:-1] #remove o ultimo caracter
        self.display.delete(0, tk.END) #Apaga todo o texto
        self.display.insert(0, novo_texto) #Insere o novo bem rápido

    def clicar_ponto(self):
        if "." not in self.display.get():
            self.display.insert(tk.END, ".")

    def clicar_maismenos(self):
        numero_atual = float(self.display.get()) 
        novo_numero = numero_atual*(-1) 
        self.display.delete(0, tk.END) #Apaga todo o texto
        self.display.insert(0, novo_numero) #Insere o novo bem rápido
        
    def calcular_raiz(self):
        try:
            numero = float(self.display.get())
            resultado = self.op.calcular_raiz_quadrada(numero)
            self.display.delete(0, tk.END)
            
            self.display.insert(0, self.formatar_resultado(resultado))
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Erro!")
       

    def calcular_quadrado(self):
        numero = float(self.display.get())
        resultado = self.op.calcular_potencia(numero, 2)
        self.display.delete(0, tk.END)
        self.display.insert(0, str(resultado))
        self.display.insert(0, self.formatar_resultado(resultado))

    #botão 1
    def criar_botoes(self):
        botao1 = tk.Button(self.janela, text="1", width=15, height=5, command=lambda: self.clicar(1))
        botao2 = tk.Button(self.janela, text="2", width=15, height=5, command=lambda: self.clicar(2))
        botao3 = tk.Button(self.janela, text="3", width=15, height=5, command=lambda: self.clicar(3))
        botao4 = tk.Button(self.janela, text="4", width=15, height=5, command=lambda: self.clicar(4))
        botao5 = tk.Button(self.janela, text="5", width=15, height=5, command=lambda: self.clicar(5))
        botao6 = tk.Button(self.janela, text="6", width=15, height=5, command=lambda: self.clicar(6))
        botao7 = tk.Button(self.janela, text="7", width=15, height=5, command=lambda: self.clicar(7))
        botao8 = tk.Button(self.janela, text="8", width=15, height=5, command=lambda: self.clicar(8))
        botao9 = tk.Button(self.janela, text="9", width=15, height=5, command=lambda: self.clicar(9))
        botao0 = tk.Button(self.janela, text="0", width=15, height=5, command=lambda: self.clicar(0))
        botao_mais = tk.Button(self.janela, text="+", width=15, height=5, command=lambda: self.escolher_operacao("+"))
        botao_menos = tk.Button(self.janela, text="-", width=15, height=5, command=lambda: self.escolher_operacao("-"))
        botao_vezes = tk.Button(self.janela, text="×", width=15, height=5, command=lambda: self.escolher_operacao("*"))
        botao_divisao = tk.Button(self.janela, text="÷", width=15, height=5, command=lambda: self.escolher_operacao("/"))
        botao_igual = tk.Button(self.janela, text="=", width=15, height=5, command=self.calcular)
        botao_c = tk.Button(self.janela, text="C", width=15, height=5, command=self.limpar)
        botao_apaga = tk.Button(self.janela, text="⌫", width=15, height=5, command=self.apagar)
        botao_ce = tk.Button(self.janela, text="CE", width=15, height=5, command=self.limpar)
        botao_virgula = tk.Button(self.janela, text=".", width=15, height=5, command=self.clicar_ponto)
        botao_maismenos = tk.Button(self.janela, text="±", width=15, height=5, command=self.clicar_maismenos)
        botao_raiz = tk.Button(self.janela, text="√", width=15, height=5, command=self.calcular_raiz)
        botao_quadrado = tk.Button(self.janela, text="x²", width=15, height=5, command=self.calcular_quadrado)
        botao_mod = tk.Button(self.janela, text="mod", width=15, height=5, command=lambda: self.escolher_operacao("mod"))
        botao_porcentagem = tk.Button(self.janela, text="%", width=15, height=5, command=lambda: self.escolher_operacao("%"))

        botao1.grid(row=5, column=0, padx=5, pady=5)
        botao2.grid(row=5, column=1, padx=5, pady=5)
        botao3.grid(row=5, column=2, padx=5, pady=5)

        botao4.grid(row=4, column=0, padx=5, pady=5)
        botao5.grid(row=4, column=1, padx=5, pady=5)
        botao6.grid(row=4, column=2, padx=5, pady=5)

        botao7.grid(row=3, column=0, padx=5, pady=5)
        botao8.grid(row=3, column=1, padx=5, pady=5)
        botao9.grid(row=3, column=2, padx=5, pady=5)

        botao0.grid(row=6, column=1, padx=5, pady=5)

        botao_mais.grid(row=5, column=3, padx=5, pady=5)
        botao_menos.grid(row=4, column=3, padx=5, pady=5)
        botao_vezes.grid(row=3, column=3, padx=5, pady=5)
        botao_divisao.grid(row=2, column=3, padx=5, pady=5)
        botao_igual.grid(row=6, column=3, padx=5, pady=5)

        botao_c.grid(row=1, column=2, padx=5, pady=5)
        botao_apaga.grid(row=1, column=3, padx=5, pady=5)
        botao_ce.grid(row=1, column=1, padx=5, pady=5) #Por enquando esta com a mesma função do C
        botao_virgula.grid(row=6, column=2, padx=5, pady=5)
        botao_maismenos.grid(row=6, column=0, padx=5, pady=5)
        botao_raiz.grid(row=2, column=2, padx=5, pady=5)
        botao_quadrado.grid(row=2, column=1, padx=5, pady=5)
        botao_mod.grid(row=2, column=0, padx=5, pady=5)
        botao_porcentagem.grid(row=1, column=0, padx=5, pady=5)



