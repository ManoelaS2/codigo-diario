import tkinter as tk

#Criar janela
janela = tk.Tk()
janela.title("Calculadora")

#Criar display 
display = tk.Entry(janela, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=3) 
#display.pack() - mais simples

def clicar(numero):
    display.insert(tk.END, str(numero))

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

#lambda: "atrasa" a execução da função, ela só vai rodar quando o botão for clicado
#botao1.pack() - empilhar

botao1.grid(row=5, column=0, padx=5, pady=5)
botao2.grid(row=5, column=1, padx=5, pady=5)
botao3.grid(row=5, column=2, padx=5, pady=5)

botao4.grid(row=4, column=0, padx=5, pady=5)
botao5.grid(row=4, column=1, padx=5, pady=5)
botao6.grid(row=4, column=2, padx=5, pady=5)

botao7.grid(row=3, column=0, padx=5, pady=5)
botao8.grid(row=3, column=1, padx=5, pady=5)
botao9.grid(row=3, column=2, padx=5, pady=5)


janela.mainloop()

