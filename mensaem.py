import tkinter as tk
from tkinter.constants import BOTH, CENTER, X, Y

#tela1 = tk.Tk()
#print(tela1.winfo_geometry())



class menssagem():
    def __init__(self, tela = tk.Tk()):
        #config tela
        tela.title("Alerta")
        tela.resizable(True, False)

        #tamanho da tela
        altura_tela = 200
        largura_tela = 500
        
        #altura do computador
        y = tela.winfo_screenheight()
        #largura do computador
        x = tela.winfo_screenwidth()

        posicao_x = int(x/2 - largura_tela/2)
        posicao_y = int(y/2 - altura_tela/2)


        tela.geometry(f"{largura_tela}x{altura_tela}+{posicao_x}+{posicao_y}")
        tela.minsize(largura_tela, altura_tela)


        #Frame
        print(tela.winfo_geometry())
        tela.update()
        print(tela.winfo_geometry())

        #self.altura_Frame = int( - altura_tela*0.1)
        self.altura_Frame = int(altura_tela - altura_tela*0.1)
        self.largura_Frame = int(largura_tela - largura_tela*0.1)
        self.Tela1 = tk.Frame(tela, background="#3fcc5b", height = self.altura_Frame, width = self.largura_Frame)

        #Label
        self.texto = tk.StringVar()
        self.label_alerta = tk.Label(self.Tela1, textvariable = self.texto, justify = CENTER, background = "#ccfdfb")


        #mensagem

        #botao
        
        #Organização dos objetos na tela
        self.Tela1.place(x = 0, y = 0)
        #self.Tela1.pack()

        



        #self.label_alerta.pack(side="bottom")
        self.label_alerta.place(x = 10, y = 10)

        

    def set_label_alerta(self, texto):
        self.texto.set(texto)

    def iniciar(self):
        tk.mainloop()

x1 = "TEXTO"

test = menssagem()
test.set_label_alerta(x1)
test.iniciar()

