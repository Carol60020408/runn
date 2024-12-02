import pygame
from buraco import Buraco
from rampa import Rampa

class Cenas:
    def __init__(self, buraco_imagem, rampa_imagem):
        self.buraco_imagem = pygame.image.load(buraco_imagem).convert_alpha()
        self.rampa_imagem = pygame.image.load(rampa_imagem).convert_alpha()
        self.buracos = []
        self.rampas = []
        self.velocidade = 5

    def criar_elementos(self):
        # Criar buracos e rampas iniciais
        self.buracos.append(Buraco(800, 300, 50, 100, self.buraco_imagem))
        self.rampas.append(Rampa(1000, 250, 100, 50, self.rampa_imagem))

    def atualizar(self):
        # Atualizar a posição de buracos e rampas
        for buraco in self.buracos:
            buraco.mover(self.velocidade)
        for rampa in self.rampas:
            rampa.mover(self.velocidade)

    def desenhar(self, tela):
        # Desenhar buracos e rampas na tela
        for buraco in self.buracos:
            buraco.desenhar(tela)
        for rampa in self.rampas:
            rampa.desenhar(tela)
