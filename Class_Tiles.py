import Game  
import Class_Room
import pygame

class Tiles:
    type=0
    def __init__(self,_type):
        self.type=_type
    
    def __repr__(self,_tailleSalle):
        Taille_ecran = Game.pixelSize[0]
        
        # changer les rectangles de coouleurs pour des images ("textures") en utilisant la fonction :
        #                 - pygame.image.load("nom image") pour charger l'image (sûrement pas içi)
        #                 - screen.blit("nom image",(x,y) ) içi la taille sera la résolution totale divisé par la taille de la salle en question.

        if (self.type == 1001 ):
            pygame.draw.rect(Game.screen,(205,133,63),50,50) #dessin de sol de couleur rgb : 205,133,63
        if (self.type == 1002):
           pygame.draw.rect(Game.screen,(105,105,105),100,100) #dessins de mur de couleur rgb : 105,105,105
        if (self.type == 1003):
             pygame.draw.rect(Game.screen,(205,133,63),100,100) #dessins de porte fond rgb : 205,133,63 de couleur rgb : 

    #etc... 