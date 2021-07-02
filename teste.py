import os
import tkinter as tk
from tkinter.constants import CENTER, W

#test = tk.Tk()
#test.winfo_screenheight

#====================================================
"""
import os
for caminho, diretorios, arquivos in os.walk(''):
    print(caminho)
    print(diretorios)
    print(arquivos)
"""

lista_program = os.listdir(".")
programa = "Imagens"
caminho = ""

for i in lista_program:
    if i == programa:
        caminho = os.path.abspath(i) + "\login.ico"
#====================================================

class Login ():
    def __init__(self, tela = tk.Tk()):
        #config tela
        tela.title("Login")
        tela.iconbitmap(caminho)

        #telas
        self.Tela1 = tk.Frame(tela)

        #tamanho da tela
        altura_tela = 600
        largura_tela = 500
        y = tela.winfo_screenheight()
        x = tela.winfo_screenwidth()

        posicao_x = int(x/2 - largura_tela/2)
        posicao_y = int(y/2 - altura_tela/2)

        tela.geometry(f"{largura_tela}x{altura_tela}+{posicao_x}+{posicao_y}")
        tela.minsize(300, 300)

        #Declaração da Label
        self.label_usuario = tk.Label(self.Tela1, text = "Usuário:")
        self.label_senha = tk.Label(self.Tela1, text = "Senha:")

        #Entry
        self.entry_usuario = tk.Entry(self.Tela1)
        self.entry_senha = tk.Entry(self.Tela1)

        #Declaração do botão
        self.btn_enviar = tk.Button(self.Tela1, name = "enviar", text = "Enviar", command = self.verificar_login)
        
        #Organização dos objetos na tela
        #self.Tela1.grid(sticky = CENTER)

        self.Tela1.pack()
        self.label_usuario.grid(row = 0, column = 0)
        self.entry_usuario.grid(row = 0, column = 1)
        self.label_senha.grid(row = 1, column = 0)
        self.entry_senha.grid(row = 1, column = 1)
        self.btn_enviar.grid(row = 2, column = 1)

        tela.mainloop()
    
    def verificar_login(self):
        user = self.entry_usuario.get()
        senha = self.entry_senha.get()
        if user == "adm" and senha == "123":
            print("deu certo")
        else:
            pass

    def conectar_BD(self):
        pass


Login()
