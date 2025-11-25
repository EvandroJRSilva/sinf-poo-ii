import tkinter as tk
from tkinter import messagebox
import requests

BASE_URL = 'http://localhost:5002'

def listar_despesas():
    try:
        response = requests.get(f'{BASE_URL}/expenses')
        data = response.json()
        lista.delete(0, tk.END)
        for exp in data['expenses']:
            lista.insert(tk.END, f"{exp['descricao']}: R${exp['valor']} em {exp['data']} (ID: {exp['id']})")
        label_total.config(text=f"Total Gasto: R${data['total']:.2f}")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")

def adicionar_despesa():
    desc = entrada_desc.get()
    valor = entrada_valor.get()
    if not desc or not valor:
        messagebox.showwarning("Aviso", "Preencha descrição e valor!")
        return
    try:
        response = requests.post(f'{BASE_URL}/expenses', json={'descricao': desc, 'valor': float(valor)})
        if response.status_code == 201:
            entrada_desc.delete(0, tk.END)
            entrada_valor.delete(0, tk.END)
            listar_despesas()
        else:
            messagebox.showerror("Erro", "Falha ao adicionar despesa")
    except (requests.RequestException, ValueError) as e:
        messagebox.showerror("Erro", f"Falha: {e}")

# Interface Tkinter
root = tk.Tk()
root.title("Calculadora de Orçamento")

tk.Label(root, text="Descrição:").grid(row=0, column=0)
entrada_desc = tk.Entry(root)
entrada_desc.grid(row=0, column=1)

tk.Label(root, text="Valor (R$):").grid(row=1, column=0)
entrada_valor = tk.Entry(root)
entrada_valor.grid(row=1, column=1)

tk.Button(root, text="Adicionar Despesa", command=adicionar_despesa).grid(row=2, column=0, columnspan=2)
tk.Button(root, text="Listar e Total", command=listar_despesas).grid(row=3, column=0, columnspan=2)

lista = tk.Listbox(root, width=50)
lista.grid(row=4, column=0, columnspan=2)

label_total = tk.Label(root, text="Total Gasto: R$0.00")
label_total.grid(row=5, column=0, columnspan=2)

listar_despesas()
root.mainloop()