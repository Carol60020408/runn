import pygame

class Jogador:
    def __init__(self, x, y, largura, altura, imagem_caminho):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade_pulo = -15
        self.gravidade = 1
        self.velocidade_horizontal = 5  # Velocidade de movimento horizontal
        self.esta_no_ar = False
        self.imagem = pygame.image.load(imagem_caminho).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))

    def pular(self, tecla_espaco):
        if tecla_espaco and not self.esta_no_ar:
            self.velocidade_pulo = -15
            self.esta_no_ar = True

    def atualizar(self, altura_chao, teclas):
        # Atualizar posição vertical
        self.y += self.velocidade_pulo
        self.velocidade_pulo += self.gravidade

        # Garantir que não ultrapasse o chão
        if self.y >= altura_chao:
            self.y = altura_chao
            self.esta_no_ar = False

        # Movimentação horizontal no ar
        if teclas[pygame.K_LEFT] and self.x > 0:  # Movimento para a esquerda
            self.x -= self.velocidade_horizontal
        if teclas[pygame.K_RIGHT] and self.x + self.largura < 800:  # Movimento para a direita
            self.x += self.velocidade_horizontal

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

    def colidir(self, objeto):
        return (self.x < objeto.x + objeto.largura and
                self.x + self.largura > objeto.x and
                self.y + self.altura > objeto.y)
