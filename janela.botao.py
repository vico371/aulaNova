import tkinter as tk 

janela = tk.Tk()
janela.title("!Minha primeira GUI")

janela.geometry("400x300")

botao = tk.Button(janela, text= "Clique Aqui")
botao.pack()

janela.mainloop()
