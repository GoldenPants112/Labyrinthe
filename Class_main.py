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
Captain_France = pygame.transform.scale(Captain_France, (100,100))
# Get the dimensions of the Captain
Captain_France_width, Captain_France_height = Captain_France.get_size()
#cordonne du CAptain
Captain_France_x=(pixelSize[0] - Captain_France_width) // 2
Captain_France_y=(pixelSize[1] - Captain_France_height) // 2


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
#cordonne du Captain dos
Captain_France_dos_x=(pixelSize[0] - Captain_France_dos_width) // 2
Captain_France_dos_y=(pixelSize[1] - Captain_France_dos_height) // 2



running = True

#spped of the caracter
Captain_France_speed = 40

# Movement flags
move_up = False
move_down = False
move_left = False
move_right = False

# Set the maximum frame rate
clock = pygame.time.Clock()
FPS = 5
facing_up=0

while running:
    #if X is pressed then close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


      # Handle keyboard events
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
    if move_up and Captain_France_y > 0:
        Captain_France_y -= Captain_France_speed
        facing_up=1
    if move_left and Captain_France_x > 0:
        Captain_France_x -= Captain_France_speed
    if move_down and Captain_France_y < pixelSize[1] - Captain_France_height:
        Captain_France_y += Captain_France_speed
    if move_right and Captain_France_x < pixelSize[0] - Captain_France_width:
        Captain_France_x += Captain_France_speed




    # Fill the screen with the background color
    #screen.fill(background_color)

    # Draw the background on the screen

    screen.blit(background_image,(0,0))
    screen.blit(background_image,(300,0))
    screen.blit(background_image,(600,0))
    screen.blit(background_image,(0,150))
    screen.blit(background_image,(0,300))
    screen.blit(background_image,(0,450))
    screen.blit(background_image,(0,600))
    screen.blit(background_image,(300,150))
    screen.blit(background_image,(300,300))
    screen.blit(background_image,(300,450))
    screen.blit(background_image,(300,600))
    screen.blit(background_image,(600,150))
    screen.blit(background_image,(600,300))
    screen.blit(background_image,(600,450))
    screen.blit(background_image,(600,600))



    
    # Draw the image on the screen if facing up is = 0
    if (facing_up == 0):
        screen.blit(Captain_France, (Captain_France_x, Captain_France_y))
    elif(facing_up == 1):
        screen.blit(Captain_France_dos, (Captain_France_x, Captain_France_y))
    # Draw the cap's back on the screen
    
    
    facing_up = 0

    # Update the screen
    pygame.display.update()

    # Delay to control the frame rate
    clock.tick(FPS)

    
# Quit Pygame
pygame.quit()
    