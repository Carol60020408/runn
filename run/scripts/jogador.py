import pygame

class Jogador:
    def __init__(self, x, y, largura, altura, imagem_caminho):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade_pulo = -15
        self.gravidade = 1
        self.esta_no_ar = False
        self.imagem = pygame.image.load(imagem_caminho).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))

    def pular(self):
        if not self.esta_no_ar:
            self.velocidade_pulo = -15
            self.esta_no_ar = True

    def atualizar(self, altura_chao):
        self.y += self.velocidade_pulo
        self.velocidade_pulo += self.gravidade
        if self.y >= altura_chao:
            self.y = altura_chao
            self.esta_no_ar = False

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

    def colidir(self, objeto):
        return (self.x < objeto.x + objeto.largura and
                self.x + self.largura > objeto.x and
                self.y + self.altura > objeto.y)
