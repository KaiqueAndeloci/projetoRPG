from sys import *
from pygame import *
#=======
import tkinter as tk

import pygame
#root = tk.Tk()
#screen_width = root.winfo_screenwidth()
#screen_height = root.winfo_screenheight()
#=======
class mensagem(pygame.sprite.Sprite):
    def __new__(cls, largura, altura, botao_cancelar, botao_ok, botao_sim_nao, Título, Mensagem, Pergunta, FPS):
        self = super().__new__(cls)
        pygame.sprite.Sprite.__init__(self)
        pygame.init()

        #VARIAVEIS UTEIS
        self.botoes_utilizados = [botao_cancelar, botao_ok, botao_sim_nao, botao_sim_nao]
        self.legendas = [Título, Mensagem, Pergunta]

        #CONFIG DA TELA
        self.largura = int(largura - 0.5*largura)
        self.altura = int((altura - 60) - 0.5*(altura - 60))

        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Mensagem")

        #CONFIG DA AREA DE DESENHO AZUL
        self.largura_desenho = int(0.9*self.largura)
        self.altura_desenho = int(0.9*self.altura)

        self.posicao_x = int((self.largura - self.largura_desenho)/2)
        self.posicao_y = int((self.altura - self.altura_desenho)/2)

        #FPS
        self.FPS = FPS
        self.relogio = pygame.time.Clock()

        #CRIANO OBJETOS
        self.objetos()

        #primeira vez desenhando na tela
        self.Desenhando()

        return self.loop()

    def objetos(self):
        #criando grupo de objetos
        self.grupo_desenho = pygame.sprite.Group()
        self.grupo_redeenhavel = pygame.sprite.Group()
        self.lista_botoes = []

        #Todass as cores
        self.cor_preto = (0, 0, 0)
        self.cor_cinza = (215, 215, 215)
        self.cor_verde = ()
        self.cor_amarelo = ()
        self.cor_azul = (204, 253, 251)

        #retandulo azul
        retangulo = pygame.sprite.Sprite(self.grupo_desenho)
        retangulo.image = pygame.Surface((self.largura_desenho, self.altura_desenho))
        retangulo.image.fill(self.cor_azul)
        retangulo.rect = retangulo.image.get_rect()
        retangulo.rect.center = (int(self.largura/2), int(self.altura/2))

        #fontes
        fonte_normal = pygame.font.SysFont("arial", 20, False, False)
        self.fonte_fps = pygame.font.SysFont("arial", 12, True, False)

        #BOTOES
        LARGURA = 100
        ALTURA = 50
        x_btn1 = int(0.05*self.largura + self.largura_desenho - LARGURA)
        y_btn1 = int(0.1*self.altura/2 + self.altura_desenho - ALTURA)
        x_btn2 = int(0.05*self.largura + self.largura_desenho - LARGURA*2 - 5)

        def dois_btn(text_btn1, text_btn2):
            self.botoes(True, (255, 236, 91), LARGURA, ALTURA, x_btn1, y_btn1, self.grupo_desenho)
            self.legenda_btn1 = fonte_normal.render(text_btn1, True, self.cor_preto)
            self.legenda_btn1_pos = self.legenda_btn1.get_rect()
            self.legenda_btn1_pos.center = (x_btn1 + LARGURA/2, y_btn1 + ALTURA/2)
                
            self.botoes(True, (66, 255, 161), LARGURA, ALTURA, x_btn2, y_btn1, self.grupo_desenho)
            self.legenda_btn2 = fonte_normal.render(text_btn2, True, self.cor_preto)
            self.legenda_btn2_pos = self.legenda_btn2.get_rect()
            self.legenda_btn2_pos.center = (x_btn2 + LARGURA/2, y_btn1 + ALTURA/2)

        def um_btn(text_btn):
            self.botoes(True, (255, 236, 91), LARGURA, ALTURA, x_btn1, y_btn1, self.grupo_desenho)
            self.legenda_btn1 = fonte_normal.render(text_btn, True, self.cor_preto)
            self.legenda_btn1_pos = self.legenda_btn1.get_rect()
            self.legenda_btn1_pos.center = (x_btn1 + LARGURA/2, y_btn1 + ALTURA/2)

        if self.botoes_utilizados == [True, True, False, False]:
            dois_btn("Cancelar", "Ok")
        
        elif self.botoes_utilizados == [False, True, False, False]:
            um_btn("Ok")
        
        elif self.botoes_utilizados == [True, False, False, False]:
            um_btn("Cancelar")

        elif self.botoes_utilizados == [False, False, True, True]:
            dois_btn("Não", "Sim")


        #Legendas
        self.titulo = fonte_normal.render(self.legendas[0], True, self.cor_preto)
        self.titulo_posicao = self.titulo.get_rect()
        self.titulo_posicao.center = (self.largura_desenho/2, self.altura_desenho*0.2)

        self.mensagem = fonte_normal.render(self.legendas[1], True, self.cor_preto)
        self.mensagem_pos = self.mensagem.get_rect()
        self.mensagem_pos.center = (self.largura_desenho/2, self.altura_desenho*0.5)

        self.pergunta = fonte_normal.render(self.legendas[2], True, self.cor_preto)
        self.pergunta_pos = self.pergunta.get_rect()
        self.pergunta_pos.center = (self.largura_desenho/2, self.altura_desenho*0.75)

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
        
    def Redesenhando(self):
        fps_posicao = (self.posicao_x, self.posicao_y)
        self.botoes(False, self.cor_azul, 100, 20, fps_posicao[0] + 1, fps_posicao[1] + 1, self.grupo_redeenhavel)

        fps_formatado = str(self.relogio).replace("<Clock(", "").replace(")>", "")
        fps_mensagem = self.fonte_fps.render(fps_formatado, True, self.cor_preto)

        self.grupo_redeenhavel.draw(self.tela)
        
        self.tela.blit(fps_mensagem, fps_posicao)

    def Desenhando(self):
        self.tela.fill(self.cor_cinza)

        self.grupo_desenho.draw(self.tela)

        self.tela.blit(self.titulo, self.titulo_posicao)
        self.tela.blit(self.mensagem, self.mensagem_pos)
        self.tela.blit(self.pergunta, self.pergunta_pos)

        if self.botoes_utilizados[0] == True and self.botoes_utilizados[1] == True or self.botoes_utilizados[2] and self.botoes_utilizados[3]:
            self.tela.blit(self.legenda_btn1, self.legenda_btn1_pos)            
            self.tela.blit(self.legenda_btn2, self.legenda_btn2_pos)
        else:
            self.tela.blit(self.legenda_btn1, self.legenda_btn1_pos) 

    def esta_em_cima(self, mouse, botao_list):
        x_mouse, y_mouse = mouse[0], mouse[1]
        contador_botoes = 0
        for botao in botao_list:
            if botao[0] <= x_mouse and x_mouse <= botao[2] and botao[1] <= y_mouse and y_mouse <= botao[3] and botao_list[contador_botoes] == botao:
                return contador_botoes
            else:
                contador_botoes =+ 1

    def loop(self) -> int:
        while True:
            self.relogio.tick(self.FPS)

            self.Redesenhando()

            for event in pygame.event.get():
                if event.type == QUIT:
                    return -1
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
                elif event.type == pygame.MOUSEBUTTONUP:
                    posicao = pygame.mouse.get_pos()

                    if self.esta_em_cima(posicao, self.lista_botoes) == 0:
                        return 0
                    elif self.esta_em_cima(posicao, self.lista_botoes) == 1:
                        return 1

            pygame.display.update()

#print(mensagem(screen_width, screen_height, True, True, False, "teste", "testando", "teste", 20))