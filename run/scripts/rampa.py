import pygame

class Rampa:
    def __init__(self, x, y, largura, altura, imagem):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.imagem_original = imagem
        self.imagem = pygame.transform.scale(imagem, (largura, altura))

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

    def mover(self, velocidade):
        self.x -= velocidade

        # Reduz a largura e a altura ao longo do movimento
        if self.largura > 10 and self.altura > 10:  # Define limites mínimos
            self.largura -= 1
            self.altura -= 1
            self.imagem = pygame.transform.scale(self.imagem_original, (self.largura, self.altura))

        # Reposicionar para o final da tela quando sair do campo de visão
        if self.x + self.largura < 0:
            self.x = 800  # Reposicionar no final da tela
            self.largura = 100  # Reiniciar largura original
            self.altura = 50   # Reiniciar altura original
            self.imagem = pygame.transform.scale(self.imagem_original, (self.largura, self.altura))
