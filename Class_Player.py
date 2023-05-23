import Game
import pygame

class Player:
    def __init__(self,_name,_position,_speed):
        self.name = _name
        self.position=_position
        self.speed = _speed

    def __repr__(self,_texture):
        Game.screen.blit(_texture, (self.position[0], self.position[1]))