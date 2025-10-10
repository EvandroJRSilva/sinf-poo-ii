from tkinter import ttk

class Model():
    def __init__(self):
        pass
    
    def mensagem(self):
        return "Olá da modelo"


    
class View():
    def __init__(self, container):
        self.container = container
    
        self.estilo = ttk.Style()
        self.estilo.configure("TButton", font=("Helvetica", 16))
        self.estilo.configure("TLabel", font=("Helvetica", 16))
    
        self.botao = ttk.Button(self.container, text="Clique", command=self.clicar)
        self.botao.pack(side="left", padx=10)
    
        self.label = ttk.Label(self.container, text="")
        self.label.pack(side="left", expand=True)
    
        self.controller = None
    
    def set_controller(self, controller):
        self.controller = controller
        
    def clicar(self):
        if self.controller:
            self.controller.chama_mensagem()


class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
    def chama_mensagem(self):
        mensagem = self.model.mensagem()
        self.mudaLabel(mensagem)
        
    def mudaLabel(self, texto):
        self.view.label["text"] = texto