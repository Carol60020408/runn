import sys
import os
import pygame

# Adicionar o caminho para a pasta 'scripts'
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from cenas import Cenas
from interface import Interface
from jogador import Jogador

# Inicializar PyGame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Gato Cadeirante")
clock = pygame.time.Clock()

# Cores e fontes
BRANCO = (255, 255, 255)
FONTE = pygame.font.Font(None, 36)

# Caminho das imagens
gato_imagem = "assets/estela.png"
buraco_imagem = "assets/buraco.png"
rampa_imagem = "assets/rampa.png"

# Objetos principais
jogador = Jogador(50, ALTURA - 100, 60, 40, gato_imagem)
cenas = Cenas(buraco_imagem, rampa_imagem)
interface = Interface(FONTE, (0, 0, 0))
cenas.criar_elementos()

# Variáveis do jogo
pontuacao = 0
fase = 1
ranking = []

# Loop principal
def jogo():
    global pontuacao, fase, ranking
    rodando = True
    altura_chao = ALTURA - 100

    while rodando:
        TELA.fill(BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()

        # Controles do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            jogador.pular()

        # Atualizações do jogo
        jogador.atualizar(altura_chao)
        cenas.atualizar()

        # Colisões
        for buraco in cenas.buracos:
            if jogador.x < buraco.x + buraco.largura and jogador.x + jogador.largura > buraco.x and jogador.y + jogador.altura > buraco.y:
                ranking.append(pontuacao)
                ranking.sort(reverse=True)
                interface.mostrar_ranking(TELA, ranking)
                rodando = False

        # Desenhar na tela
        jogador.desenhar(TELA)
        cenas.desenhar(TELA)
        interface.exibir_texto(TELA, f"Fase: {fase} | Pontuação: {pontuacao}", 10, 10)

        # Pontuação e fases
        pontuacao += 1
        if pontuacao % 50 == 0:
            fase += 1
            cenas.velocidade += 1

        pygame.display.flip()
        clock.tick(30)

# Iniciar o jogo
jogo()
