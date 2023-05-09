import pygame

#Creation de la premiere fentre
pygame.init()

#determination des dimentions de l'ecran
pixelSize = (800,600)

#Creation de l'ecran
screen = pygame.display.set_mode(pixelSize)

running = True

background_color = (255,255,255) #white

#while running:
    

running = True
while running:
    # Fill the screen with the background color
    screen.fill(background_color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update the screen
    pygame.display.update()