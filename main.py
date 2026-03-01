import pygame

# Charger les composants à l'intérieur de pygame
pygame.init()

#  Class Game qui va réprésenter le jeu
class Game():
    def __init__(self):
        # Générer le joueur
        self.player = Player()


# Représentation joueur avec une class
class Player(pygame.sprite.Sprite ):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

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