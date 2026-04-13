import tkinter as tk
from mvc import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("600x100")
        
        model = Model()
        view = View(self)
        controller = Controller(model, view)
        
        view.set_controller(controller)
    
if __name__ == '__main__':
    app = App()
    app.mainloop()