import pygame


#Creation de la premiere fentre
pygame.init()

#determination des dimentions de l'ecran
pixelSize = (800,600)

#Creation de l'ecran
screen = pygame.display.set_mode(pixelSize)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit() # Quit the game