import pygame 
pygame.init() # iniciando a lib pygame

janela = pygame.display.set_mode((800,600)) # criando e dando tamanho a tela
pygame.display.set_caption("Criando um jogo com python") # dando nome a tela

# Abrir e fechar tela em um programa Python.
janela_aberta = True
while janela_aberta :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

# Encerrar o jogo
pygame.quit()