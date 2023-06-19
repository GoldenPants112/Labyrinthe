import pygame

def main_menu(_screen,_taille_ecran,_textu_play_button,_textu_menu_bg) :

    play_button_size = []  
    play_button_size.append(_taille_ecran[0]/5)
    play_button_size.append(_taille_ecran[1]/8) 

    play_button_pos = []  
    play_button_pos.append(_taille_ecran[0]/2 - play_button_size[0]/2)
    play_button_pos.append(_taille_ecran[1]/8) 
    
    _textu_play_button = pygame.transform.scale(_textu_play_button,(play_button_size[0] , play_button_size[1]) )
    _textu_menu_bg =  pygame.transform.scale(_textu_menu_bg,(_taille_ecran[0] , _taille_ecran[1] ) )

     #affiche le menu principal
    _screen.blit(_textu_play_button,(  play_button_pos[0],  play_button_pos[1]  ))
    _screen.blit(_textu_menu_bg,(0,0))
    
    checker = 1 
    while checker == 1 :
    
        ##pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()
        #verifie si le joueur active un outon de la souris
        if pygame.mouse.get_pressed()[0] == 1 :
            #verfie si la souris est a la position du bouton play
            if mouse_pos[0] > (play_button_pos[0]) and mouse_pos[0] < (play_button_pos[0] + play_button_size[0]) :
                if mouse_pos[1] > (play_button_pos[1]) and mouse_pos[1] < (play_button_pos[1] + play_button_size[1]) :
                    checker = 0
            #rajouter d'éventuels autres boutons

        pygame.display.update()   

def pause_menu(_screen,_taille_ecran,_textu_resume_button,_textu_pause_bg) :
    #on définie les dimensions des membres du menu
    pause_menu_size = []
    pause_menu_size.append( _taille_ecran[0]/3)
    pause_menu_size.append( _taille_ecran[0]/5)

    resume_button_size = []
    resume_button_size.append(60)
    resume_button_size.append(60)
    
    #on définie les positions des membres du menu
    pause_menu_pos = []
    pause_menu_pos.append( (_taille_ecran[0]/2)-(pause_menu_size[0]/2))
    pause_menu_pos.append( (_taille_ecran[0]/2)-(pause_menu_size[1]) )

    resume_button_pos = []
    resume_button_pos.append(_taille_ecran[0]/2-resume_button_size[0] ) 
    resume_button_pos.append((_taille_ecran[1]/2)-(pause_menu_size[1])+70)

    _textu_resume_button =  pygame.transform.scale(_textu_resume_button,( resume_button_size[0] , resume_button_size[1] ))
    _textu_pause_bg = pygame.transform.scale(_textu_pause_bg,( pause_menu_size[0] , pause_menu_size[1] ) )

    _screen.blit(_textu_pause_bg , ( pause_menu_pos[0] , pause_menu_pos[1] ))
    _screen.blit(_textu_resume_button, ( resume_button_pos[0] , resume_button_pos[1] ))

    checker = 1
    
    while checker == 1 :
        mouse_pos = pygame.mouse.get_pos()
        #verifie si le joueur active un outon de la souris
        if pygame.mouse.get_pressed()[0] == 1 :
            #verfie si la souris est a la position du bouton play
            if mouse_pos[0] > (resume_button_pos[0]) and mouse_pos[0] < (resume_button_pos[0]+resume_button_size[0]) :
                if mouse_pos[1] > (resume_button_pos[1])  and mouse_pos[1] < (resume_button_pos[1]+resume_button_size[1]) :
                        checker = 0
