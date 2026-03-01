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

    # Vérifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()

    # Mettre à jour la fenêtre
    pygame.display.flip()

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #si fermeture de fenêtre
            running = False
            pygame.quit()
        # Détecter si un joueur lâche un touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False