import pygame
import Class_Player
import Class_Room
import menu
from pygame import mixer


def nextRoom(_currentRoom):
    #prend la salel actuel et retourne une nouvelle salle construite

    nxt_room_Id = _currentRoom.roomId
    nxt_room_Id += 1
    nxt_room = Class_Room.Room(nxt_room_Id)
    return nxt_room

def startGame(_taille_ecran) :
    running = True
    clock = pygame.time.Clock()
    FPS = 6

    #création de la première salle
    first_R = Class_Room.Room(1)
    current_R = first_R
    Size_Tile = _taille_ecran[1]/current_R.size

    #check ou est l'entree et place le joueur a celle ci (init depart)
    for k in range(first_R.size) :
        for l in range(first_R.size) :
            if first_R.map[k][l].type == 3:
                speed=int(1)
                start_pos = [k,l]
                player_1 = Class_Player.Player("Hicham",start_pos,speed)

     #Instantiate mixer
    mixer.init()

    #Load audio file
    mixer.music.load('Soundtrack/Diablo2.mp3')

    print("music started playing....")

    #Set preferred volume
    mixer.music.set_volume(0.7)

    #Play the music
    mixer.music.play()

    play_button = pygame.image.load("Buttons\Play.png")
    menu_bg = pygame.image.load("Buttons\Fond-menu.png")
    
    menu.main_menu(screen,_taille_ecran,play_button,menu_bg)

    Game(_taille_ecran,player_1,clock,FPS,running,current_R,Size_Tile)
    

