import pygame

#Creation de la premiere fentre
pygame.init()

#determination des dimentions de l'ecran
pixelSize = (800,600)

#Creation de l'ecran
screen = pygame.display.set_mode(pixelSize)


background_color = (255,255,255) #white


#extracts Rico from file
rico = pygame.image.load("Rico.png")

# Get the dimensions of the image
rico_width, rico_height = rico.get_size()

running = True


while running:
    #if X -> close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Fill the screen with the background color
    screen.fill(background_color)
    
    
    # Calculate the position of the image in the center of the screen
    x = (pixelSize[0] - rico_width) // 2
    y = (pixelSize[1] - rico_height) // 2

    # Draw the image on the screen
    screen.blit(rico, (x, y))

    # Update the screen
    pygame.display.update()



    