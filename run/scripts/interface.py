import pygame

class Interface:
    def __init__(self, fonte, cor_texto):
        self.fonte = fonte
        self.cor_texto = cor_texto

    def exibir_texto(self, tela, texto, x, y):
        renderizado = self.fonte.render(texto, True, self.cor_texto)
        tela.blit(renderizado, (x, y))

    def mostrar_ranking(self, tela, ranking):
        tela.fill((255, 255, 255))
        titulo = self.fonte.render("Ranking de Pontuação", True, (0, 0, 0))
        tela.blit(titulo, (400 - titulo.get_width() // 2, 50))
        for i, score in enumerate(ranking[:5], start=1):
            texto = self.fonte.render(f"{i}. {score}", True, (0, 0, 0))
            tela.blit(texto, (400 - texto.get_width() // 2, 100 + i * 30))
        pygame.display.flip()
        pygame.time.wait(5000)
