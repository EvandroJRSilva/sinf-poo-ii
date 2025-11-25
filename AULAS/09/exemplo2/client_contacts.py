import tkinter as tk
from tkinter import messagebox
import requests

BASE_URL = 'http://localhost:5001'

def listar_contatos():
    try:
        response = requests.get(f'{BASE_URL}/contacts')
        contacts = response.json()
        lista.delete(0, tk.END)
        for contact in contacts:
            lista.insert(tk.END, f"{contact['name']} - {contact['email']} - {contact['phone']} (ID: {contact['id']})")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")

def adicionar_contato():
    nome = entrada_nome.get()
    email = entrada_email.get()
    phone = entrada_phone.get()
    if not all([nome, email, phone]):
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return
    try:
        response = requests.post(f'{BASE_URL}/contacts', json={'name': nome, 'email': email, 'phone': phone})
        if response.status_code == 201:
            entrada_nome.delete(0, tk.END)
            entrada_email.delete(0, tk.END)
            entrada_phone.delete(0, tk.END)
            listar_contatos()
        else:
            messagebox.showerror("Erro", "Falha ao adicionar contato")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")

# Interface Tkinter
root = tk.Tk()
root.title("Gerenciador de Contatos")

tk.Label(root, text="Nome:").grid(row=0, column=0)
entrada_nome = tk.Entry(root)
entrada_nome.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0)
entrada_email = tk.Entry(root)
entrada_email.grid(row=1, column=1)

tk.Label(root, text="Telefone:").grid(row=2, column=0)
entrada_phone = tk.Entry(root)
entrada_phone.grid(row=2, column=1)

tk.Button(root, text="Adicionar", command=adicionar_contato).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Listar Contatos", command=listar_contatos).grid(row=4, column=0, columnspan=2)

lista = tk.Listbox(root, width=50)
lista.grid(row=5, column=0, columnspan=2)

listar_contatos()
root.mainloop()