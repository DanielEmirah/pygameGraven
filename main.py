import pygame

# Charger les composants à l'intérieur de pygame
pygame.init()

# Générer fenêtre
pygame.display.set_caption("Commet Fall Game") # Titre de la fenêtre
pygame.display.set_mode((1080,720)) #Définition dimension fenêtre

#Boucle du jeu
running = True
while running:
    #Si le joueur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #si fermeture de fenêtre
            running = False
            pygame.quit()