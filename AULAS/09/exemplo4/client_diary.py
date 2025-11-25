import tkinter as tk
from tkinter import messagebox
import requests

BASE_URL = 'http://localhost:5003'

def listar_entradas():
    try:
        response = requests.get(f'{BASE_URL}/entries')
        entries = response.json()
        lista.delete(0, tk.END)
        for entry in entries:
            lista.insert(tk.END, f"{entry['data']}: {entry['texto'][:50]}... (ID: {entry['id']})")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")

def adicionar_entrada():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Aviso", "Digite uma entrada!")
        return
    try:
        response = requests.post(f'{BASE_URL}/entries', json={'texto': texto})
        if response.status_code == 201:
            entrada_texto.delete("1.0", tk.END)
            listar_entradas()
        else:
            messagebox.showerror("Erro", "Falha ao adicionar entrada")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")

# Interface Tkinter
root = tk.Tk()
root.title("Diário Pessoal")

tk.Label(root, text="Nova Entrada:").pack()
entrada_texto = tk.Text(root, height=5, width=50)
entrada_texto.pack()

tk.Button(root, text="Adicionar", command=adicionar_entrada).pack()
tk.Button(root, text="Listar Entradas", command=listar_entradas).pack()

lista = tk.Listbox(root, width=60, height=10)
lista.pack()

listar_entradas()
root.mainloop()