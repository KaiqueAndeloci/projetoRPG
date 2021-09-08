from pygame import *
import pygame
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

class Login(pygame.sprite.Sprite):
    def __new__(cls, screen_width, screen_height, FPS):
        self = super().__new__(cls)
        pygame.sprite.Sprite.__init__(self)
        pygame.init()

        #Variaveis uteis
        self.largura_tela = screen_width
        self.altura_tela = screen_height
        
        #FPS
        self.FPS = FPS
        self.relogio = pygame.time.Clock()

        return self.loop()

    def Objetos(self):
        #Cores
        self.cor_azul = None
        self.cor_cinza = (215, 215, 215)
        self.cor_preto = (0, 0, 0)
        self.cor_roxa_escura = (73, 0, 147)

        #Tela
        self.tela = pygame.display.set_mode((self.largura_tela, (self.altura_tela - 60)))
        pygame.display.set_caption("Login")

        #Grupo de desenhos
        self.grupo_desenho = pygame.sprite.Group()
        self.grupo_redesenhavel = pygame.sprite.Group()

        #Fontes
        self.fonte_fps = pygame.font.SysFont("arial", 12, True, False)

        #Superfice para os widget
        retangulo = pygame.sprite.Sprite(self.grupo_desenho)
        retangulo.image = pygame.Surface((200, 200))
        retangulo.image.fill(self.cor_roxa_escura)
        retangulo.rect = retangulo.image.get_rect()
        retangulo.rect.center = (int(self.largura_tela), int(self.largura_tela))

        #Lista de botoes
        self.lista_botoes = []

    def desenhando(self):
        self.tela.fill(self.cor_cinza)
        self.grupo_desenho.draw(self.tela)

    def redesenhando(self):
        self.tela.fill(self.cor_cinza)
        fps_posicao = (100, 100)
        fps_formatado = str(self.relogio).replace("<Clock(", "").replace(")>", "")
        fps_mensagem = self.fonte_fps.render(fps_formatado, True, self.cor_preto)

        self.grupo_redesenhavel.draw(self.tela)
        
        self.tela.blit(fps_mensagem, fps_posicao)

    def botoes(self, add_lista, cor, largura_botao, altura_botao, x_botao, y_botao, grupo_desenho):
        dimensoes_botao = []

        dimensoes_botao.append(x_botao)
        dimensoes_botao.append(y_botao)
        dimensoes_botao.append(x_botao + largura_botao)
        dimensoes_botao.append(y_botao + altura_botao)

        botao = pygame.sprite.Sprite(grupo_desenho)
        botao.image = pygame.Surface((largura_botao, altura_botao))
        botao.image.fill((cor))
        botao.rect = botao.image.get_rect()
        botao.rect = (x_botao, y_botao)

        if add_lista == True:
            self.lista_botoes.append(dimensoes_botao)

    def loop(self):
        self.Objetos()
        self.desenhando()

        while True:
            self.redesenhando()
            self.relogio.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == QUIT:
                    return -1
                    

            pygame.display.update()


print(Login(screen_width, screen_height, 30))