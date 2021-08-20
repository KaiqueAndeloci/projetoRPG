from sys import *
from pygame import *
#=======
import tkinter as tk

import pygame
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#=======
class mensagem(pygame.sprite.Sprite):
    def __init__(self, largura, altura, botao_cancelar, botao_ok, botao_sim, botao_nao):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()

        #VARIAVEIS UTEIS
        self.botoes_utilizados = [botao_cancelar, botao_ok, botao_sim, botao_nao]

        #CONFIG DA TELA
        self.largura = int(largura - 0.7*largura)
        self.altura = int((altura - 60) - 0.7*(altura - 60))

        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Mensagem")

        #CONFIG DA AREA DE DESENHO
        self.largura_desenho = int(self.largura - 0.1*self.largura)
        self.altura_desenho = int(self.altura - 0.1*self.altura)

        self.posicao_x = int((self.largura - self.largura_desenho)/2)
        self.posicao_y = int((self.altura - self.altura_desenho)/2)

        #FPS
        self.FPS = 60
        self.relogio = pygame.time.Clock()

        #CRIANO OBJETOS
        self.objetos()

        self.loop()

    def Desenhando(self):
        self.tela.fill((215, 215, 215))

        self.grupo_desenho.draw(self.tela)

        self.tela.blit(self.fps_menagem, (self.posicao_x, self.posicao_y))
        self.tela.blit(self.titulo, (self.largura_desenho/2, self.altura_desenho*0.2))
        self.tela.blit(self.mensagem, (self.largura_desenho/2, self.altura_desenho*0.5))
        self.tela.blit(self.pergunta, (self.largura_desenho/2, self.altura_desenho*0.75))

    def objetos(self):
        #criando grupo de objetos
        self.grupo_desenho = pygame.sprite.Group()
        self.lista_botoes = []

        #retandulo azul
        retangulo = pygame.sprite.Sprite(self.grupo_desenho)
        retangulo.image = pygame.Surface((self.largura_desenho, self.altura_desenho))
        retangulo.image.fill((204, 253, 251))
        retangulo.rect = retangulo.image.get_rect()
        retangulo.rect.center = (int(self.largura/2), int(self.altura/2))

        #botao retangular verde cancelar
        botao_cancelar = []

        botao_cancelar.append(int(self.largura*0.85))
        botao_cancelar.append(0)
        botao_cancelar.append(int(self.largura*0.85 + 50))
        botao_cancelar.append(50)

        botao = pygame.sprite.Sprite(self.grupo_desenho)
        botao.image = pygame.Surface((50, 50))
        botao.image.fill((66, 255, 161))
        botao.rect = botao.image.get_rect()
        botao.rect = (int(self.largura/2),int(self.altura/2))

        self.lista_botoes.append(botao_cancelar)

        #botao amarelo ok
        botao_ok = []

        botao_ok.append(int(self.largura*0.85))
        botao_ok.append(0)
        botao_ok.append(int(self.largura*0.85 + 50))
        botao_ok.append(50)

        botao = pygame.sprite.Sprite(self.grupo_desenho)
        botao.image = pygame.Surface((50, 50))
        botao.image.fill((255, 236, 91))
        botao.rect = botao.image.get_rect()
        botao.rect = (self.largura_desenho,0)

        self.lista_botoes.append(botao_ok)

        #fontes
        fonte_normal = pygame.font.SysFont("arial", 20, False, False)
        fonte_fps = pygame.font.SysFont("arial", 12, True, False)

        #Legendas
        fps_formatado = str(self.relogio).replace("<Clock(", "").replace(")>", "")
        self.fps_menagem = fonte_fps.render(fps_formatado, True, (0, 0, 0))

        self.titulo = fonte_normal.render("Titulo", True, (0, 0, 0))

        self.mensagem = fonte_normal.render("Menagem", True, (0, 0, 0))

        self.pergunta = fonte_normal.render("Pergunta", True, (0, 0, 0))

    def esta_em_cima(self, mouse, botao_list): 
        for botao in botao_list:
            x_mouse, y_mouse = mouse[0], mouse[1]
            x_inicial_botao, y_inicial_botao, x_final_botao, y_final_botao = botao[0], botao[1], botao[2], botao[3]

            if x_inicial_botao <= x_mouse and x_mouse <= x_final_botao and y_inicial_botao <= y_mouse and y_mouse <= y_final_botao:
                return True
            else:
                return False

    def loop(self):
        while True:
            self.relogio.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
                elif event.type == pygame.MOUSEBUTTONUP:
                    posicao = pygame.mouse.get_pos()

                    if self.esta_em_cima(posicao, self.lista_botoes) == True:
                        print("clicou na area")


            #print(pygame.key.get_pressed())

            #quadrado_cinza = pygame.draw.rect(tela, (215, 215, 215), (0, 0, largura, altura))
            #pygame.draw.rect(tela, (204, 253, 251), (posicao_x, posicao_y, largura_desenho, altura_desenho))
            

            self.Desenhando()
            pygame.display.update()

mensagem(screen_width,screen_height,True, True, True, True)

""" 
elif event.type == pygame.MOUSEWHEEL:
    #print(pygame.MOUSEWHEEL)
    #print(event.type)
    pass"""