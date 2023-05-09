import pygame
class Tiles:
    position=[0.0]
    type=0
    def __init__(self,_position,_type):
        self.position=_position
        self.type=_type
    
    def __repr__(self):
        if (self.type == 1001) : # 1001 représente la case mur
            pygame.draw.rectangle
