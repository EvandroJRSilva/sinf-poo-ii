import tkinter as tk
from tkinter import messagebox
import requests

BASE_URL = 'http://localhost:5004'

def listar_livros():
    try:
        response = requests.get(f'{BASE_URL}/books')
        books = response.json()
        lista.delete(0, tk.END)
        for book in books:
            status = 'Lido' if book['lido'] else 'Não Lido'
            lista.insert(tk.END, f"{book['titulo']} por {book['autor']} - {status} (ID: {book['id']})")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")

def adicionar_livro():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    if not titulo or not autor:
        messagebox.showwarning("Aviso", "Preencha título e autor!")
        return
    try:
        response = requests.post(f'{BASE_URL}/books', json={'titulo': titulo, 'autor': autor})
        if response.status_code == 201:
            entrada_titulo.delete(0, tk.END)
            entrada_autor.delete(0, tk.END)
            listar_livros()
        else:
            messagebox.showerror("Erro", "Falha ao adicionar livro")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")

def toggle_lido():
    selecao = lista.curselection()
    if not selecao:
        messagebox.showwarning("Aviso", "Selecione um livro!")
        return
    item = lista.get(selecao[0])
    book_id = int(item.split('ID: ')[1].strip(')'))
    try:
        # Toggle lido (simplificado: alterna baseado no atual)
        response_get = requests.get(f'{BASE_URL}/books/{book_id}')  # Assumindo GET por ID, mas adaptado
        # Na verdade, para simplicidade, envia True para marcar como lido
        requests.put(f'{BASE_URL}/books/{book_id}', json={'lido': True})
        listar_livros()
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")

# Interface Tkinter
root = tk.Tk()
root.title("Gerenciador de Livros")

tk.Label(root, text="Título:").grid(row=0, column=0)
entrada_titulo = tk.Entry(root)
entrada_titulo.grid(row=0, column=1)

tk.Label(root, text="Autor:").grid(row=1, column=0)
entrada_autor = tk.Entry(root)
entrada_autor.grid(row=1, column=1)

tk.Button(root, text="Adicionar Livro", command=adicionar_livro).grid(row=2, column=0, columnspan=2)
tk.Button(root, text="Listar Livros", command=listar_livros).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Marcar como Lido", command=toggle_lido).grid(row=4, column=0, columnspan=2)

lista = tk.Listbox(root, width=50)
lista.grid(row=5, column=0, columnspan=2)

listar_livros()
root.mainloop()