def Game(_taille_ecran,player_1,clock,FPS,_running,_current_R,_Size_Tile) :

 #set the textures    
    Captain_France_dos = pygame.image.load("Assets/Captain_France_dos.png")
    Captain_France = pygame.image.load("Assets/Captain_France.png")
    background_image = pygame.image.load("Assets/Dungeon_Texture.jpg")
    Captain_France_right = pygame.image.load("Assets/Captain_France_right.png")
    Captain_France_left = pygame.image.load("Assets/Captain_France_left.png")
    curseur_surface= pygame.image.load("Buttons/Curseur.png").convert_alpha()
    play_button = pygame.image.load("Buttons\Play.png")
    menu_bg = pygame.image.load("Buttons\Fond-menu.png")
    resume_button = pygame.image.load("Buttons\Resume.png")
    pause_button = pygame.image.load("Buttons\Bouton_menu.png")
    pause_bg = pygame.image.load("Buttons\Back_menu.png")

    #scaling of the assets
    Captain_France_dos = pygame.transform.scale(Captain_France_dos, ( _Size_Tile, _Size_Tile))
    Captain_France = pygame.transform.scale(Captain_France, ( _Size_Tile, _Size_Tile))
    background_image = pygame.transform.scale(background_image, (2*_Size_Tile, _Size_Tile))
    Captain_France_right = pygame.transform.scale(Captain_France_right, ( _Size_Tile, _Size_Tile))
    Captain_France_left = pygame.transform.scale(Captain_France_left, ( _Size_Tile, _Size_Tile))
    pause_button = pygame.transform.scale(pause_button, (30,30))

    curseur_surface= pygame.transform.scale(curseur_surface, (30,30))

    # set Movement flags
    move_up = False
    move_down = False
    move_left = False
    move_right = False

    # set orientation Flags (pour les textures)
    facing_up = 0
    facing_right = 0
    facing_left = 0
    facing_down = 0

    
    while _running:
        
        #gets the time in seconds since the init
        time = pygame.time.get_ticks()

        if _current_R.roomId == 1:
            print((time)/1000)
        elif _current_R.roomId == 2 :
            print((time - time_1)/1000)
        elif _current_R.roomId == 3:
            print((time -time_1-time_2)/1000)
        elif _current_R.roomId == 4:
            print((time-time_1-time_2-time_3)/1000)
        elif _current_R.roomId == 5:
            print((time-time_1-time_2-time_3-time_4)/1000)





        #check si le joueur est à la sortie
        if _current_R.map[player_1.position[0]][player_1.position[1]].type == 4 :
            #afiichage du temps requit pour finir une salle
            if _current_R.roomId == 1:
                time_1=time
                print("Fin du premier niveau") 
                print(time_1/1000)
            if _current_R.roomId == 2:
                time_2=time-time_1
                print("Fin du deuxieme niveau")
                print(time_2/1000)
            if _current_R.roomId == 3:
                time_3=time-time_2-time_1
                print("Fin du troiseme niveau")
                print(time_3/1000)
            if _current_R.roomId == 4:
                time_4=time-time_3-time_2-time_1
                print("Fin du quatrieme niveau")
                print(time_4/1000)
            if _current_R.roomId == 5:
                time_5=time-time_4-time_3-time_2-time_1
                print("Fin du cinquieme niveau")
                print(time_5/1000)


            _current_R  = nextRoom(_current_R)
            #check ou est l'entree est l'entree et place  joueur dedans
            for k in range (_current_R.size) :
                for l in range (_current_R.size) :
                    if _current_R.map[k][l].type == 3:
                        player_1.position[0] = k
                        player_1.position[1] = l                   

      # Draw the background on the screen
        for i in range(0,_taille_ecran[0]):
            for j in range(0,_taille_ecran[0]):
                if (j% (_Size_Tile) == 0 and i%(2*_Size_Tile) == 0):
                    screen.blit(background_image,(i,j))

        #met à jour la taille des textures  (pratique lorsque qu'on change de salle avec des salles de taille différentes)
        _Size_Tile =  _taille_ecran[1]//_current_R.size

        Captain_France = pygame.transform.scale(Captain_France, (_Size_Tile,_Size_Tile))
        Captain_France_dos = pygame.transform.scale(Captain_France_dos, (_Size_Tile,_Size_Tile))
        Captain_France_left = pygame.transform.scale(Captain_France_left, (_Size_Tile,_Size_Tile))
        Captain_France_right = pygame.transform.scale(Captain_France_right, (_Size_Tile,_Size_Tile))

        #récupère la taille d'une des textures (pour les colisions)
        Captain_France_width, Captain_France_height = Captain_France.get_size()

        #affiche la salle
        _current_R.__repr__(screen,_Size_Tile)
       
        #if X is pressed then close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _running = False    

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

        # Update character position and set oirentation flags, based on movement flags and the type of the next tile
        if move_up and player_1.position[1] > 0 and _current_R.map[player_1.position[0]][player_1.position[1]-1].type != 1:
            player_1.position[1] -= player_1.speed
            facing_up=1

        if move_left and player_1.position[0] > 0 and _current_R.map[player_1.position[0]-1][player_1.position[1]].type != 1:
            player_1.position[0] -= player_1.speed
            facing_left=1

        if move_down and player_1.position[1] < (_taille_ecran[1] - Captain_France_height) and _current_R.map[player_1.position[0]][player_1.position[1]+1].type != 1:
            player_1.position[1] += player_1.speed
            facing_down=1

        if move_right and player_1.position[0] < (_taille_ecran[0] - Captain_France_width) and _current_R.map[player_1.position[0]+1][player_1.position[1]].type != 1:
            player_1.position[0] += player_1.speed
            facing_right=1 

        # Draw the rigth texture after the right orientation flag
        if (facing_down == 1):
            player_1.__repr__(Captain_France,screen,_Size_Tile)

        elif(facing_up == 1):# Draw the cap's back on the screen
            player_1.__repr__(Captain_France_dos,screen,_Size_Tile)

        elif(facing_right == 1): # Draw the Captain Franace right on the screen
            player_1.__repr__(Captain_France_right,screen,_Size_Tile)

        elif(facing_left == 1): # Draw the Captain Frnace left on the screen
            player_1.__repr__(Captain_France_left,screen,_Size_Tile)
        else:
            player_1.__repr__(Captain_France,screen,_Size_Tile)
    
        #réinitialisation des flags après mouvment
        facing_up = 0
        facing_left = 0 
        facing_right = 0
        facing_down = 0
        color_brouillard=(0,0,0)
 
        #pygame.draw.rect( ecran , couleur , Pygame.Rect( x , y , largeur , hauteur ))  -- les coord x et y étants les coordonées du coins en haut à gauche du rectangle.
        #affichage de la tialle du brouillard en fonciton de l'iD de la salle
        if _current_R.roomId == 1 or _current_R.roomId == 2:
            pygame.draw.rect(screen,color_brouillard, pygame.Rect(0 , 0 , (player_1.position[0] +2 )*_Size_Tile , (player_1.position[1] -1 )*_Size_Tile ))
            pygame.draw.rect(screen,color_brouillard, pygame.Rect( (player_1.position[0] +2)*_Size_Tile , 0 , _taille_ecran[0] - (player_1.position[0] +2)*_Size_Tile , (player_1.position[1]+2)*_Size_Tile  ) )
            pygame.draw.rect(screen,color_brouillard, pygame.Rect( (player_1.position[0] -1 )*_Size_Tile , (player_1.position[1]+2)*_Size_Tile , _taille_ecran[0]  - (player_1.position[0] -1)*_Size_Tile , _taille_ecran[0] - (player_1.position[1] +2)*_Size_Tile ) ) 
            pygame.draw.rect(screen,color_brouillard,pygame.Rect( 0 , (player_1.position[1] -1 )*_Size_Tile , (player_1.position[0]-1)*_Size_Tile , _taille_ecran[0]  - (player_1.position[1]-1)*_Size_Tile ))

        elif _current_R.roomId == 3 or  _current_R.roomId == 4 or  _current_R.roomId == 5:       
            pygame.draw.rect(screen,color_brouillard, pygame.Rect(0 , 0 , (player_1.position[0] +3 )*_Size_Tile , (player_1.position[1] -2 )*_Size_Tile ))
            pygame.draw.rect(screen,color_brouillard, pygame.Rect( (player_1.position[0] +3)*_Size_Tile , 0 , _taille_ecran[0] - (player_1.position[0] +3)*_Size_Tile , (player_1.position[1]+3)*_Size_Tile  ) )
            pygame.draw.rect(screen,color_brouillard, pygame.Rect( (player_1.position[0] -2 )*_Size_Tile , (player_1.position[1]+3)*_Size_Tile , _taille_ecran[0]  - (player_1.position[0] -2)*_Size_Tile , _taille_ecran[0] - (player_1.position[1] +3)*_Size_Tile ) ) 
            pygame.draw.rect(screen,color_brouillard,pygame.Rect( 0 , (player_1.position[1] -2 )*_Size_Tile , (player_1.position[0]-2)*_Size_Tile , _taille_ecran[0]  - (player_1.position[1]-2)*_Size_Tile ))

        #afficher le curseur adequat
        curseur=pygame.cursors.Cursor((0,0),curseur_surface)
        pygame.mouse.set_cursor(curseur)

        if pygame.mouse.get_pressed()[0] == 1 :
            mouse_pos = pygame.mouse.get_pos()
            #verfie si la souris est a la position du bouton pause
            if mouse_pos[0] > 30 and mouse_pos[0] < 60 :
                if mouse_pos[1] > 30 and mouse_pos[1] < 60 :
                    menu.pause_menu(screen,_taille_ecran,resume_button,pause_bg)

        screen.blit(pause_button,(30,30))

        # Update the screen
        pygame.display.update()

        # Delay to control the frame rate
        clock.tick(FPS)
   
    # Quit Pygame
    pygame.quit()


#Creation de la premiere fenetre
pygame.init()

#determination des dimentions de l'ecran
pixelSize = [700,700]
#Creation de l'ecran
screen = pygame.display.set_mode(pixelSize)

#debut de la partie
Game = startGame(pixelSize)






    