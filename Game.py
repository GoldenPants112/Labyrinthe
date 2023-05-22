import Class_Room
import pygame
import Class_Player



def nextRoom(_currentRoom):
    nxt_room = _currentRoom.roomID +1
    
    return Class_Room.Room.__init__(nxt_room)


def startGame(_taille_ecran) :
    running = True
    clock = pygame.time.Clock()
    FPS = 5

    first_R = Class_Room.Room.__init__(1)
    
    #check ou est l'entree et place le joueur à celle ci (init depart)
    for k in range (first_R.size) :
        for l in range (first_R.size) :
            if first_R.map[k,l].type == 1003:
                player_1 = Class_Player.Player.__init__("Geralt",[k,l],1)

    

    current_R = first_R
    Size_Tile = _taille_ecran/current_R.size

    #set the textures    
    Captain_France = pygame.image.load("Captain_France_dos.png")
    Captain_France = pygame.image.load("Captain_France.png")
    background_image = pygame.image.load("Dungeon_Texture.jpg")

    

    Captain_France = pygame.transform.scale(Captain_France, ( Size_Tile, Size_Tile))
    Captain_France = pygame.transform.scale(Captain_France, ( Size_Tile, Size_Tile))
    background_image = pygame.transform.scale(background_image, (Size_Tile,Size_Tile/2))
    

    #extracts the background from file



    # set Movement flags
    move_up = False
    move_down = False
    move_left = False
    move_right = False

    # set orientation Flags (pour les textures)
    facing_up = 0
    

    while running:

        if current_R.map[player_1.position[0],player_1.position[1]] == 1004 :
            current_R = nextRoom(current_R)
            #check ou est l'entree est l'entree et place  joueur dedans
            for k in range current_R.size :
                for l in range current_R.size :
                    if first_R.map[k,l].type == 1003:
                        player_1.position
                    

        Size_Tile =  _taille_ecran/current_R.size

        Captain_France_dos = pygame.transform.scale(Captain_France_dos, (Size_Tile,Size_Tile))
        Captain_France_width, Captain_France_height = Captain_France.get_size()

        Captain_France_dos = pygame.transform.scale(Captain_France_dos, (Size_Tile,Size_Tile))

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

         

        # Update character position based on movement flags and the type of the next tile
        if move_up and player_1.position[1] > 0 and current_R.map[player_1.position[1]-1 ].type != 1002:
            player_1.position[1] -= player_1.speed * Size_Tile
            facing_up=1
        if move_left and player_1.position[0] > 0 and current_R.map[player_1.position[0]-1].type != 1002:
            player_1.position[0] -= player_1.speed * Size_Tile
        if move_down and player_1.position[1] < _taille_ecran[1] - Captain_France_height and current_R.map[player_1.position[1] +1 ].type != 1002:
            player_1.position[1] += player_1.speed * Size_Tile
        if move_right and player_1.position[0] < _taille_ecran[0] - Captain_France_width and current_R.map[player_1.position[0] +1 ].type != 1002:
            player_1.position[0] += player_1.speed * Size_Tile


    

        # Draw the background on the screen

        for i in range (_taille_ecran[0]):
            for j in range (_taille_ecran[1]):
                if (j%Size_Tile/2 == 0 and i%Size_Tile == 0):
                    screen.blit(background_image,(i,j))
            

        #check la position du joueur si le joueur va dans le mur ou non

    
        # Draw the image on the screen if facing up is = 0
        if (facing_up == 0):
            screen.blit(Captain_France, (player_1.position[0], player_1.position[1]))
        # Draw the cap's back on the screen
        elif(facing_up == 1):
            screen.blit(Captain_France_dos, (player_1.position[0], player_1.position[1]))
        
        facing_up = 0



        # Update the screen
        pygame.display.update()

        # Delay to control the frame rate
        clock.tick(FPS)
    
    # Quit Pygame
    pygame.quit()



Game = startGame(pixelSize)

#Creation de la premiere fenetre
pygame.init()
#determination des dimentions de l'ecran
pixelSize = (700,700)

#Creation de l'ecran
screen = pygame.display.set_mode(pixelSize)



# Get the dimensions of the background image
background_image_width, background_image_height = background_image.get_size()





    