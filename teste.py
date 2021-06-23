import os
import tkinter as tk

#from tkinter import *

#Tela = Tk()
#Tela.geometry()

class Login ():
    def __init__(self, tela = tk.Tk()) -> None:
        #config tela
        tela.title("Login")
        tela.iconbitmap(caminho)

        #tamanho da tela
        #tela.geometry("300x300")
        tela.minsize(300, 300)

        #Declaração da Label
        #Declaração do botão

        tela.mainloop()

#====================================================
lista_program = os.listdir(".")
programa = "Imagens"

for i in lista_program:
    if i == programa:
        caminho = os.path.abspath(i) + "\login.ico"
#====================================================

Login()

"""
import os
for caminho, diretorios, arquivos in os.walk(''):
    print(caminho)
    print(diretorios)
    print(arquivos)
"""