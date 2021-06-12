import tkinter as tk

#from tkinter import *

#Tela = Tk()
#Tela.geometry()

class Login ():
    def __init__(self, tela = tk.Tk()) -> None:
        #config tela
        tela.title("Login")
        tela.iconbitmap("login.ico")

        #tamanho da tela
        #tela.geometry("300x300")
        tela.minsize(300, 300)

        #Declaração da Label

        #Declaração do botão

        tela.mainloop()

Login()