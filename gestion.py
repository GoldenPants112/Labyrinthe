import pygame
import Player
import Room
import menu
import random

from pygame import mixer




def nextRoom(_currentRoom):
    #prend la salel actuel et retourne une nouvelle salle construite

    nxt_room_Id = _currentRoom.roomId
    nxt_room_Id += 1
    nxt_room = Room.Room(nxt_room_Id)
    return nxt_room

def startGame(_screen,_taille_ecran) :
    running = True
    clock = pygame.time.Clock()
    FPS = 5

    #création de la première salle
    first_R = Room.Room(1)
    current_R = first_R
    Size_Tile = _taille_ecran[1]/current_R.size

    #check ou est l'entree et place le joueur a celle ci (init depart)
    for k in range(first_R.size) :
        for l in range(first_R.size) :
            if first_R.map[k][l].type == 3:
                speed=int(1)
                start_pos = [k,l]
                player_1 = Player.Player("Hicham",start_pos,speed)

     #Instantiate mixer
    mixer.init()

    #Load audio file
    mixer.music.load('Sound/Diablo2.mp3')

    #Set preferred volume
    mixer.music.set_volume(0.1)

    #Play the music
    mixer.music.play()

    play_button = pygame.image.load("Buttons\Play.png")
    menu_bg = pygame.image.load("Buttons\Fond_menu.png")
    
    menu.main_menu(_screen,_taille_ecran,play_button,menu_bg)
    
    game(_screen,_taille_ecran,player_1,clock,FPS,running,current_R,Size_Tile)





