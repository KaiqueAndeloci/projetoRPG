import os
import pygame
from projetoRPG import teste3

lista_program = os.listdir(".")
programa = "Imagens"

for i in lista_program:
    if i == programa:
        caminho = os.path.abspath(i) + "\login.ico"

class Login():
    def __init__(self):
        pygame.init()

        #tela
        largura = 400
        altura = 400

        self.janela = pygame.display.set_mode ([largura, altura])
        pygame.display.set_caption('TESTE')

        self.chkbox = teste3.Checkbox(self.janela, 400, 400)

        #mainloop
        self.loop()

    def loop(self):
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                self.chkbox.update_checkbox(event)
            pygame.display.update()

            self.janela.fill((200, 200, 200))
            self.chkbox.render_checkbox()
            pygame.display.flip()

#Login()

#pygame.quit()

def main():
    WIDTH = 800
    HEIGHT = 600
    display = pygame.display.set_mode((WIDTH, HEIGHT))

    chkbox = teste3.Checkbox(display, 400, 400)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            chkbox.update_checkbox(event)

        display.fill((200, 200, 200))
        chkbox.render_checkbox()
        pygame.display.flip()

if __name__ == '__main__': main()