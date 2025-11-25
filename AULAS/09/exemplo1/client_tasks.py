import tkinter as tk
from tkinter import messagebox
import requests

BASE_URL = 'http://localhost:5000'

def listar_tarefas():
    try:
        response = requests.get(f'{BASE_URL}/tasks')
        tasks = response.json()
        lista.delete(0, tk.END)
        for task in tasks:
            status = '✓' if task['completed'] else '✗'
            lista.insert(tk.END, f"{status} {task['task']} (ID: {task['id']})")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")

def adicionar_tarefa():
    tarefa = entrada.get()
    if not tarefa:
        messagebox.showwarning("Aviso", "Digite uma tarefa!")
        return
    try:
        response = requests.post(f'{BASE_URL}/tasks', json={'task': tarefa})
        if response.status_code == 201:
            entrada.delete(0, tk.END)
            listar_tarefas()
        else:
            messagebox.showerror("Erro", "Falha ao adicionar tarefa")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")

def remover_tarefa():
    selecao = lista.curselection()
    if not selecao:
        messagebox.showwarning("Aviso", "Selecione uma tarefa!")
        return
    item = lista.get(selecao[0])
    task_id = int(item.split('ID: ')[1].strip(')'))
    try:
        response = requests.delete(f'{BASE_URL}/tasks/{task_id}')
        if response.status_code == 200:
            listar_tarefas()
        else:
            messagebox.showerror("Erro", "Falha ao remover tarefa")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")
        
def concluir_tarefa():
    selecao = lista.curselection()
    if not selecao:
        messagebox.showwarning("Aviso", "Selecione uma tarefa!")
        return
    item = lista.get(selecao[0])
    task_id = int(item.split('ID: ')[1].strip(')'))
    try:
        response = requests.patch(f'{BASE_URL}/tasks/{task_id}')
        if response.status_code == 200:
            messagebox.showinfo("Sucesso", "Tarefa concluída com sucesso!", icon='info')
            listar_tarefas()
        else:
            messagebox.showerror("Erro", "Falha ao concluir tarefa")
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Falha na conexão: {e}")

# Interface Tkinter
root = tk.Tk()
root.title("Gerenciador de Tarefas")

tk.Label(root, text="Nova Tarefa:").pack()
entrada = tk.Entry(root, width=50)
entrada.pack()

tk.Button(root, text="Adicionar", command=adicionar_tarefa).pack()
tk.Button(root, text="Listar Tarefas", command=listar_tarefas).pack()
tk.Button(root, text="Remover Selecionada", command=remover_tarefa).pack()
tk.Button(root, text="Concluir Tarefa", command=concluir_tarefa).pack()

lista = tk.Listbox(root, width=60, height=10)
lista.pack()

listar_tarefas()  # Carrega tarefas iniciais
root.mainloop()