def game(_screen,_taille_ecran,player_1,clock,FPS,_running,_current_R,_Size_Tile) :

    # Create a font object
    font = pygame.font.Font("Font/Raleway-Regular.ttf", 22)

    #set the textures    
    character_dos = pygame.image.load("Assets/Captain_France_dos.png")
    character = pygame.image.load("Assets/Captain_France.png")
    background_image = pygame.image.load("Assets/Dungeon_Texture.jpg")
    character_right = pygame.image.load("Assets/Captain_France_right.png")
    character_left = pygame.image.load("Assets/Captain_France_left.png")
    curseur_surface= pygame.image.load("Buttons/Curseur.png").convert_alpha()
    resume_button = pygame.image.load("Buttons\Resume.png")
    pause_button = pygame.image.load("Buttons\Bouton_menu.png")
    pause_bg = pygame.image.load("Buttons\Back_menu.png")

    #scaling of the assets
    character_dos = pygame.transform.scale(character_dos, ( _Size_Tile, _Size_Tile))
    character = pygame.transform.scale(character, ( _Size_Tile, _Size_Tile))
    background_image = pygame.transform.scale(background_image, (2*_Size_Tile, _Size_Tile))
    character_right = pygame.transform.scale(character_right, ( _Size_Tile, _Size_Tile))
    character_left = pygame.transform.scale(character_left, ( _Size_Tile, _Size_Tile))
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

    walk_sound = mixer.Sound('Sound/Walk.wav')
    level_up_sound_effect = mixer.Sound('Sound/Level_Up_Sound_Effect.mp3')
    lighting_sound=mixer.Sound('Sound/Lightning.mp3')
    
    time_0=pygame.time.get_ticks()
    

    time_pause=0
    while _running:
        
        #gets the time in seconds since the init
        time = pygame.time.get_ticks()
     
        #check si le joueur est à la sortie
        if _current_R.map[player_1.position[0]][player_1.position[1]].type == 4 :
            #stocker le temps de chargemetn pour optimiser le temps
            time_chargement_start=time
            if _current_R.roomId == 6 :
                end_menu_bg = pygame.image.load("Buttons\Fond_menu.png")
                menu.endgame(_screen,_taille_ecran,end_menu_bg)

            _current_R  = nextRoom(_current_R)
            time = pygame.time.get_ticks()
            time_chargement_end=time
            time_chargement = time_chargement_end-time_chargement_start
            
            mixer.Sound.play(level_up_sound_effect)

            #check ou est l'entree est l'entree et place  joueur dedans
            for k in range (_current_R.size) :
                for l in range (_current_R.size) :
                    if _current_R.map[k][l].type == 3:
                        player_1.position[0] = k
                        player_1.position[1] = l                   

      # Draw the background on the _screen
        for i in range(0,_taille_ecran[0]):
            for j in range(0,_taille_ecran[0]):
                if (j% (_Size_Tile) == 0 and i%(2*_Size_Tile) == 0):
                    _screen.blit(background_image,(i,j))

        #met à jour la taille des textures  (pratique lorsque qu'on change de salle avec des salles de taille différentes)
        _Size_Tile =  _taille_ecran[1]//_current_R.size

        character = pygame.transform.scale(character, (_Size_Tile,_Size_Tile))
        character_dos = pygame.transform.scale(character_dos, (_Size_Tile,_Size_Tile))
        character_left = pygame.transform.scale(character_left, (_Size_Tile,_Size_Tile))
        character_right = pygame.transform.scale(character_right, (_Size_Tile,_Size_Tile))

        #récupère la taille d'une des textures (pour les colisions)
        character_width, character_height = character.get_size()

       
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

            if (event.type == pygame.MOUSEBUTTONUP and mouse_pos[0] > 30 and mouse_pos[0] < 60 and mouse_pos[1] > 30 and mouse_pos[1] < 60) or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                        time_pause_start = time
                        menu.pause_menu(_screen,_taille_ecran,resume_button,pause_bg)
                        time = pygame.time.get_ticks()
                        time_pause_end=time
                        time_pause = time_pause_end-time_pause_start+time_pause

        # Update character position and set oirentation flags, based on movement flags and the type of the next tile
        if move_up and player_1.position[1] > 0 and _current_R.map[player_1.position[0]][player_1.position[1]-1].type != 1:
            player_1.position[1] -= player_1.speed
            facing_up=1
            mixer.Sound.play(walk_sound)

        if move_left and player_1.position[0] > 0 and _current_R.map[player_1.position[0]-1][player_1.position[1]].type != 1:
            player_1.position[0] -= player_1.speed
            facing_left=1
            mixer.Sound.play(walk_sound)

        if move_down and player_1.position[1] < (_taille_ecran[1] - character_height) and _current_R.map[player_1.position[0]][player_1.position[1]+1].type != 1:
            player_1.position[1] += player_1.speed
            facing_down=1
            mixer.Sound.play(walk_sound)

        if move_right and player_1.position[0] < (_taille_ecran[0] - character_width) and _current_R.map[player_1.position[0]+1][player_1.position[1]].type != 1:
            player_1.position[0] += player_1.speed
            facing_right=1 
            mixer.Sound.play(walk_sound)

        # Draw the rigth texture after the right orientation flag
        if (facing_down == 1):
            player_1.__repr__(character,_screen,_Size_Tile)

        elif(facing_up == 1):# Draw the cap's back on the screen
            player_1.__repr__(character_dos,_screen,_Size_Tile)

        elif(facing_right == 1): # Draw the Captain Franace right on the screen
            player_1.__repr__(character_right,_screen,_Size_Tile)

        elif(facing_left == 1): # Draw the Captain Frnace left on the screen
            player_1.__repr__(character_left,_screen,_Size_Tile)
        else:
            player_1.__repr__(character,_screen,_Size_Tile)
    
        #réinitialisation des flags après mouvment
        facing_up = 0
        facing_left = 0 
        facing_right = 0
        facing_down = 0
        color_brouillard=(0,0,0)

        #tonnaire qui permets au joueur de voir la salle en entier pour un image
        lighting=random.randint(0,200)

             #affiche la salle
        _current_R.__repr__(_screen,_Size_Tile)
        
        #pygame.draw.rect( ecran , couleur , Pygame.Rect( x , y , largeur , hauteur ))  -- les coord x et y étants les coordonées du coins en haut à gauche du rectangle.
        #affichage de la tialle du brouillard en fonciton de l'iD de la salle
        if (_current_R.roomId == 1 or _current_R.roomId == 2) and lighting != 1:
            pygame.draw.rect(_screen,color_brouillard, pygame.Rect(0 , 0 , (player_1.position[0] +2 )*_Size_Tile , (player_1.position[1] -1 )*_Size_Tile ))
            pygame.draw.rect(_screen,color_brouillard, pygame.Rect( (player_1.position[0] +2)*_Size_Tile , 0 , _taille_ecran[0] - (player_1.position[0] +2)*_Size_Tile , (player_1.position[1]+2)*_Size_Tile  ) )
            pygame.draw.rect(_screen,color_brouillard, pygame.Rect( (player_1.position[0] -1 )*_Size_Tile , (player_1.position[1]+2)*_Size_Tile , _taille_ecran[0]  - (player_1.position[0] -1)*_Size_Tile , _taille_ecran[0] - (player_1.position[1] +2)*_Size_Tile ) ) 
            pygame.draw.rect(_screen,color_brouillard,pygame.Rect( 0 , (player_1.position[1] -1 )*_Size_Tile , (player_1.position[0]-1)*_Size_Tile , _taille_ecran[0]  - (player_1.position[1]-1)*_Size_Tile ))

        elif (_current_R.roomId == 3 or  _current_R.roomId == 4 or  _current_R.roomId == 5 or _current_R.roomId == 6) and lighting!=1:       
            pygame.draw.rect(_screen,color_brouillard, pygame.Rect(0 , 0 , (player_1.position[0] +3 )*_Size_Tile , (player_1.position[1] -2 )*_Size_Tile ))
            pygame.draw.rect(_screen,color_brouillard, pygame.Rect( (player_1.position[0] +3)*_Size_Tile , 0 , _taille_ecran[0] - (player_1.position[0] +3)*_Size_Tile , (player_1.position[1]+3)*_Size_Tile  ) )
            pygame.draw.rect(_screen,color_brouillard, pygame.Rect( (player_1.position[0] -2 )*_Size_Tile , (player_1.position[1]+3)*_Size_Tile , _taille_ecran[0]  - (player_1.position[0] -2)*_Size_Tile , _taille_ecran[0] - (player_1.position[1] +3)*_Size_Tile ) ) 
            pygame.draw.rect(_screen,color_brouillard,pygame.Rect( 0 , (player_1.position[1] -2 )*_Size_Tile , (player_1.position[0]-2)*_Size_Tile , _taille_ecran[0]  - (player_1.position[1]-2)*_Size_Tile ))
        elif lighting ==1 :
            mixer.Sound.play(lighting_sound)


        #afficher le curseur adequat
        curseur=pygame.cursors.Cursor((0,0),curseur_surface)
        pygame.mouse.set_cursor(curseur)
            
        _screen.blit(pause_button,(30,30))
            
     
    
                    
        



        if _current_R.roomId == 1:
                # Render the time as text
            lv1_time_text = font.render(f"Time : {(time-time_pause-time_0)/1000} ", True, (255, 255, 255))

            # Blit the rendered text onto the _screen
            _screen.blit(lv1_time_text, (_taille_ecran[0] - 140, 10))

        elif _current_R.roomId == 2 :
            lvl2_time_text = font.render(f"Time : {(time-time_pause-time_0 - time_1-time_chargement)/1000} ", True, (255, 255, 255))
            _screen.blit(lvl2_time_text, (_taille_ecran[0] - 140, 10))

        elif _current_R.roomId == 3:
            lvl3_time_text = font.render(f"Time : {(time -time_pause-time_0-time_1-time_2-time_chargement)/1000} ", True, (255, 255, 255))
            _screen.blit(lvl3_time_text, (_taille_ecran[0] - 140, 10))

        elif _current_R.roomId == 4:
            lvl4_time_text = font.render(f"Time : {(time-time_pause-time_0-time_1-time_2-time_3-time_chargement)/1000} ", True, (255, 255, 255))
            _screen.blit(lvl4_time_text, (_taille_ecran[0] - 140, 10))

        elif _current_R.roomId == 5:
            lvl5_time_text = font.render(f"Time : {(time-time_pause-time_0-time_1-time_2-time_3-time_4-time_chargement)/1000} ", True, (255, 255, 255))
            _screen.blit(lvl5_time_text, (_taille_ecran[0] - 140, 10))

        elif _current_R.roomId == 6:
            lvl6_time_text = font.render(f"Time : {(time-time_pause-time_0-time_1-time_2-time_3-time_4-time_5-time_chargement)/1000} ", True, (255, 255, 255))
            _screen.blit(lvl6_time_text, (_taille_ecran[0] - 140, 10))


        if _current_R.map[player_1.position[0]][player_1.position[1]].type == 4 :
            #afiichage du temps requit pour finir une salle
            if _current_R.roomId == 1:
                time_1=time-time_pause-time_0
                lvl1_accomplished_time = font.render(f"Time to complete level 1: {time_1/1000} ", True, (0, 255, 0))
                _screen.blit(lvl1_accomplished_time,((_taille_ecran[0] - 330, 50)))

            if _current_R.roomId == 2:
                time_2=time-time_pause-time_0-time_1
                lvl2_accomplished_time = font.render(f"Time to complete level 2: {time_2/1000} ", True, (0, 255, 0))
                _screen.blit(lvl2_accomplished_time,((_taille_ecran[0] - 330, 50)))

            if _current_R.roomId == 3:
                time_3=time-time_pause-time_0-time_1-time_2
                lvl3_accomplished_time = font.render(f"Time to complete level 3: {time_3/1000} ", True, (0, 255, 0))
                _screen.blit(lvl3_accomplished_time,((_taille_ecran[0] - 330, 50)))

            if _current_R.roomId == 4:
                time_4=time-time_pause-time_0-time_1-time_2-time_3
                lvl4_accomplished_time = font.render(f"Time to complete level 4: {time_4/1000} ", True, (0, 255, 0))
                _screen.blit(lvl4_accomplished_time,((_taille_ecran[0] - 330, 50)))

            if _current_R.roomId == 5:
                time_5=time-time_pause-time_0-time_1-time_2-time_3-time_4
                lvl5_accomplished_time = font.render(f"Time to complete level 5: {time_5/1000} ", True, (0, 255, 0))
                _screen.blit(lvl5_accomplished_time,((_taille_ecran[0] - 330, 50)))

            if _current_R.roomId == 6:
                time_6=time-time_pause-time_0-time_1-time_2-time_3-time_4-time_5
                lvl6_accomplished_time = font.render(f"Time to complete level 6: {time_6/1000} ", True, (0, 255, 0))
                _screen.blit(lvl6_accomplished_time,((_taille_ecran[0] - 330, 50)))

        # Update the entire display
        pygame.display.flip()
        #verfie si la souris est a la position du bouton pause
        #for event in pygame.event.get():
            
       
       

        # Update the _screen
        pygame.display.update()

        mouse_pos = pygame.mouse.get_pos()
       
        # Delay to control the frame rate
        clock.tick(FPS)
    # Quit Pygame
    pygame.quit()