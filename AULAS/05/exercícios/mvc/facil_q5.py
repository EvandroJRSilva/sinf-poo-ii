import tkinter as tk
from tkinter import ttk

class View():
    def __init__(self, container):
        self.container = container
        self.controller = None
        
        self.estilo = ttk.Style()
        self.estilo.theme_use('clam')
        self.estilo.configure('TButton', font=('Arial', 14))
        self.estilo.configure("botao1.TButton", foreground="red")
        self.estilo.configure("botao2.TButton", foreground="green")
        self.estilo.configure("botao3.TButton", foreground="blue")
        
        self.botao1 = ttk.Button(self.container, text="Vermelho", style='botao1.TButton')
        self.botao1['command'] = lambda: self.muda_cor('vermelho')
        self.botao1.grid(row=0, column=0, padx=10)
        
        self.botao2 = ttk.Button(self.container, text="Verde", style='botao2.TButton')
        self.botao2['command'] = lambda: self.muda_cor('verde')
        self.botao2.grid(row=0, column=1, padx=10)
        
        self.botao3 = ttk.Button(self.container, text="Azul", style='botao3.TButton')
        self.botao3['command'] = lambda: self.muda_cor('azul')
        self.botao3.grid(row=0, column=2, padx=10)
        
    def muda_cor(self, cor):
        #print(f'linha 26: {cor}')
        print(f'linha 27: {self.controller}')
        if self.controller:
            print(cor)
            self.controller.set_color(cor)
    
    def set_controller(self, controller):
        self.controller = controller
        
            
class Model():
    def __init__(self):
        pass
    
    def select_color(self, cor):
        match cor:
            case 'vermelho':
                return 'red'
            case 'verde':
                return 'green'
            case 'azul':
                return 'blue'
            
class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
    def set_color(self, cor):
        self.view.container['bg'] = self.model.select_color(cor)
        
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("600x100")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        modelo = Model()
        view = View(self)
        controller = Controller(modelo, view)
        
        view.set_controller(controller)
        
if __name__ == '__main__':
    app = App()
    app.mainloop()