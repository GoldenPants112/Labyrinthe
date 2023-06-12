import pygame

def update_menu(_menu_Id,_screen,_taille_ecran) :

    textu_play = pygame.image.load("Buttons\Resume.png")

    textu_play = pygame.transform.scale(textu_play,(_taille_ecran[0]/5 , _taille_ecran[1]/8) )
    
    if _menu_Id == 1 :
           #affiche le menu principal
        pygame.draw.rect(_screen,(10,10,10), pygame.Rect(0 , 0 , _taille_ecran[0], _taille_ecran[1]))
        _screen.blit(textu_play,( (_taille_ecran[0]/2) , _taille_ecran[1]*2/5  ))
        

    while _menu_Id == 1 :
        #verifie la prochaine action du joueur (sur quel bouton il appuie)

        pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == 1 :
            #verfie si la souris est a la position du bouton play
            if mouse_pos[0] > (_taille_ecran[0]/2) and mouse_pos[0] < (_taille_ecran[0]/2 + _taille_ecran[0]/5) :
                if mouse_pos[1] > (_taille_ecran[1]*2/5) and mouse_pos[1] < (_taille_ecran[1]*2/5 +  _taille_ecran[1]/8) :
                    _menu_Id = 0

            #rajouter les autres cas (autres boutons avec leurs position) /!\


        pygame.display.update()
    
    
    while _menu_Id == 2 :
        #a completer
