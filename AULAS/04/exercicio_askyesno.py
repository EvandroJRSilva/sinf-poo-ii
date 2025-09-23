import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo

def funcao(event):
    if askyesno('Sim ou Não', 'Você tem certeza?'):
        showinfo('Info Sim ou Não', 'Você teve certeza')
    else:
        showinfo('Info Sim ou Não', 'Você não teve certeza')

root = tk.Tk()
root.title('Exemplo Sim Não')
root.geometry('600x400')

ttk.Label(root, text='Você deseja clicar no botão ao lado?').pack(side=tk.LEFT, padx=10)
botao = ttk.Button(root, text='Botão ao lado')
botao.pack(side=tk.LEFT)
botao.bind('<Button-1>', funcao)

root.mainloop()