import tkinter as tk

class Interface:
    def __init__(self, janela, nome):
        self.janela = janela
        self.janela.title(nome)
        self.janela.geometry("500x500")