import pygame

class Jogador:
    def __init__(self, x, y, largura, altura, imagem_path):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.imagem = pygame.image.load(imagem_path).convert_alpha()
        self.velocidade_y = 0
        self.gravidade = 1
        self.pulando = False

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

    def pular(self):
        if not self.pulando:
            self.velocidade_y = -15
            self.pulando = True

    def atualizar(self, altura_chao):
        self.velocidade_y += self.gravidade
        self.y += self.velocidade_y
        if self.y + self.altura >= altura_chao:
            self.y = altura_chao - self.altura
            self.pulando = False
