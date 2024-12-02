import pygame

class Buraco:
    def __init__(self, x, y, largura, altura, imagem):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.imagem = pygame.transform.scale(imagem, (largura, altura))

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

    def mover(self, velocidade):
        self.x -= velocidade
        if self.x + self.largura < 0:
            self.x = 800  # Reposicionar para o final da tela
