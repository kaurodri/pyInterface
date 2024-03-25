import tkinter as tk

class Interface:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Interface")
        self.janela.geometry("500x500")

if __name__ == "__main__":
    root = tk.Tk()
    interface = Interface(root)
    root.mainloop()