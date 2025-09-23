import tkinter as tk
from tkinter import ttk, filedialog as fd


root = tk.Tk()
root.title('Label de caminho de arquivo')
root.geometry('600x400')

texto_label = tk.StringVar()

def funcao(event):
    label.config(text=fd.askopenfilename())

botao = ttk.Button(root, text='Clique para selecionar um arquivo')
botao.bind('<Button-1>', funcao)
botao.grid(column=0, row=0)

label = ttk.Label(root, text='')
label.grid(column=0, row=1)


root.mainloop()