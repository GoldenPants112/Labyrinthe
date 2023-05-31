import pygame

class Tiles:
    def __init__(self,_type):
        self.type=_type
        self.txtu_mur = pygame.image.load("Assets/Mur.png")
        self.txtu_entree = pygame.image.load("Assets/Porte_entree.png")
        self.txtu_sortie = pygame.image.load("Assets/Prote_sortie.png")

    def __repr__(self,_ecran,_sizeTile,_posx,posy):
        #affiche un mur si le type est le bon
        if self.type == 1 :
            self.txtu_mur = pygame.transform.scale(self.txtu_mur, ( _sizeTile , _sizeTile ))
            _ecran.blit(self.txtu_mur,( _posx * _sizeTile , posy * _sizeTile ))
        
        #affiche la porte d'entrere si le type est le bon
        if self.type == 3 :
            self.txtu_mur = pygame.transform.scale(self.txtu_entree, ( _sizeTile , _sizeTile ))
            _ecran.blit(self.txtu_entree,( _posx * _sizeTile , posy * _sizeTile ))

        #affiche la porte de sortie si le type est le bon
        if self.type == 4 :
            self.txtu_mur = pygame.transform.scale(self.txtu_sortie, ( _sizeTile , _sizeTile ))
            _ecran.blit(self.txtu_sortie,( _posx * _sizeTile , posy * _sizeTile ))