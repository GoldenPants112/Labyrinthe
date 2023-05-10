import pygame


#Creation de la premiere fentre
pygame.init()

#determination des dimentions de l'ecran
pixelSize = (700,700)

#Creation de l'ecran
screen = pygame.display.set_mode(pixelSize)


background_color = (0,0,0) #Black


#extracts Captain_France from file
Captain_France = pygame.image.load("Captain_France.png")
# Scale the image to half its original size
Captain_France = pygame.transform.scale(Captain_France, (100,100))

# Get the dimensions of the image
Captain_France_width, Captain_France_height = Captain_France.get_size()


running = True

while running:
    #if X -> close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Fill the screen with the background color
    screen.fill(background_color)
    
    

    # Calculate the position of the image in the center of the screen
    x = (pixelSize[0] - Captain_France_width) // 2 #ordonne
    y = (pixelSize[1] - Captain_France_height) // 2 #abscisse

    # Draw the image on the screen
    screen.blit(Captain_France, (x, y))

    # Update the screen
    pygame.display.update()

    
# Quit Pygame
pygame.quit()
    