import pygame 
pygame.init() # iniciando a lib pygame
x = 400
y = 300
velocidade = 10
fundo = pygame.image.load('fundo.png')
rocket = pygame.image.load('rocket.png')

janela = pygame.display.set_mode((800,600)) # criando e dando tamanho a tela
pygame.display.set_caption("Criando um jogo com python") # dando nome a tela

# Abrir e fechar tela em um programa Python.
janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    if comandos[pygame.K_RIGHT]:
        x+= velocidade
    if comandos[pygame.K_LEFT]:
        x-= velocidade

    janela.blit(fundo, (0,0))
    janela.blit(rocket, (x,y))
    # onde , cor , posição, arredondamento
    pygame.display.update()

# Encerrar o jogo
pygame.quit()