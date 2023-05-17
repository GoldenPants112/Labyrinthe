import pygame
import Class_Player

#Creation de la premiere fenetre
pygame.init()
#determination des dimentions de l'ecran
pixelSize = (700,700)

#Creation de l'ecran
screen = pygame.display.set_mode(pixelSize)

#extracts Captain_France from file
Captain_France = pygame.image.load("Captain_France.png")
Captain_France = pygame.transform.scale(Captain_France, (100,100))

# Get the dimensions of the image
Captain_France_width, Captain_France_height = Captain_France.get_size()




#extracts the background from file
background_image = pygame.image.load("Dungeon_Texture.jpg")
background_image = pygame.transform.scale(background_image, (300,150))

# Get the dimensions of the background image
background_image_width, background_image_height = background_image.get_size()


#extracts the Captain_france_dos from file
Captain_France_dos = pygame.image.load("Captain_France_dos.png")
Captain_France_dos = pygame.transform.scale(Captain_France_dos, (100,100))

# Get the dimensions of the Captain_dos
Captain_France_dos_width, Captain_France_dos_height = Captain_France_dos.get_size()

# Movement flags



# Set the maximum frame rate
clock = pygame.time.Clock()
FPS = 5


def startGame() :
    running = True
    facing_up = 0
    move_up = False
    move_down = False
    move_left = False
    move_right = False
    player1 = Class_Player.Player.__init__("Geralt",[0,0],40)
    
    while running:
        
        #if X is pressed then close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    

            #Handle keyboard events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move_up = True
                elif event.key == pygame.K_a:
                    move_left = True
                elif event.key == pygame.K_s:
                    move_down = True
                elif event.key == pygame.K_d:
                    move_right = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    move_up = False
                elif event.key == pygame.K_a:
                    move_left = False
                elif event.key == pygame.K_s:
                    move_down = False
                elif event.key == pygame.K_d:
                    move_right = False

        # Update character position based on movement flags
        if move_up and player1.position[1] > 0:
            player1.position[1] -= player1.speed
            facing_up=1
        if move_left and player1.position[0] > 0:
            player1.position[0] -= player1.speed
        if move_down and player1.position[1] < pixelSize[1] - Captain_France_height:
            player1.position[1] += player1.speed
        if move_right and player1.position[0] < pixelSize[0] - Captain_France_width:
            player1.position[0] += player1.speed




    

        # Draw the background on the screen

        for i in range (pixelSize[0]):
            for j in range (pixelSize[1]):
                if (j%150 == 0 and i%300 == 0):
                    screen.blit(background_image,(i,j))
            

    
        # Draw the image on the screen if facing up is = 0
        if (facing_up == 0):
            screen.blit(Captain_France, (player1.position[0], player1.position[1]))
        elif(facing_up == 1):
            screen.blit(Captain_France_dos, (player1.position[0], player1.position[1]))
        # Draw the cap's back on the screen
    
    
        facing_up = 0

        # Update the screen
        pygame.display.update()

        # Delay to control the frame rate
        clock.tick(FPS)
    
    # Quit Pygame
    pygame.quit()


    

    