import pygame
from game import Game

# Charger les composants à l'intérieur de pygame
pygame.init()

# Générer fenêtre
pygame.display.set_caption("Commet Fall Game") # Titre de la fenêtre
screen = pygame.display.set_mode((1080,720)) #Définition dimension fenêtre

# Charger l'arrière plan
background = pygame.image.load('assets/bg.jpg')

# Charger le jeu
game = Game()

#Boucle du jeu
running = True
while running:
    # Appliquer l'arrière plan
    screen.blit(background, (0, -200))

    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Mettre à jour la fenêtre
    pygame.display.flip()

    #Si le joueur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #si fermeture de fenêtre
            running = False
            pygame.quit()