import pygame

class Player:
    def __init__(self,_name,_position,_speed):
        self.name = _name
        _position=[_position[0],_position[1]]
        self.position=_position
        self.speed = int(_speed)

    def __repr__(self,_texture,_ecran,_tailleTuile):
        _ecran.blit(_texture, (self.position[0]*_tailleTuile, self.position[1]*_tailleTuile))