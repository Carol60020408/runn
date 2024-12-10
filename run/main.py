import sys
import os
import pygame
import time

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
jogador = Jogador(50, ALTURA - 100, 50, 50, gato_imagem)
cenas = Cenas(buraco_imagem, rampa_imagem)
interface = Interface(FONTE, (0, 0, 0))
cenas.criar_elementos()

# Variáveis do jogo
pontuacao = 0
fase = 1
ranking = []

# Controle do tempo
ultimo_segundo = time.time()

# Loop principal
def jogo():
    global pontuacao, fase, ranking, ultimo_segundo
    rodando = True
    altura_chao = ALTURA - 100
    proxima_fase_pontuacao = 20 # Pontuação para mudar de fase

    while rodando:
        TELA.fill(BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()

        # Captura o estado das teclas
        teclas = pygame.key.get_pressed()
        
        # Controle de pulo
        jogador.pular(teclas[pygame.K_SPACE])

        # Atualizações do jogo
        jogador.atualizar(altura_chao, teclas)
        cenas.atualizar()

        # Incremento da pontuação por segundo
        tempo_atual = time.time()
        if tempo_atual - ultimo_segundo >= 1:
            pontuacao += 1
            ultimo_segundo = tempo_atual

        # Colisões
        for buraco in cenas.buracos:
            if jogador.colidir(buraco):
                ranking.append(pontuacao)
                ranking.sort(reverse=True)
                interface.mostrar_ranking(TELA, ranking)
                rodando = False

        # Controle de fases
        if pontuacao >= proxima_fase_pontuacao:
            fase += 1
            proxima_fase_pontuacao += 50
            
            interface.exibir_texto(TELA, f"Fase {fase}!", LARGURA // 2 - 50, ALTURA // 2)
            pygame.display.flip()
            pygame.time.delay(1000)

        # Desenhar na tela
        jogador.desenhar(TELA)
        cenas.desenhar(TELA)
        interface.exibir_texto(TELA, f"Fase: {fase} | Pontuação: {pontuacao}", 10, 10)

        # Condição de vitória
        if fase > 3:
            interface.exibir_texto(TELA, "Você venceu!", LARGURA // 2 - 50, ALTURA // 2)
            pygame.display.flip()
            pygame.time.delay(3000)
            rodando = False

        pygame.display.flip()
        clock.tick(30)

# Iniciar o jogo
jogo()
