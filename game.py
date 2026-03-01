import pygame
from player import Player

#  Class Game qui va réprésenter le jeu
class Game():
    def __init__(self):
        # Générer le joueur
        self.player = Player()
        self.pressed = {}