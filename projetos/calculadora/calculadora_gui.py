import tkinter as tk
from calculadora import soma, subtracao, multiplicacao, divisao

#Criar janela
janela = tk.Tk()
janela.title("Calculadora")

#Criar display 
display = tk.Entry(janela, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=3) 
#display.pack() - mais simples

def clicar(numero):
    display.insert(tk.END, str(numero))

#lambda: "atrasa" a execução da função, ela só vai rodar quando o botão for clicado
#botao1.pack() - empilhar

#Botões com funções
primeiro_numero = None
operacao = None
segundo_numero = None
def escolher_operacao(op):
    global primeiro_numero, operacao
    if display.get() == '': #se a pessoa clicar em + não vai dar erro
        return
    primeiro_numero = float(display.get())  #display.get como um input
    operacao = op                            # Guarda qual operação
    display.delete(0, tk.END) 
def calcular():
    global primeiro_numero, operacao
    
    segundo_numero = float(display.get())
    
    if operacao == "+":
        resultado = soma(primeiro_numero, segundo_numero)
    elif operacao == "-":
        resultado = subtracao(primeiro_numero, segundo_numero)
    elif operacao == "*":
        resultado = multiplicacao(primeiro_numero, segundo_numero)
    elif operacao == "/":
        resultado = divisao(primeiro_numero, segundo_numero)
    
    display.delete(0, tk.END)
    display.insert(tk.END, str(resultado))

#botão 1
botao1 = tk.Button(janela, text="1", width=15, height=5, command=lambda: clicar(1))
botao2 = tk.Button(janela, text="2", width=15, height=5, command=lambda: clicar(2))
botao3 = tk.Button(janela, text="3", width=15, height=5, command=lambda: clicar(3))
botao4 = tk.Button(janela, text="4", width=15, height=5, command=lambda: clicar(4))
botao5 = tk.Button(janela, text="5", width=15, height=5, command=lambda: clicar(5))
botao6 = tk.Button(janela, text="6", width=15, height=5, command=lambda: clicar(6))
botao7 = tk.Button(janela, text="7", width=15, height=5, command=lambda: clicar(7))
botao8 = tk.Button(janela, text="8", width=15, height=5, command=lambda: clicar(8))
botao9 = tk.Button(janela, text="9", width=15, height=5, command=lambda: clicar(9))
botao0 = tk.Button(janela, text="0", width=15, height=5, command=lambda: clicar(0))
botao_mais = tk.Button(janela, text="+", width=15, height=5, command=lambda: escolher_operacao("+"))
botao_menos = tk.Button(janela, text="-", width=15, height=5, command=lambda: escolher_operacao("-"))
botao_vezes = tk.Button(janela, text="×", width=15, height=5, command=lambda: escolher_operacao("*"))
botao_divisao = tk.Button(janela, text="÷", width=15, height=5, command=lambda: escolher_operacao("/"))
botao_igual = tk.Button(janela, text="=", width=15, height=5, command=calcular)



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


janela.mainloop()

