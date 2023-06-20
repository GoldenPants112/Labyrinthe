import pygame
import pygame.font
import gestion

#Creation de la premiere fenetre
pygame.init()

#initialisation de pygame pour le texte 
pygame.font.init()

#determination des dimentions de l'ecran
resolution = [700,700]

#Creation de l'ecran
screen = pygame.display.set_mode(resolution)

#debut de la partie
Game = gestion.startGame(screen,resolution)
