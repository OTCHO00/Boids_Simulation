import pygame, sys
from config import HAUTEUR, LARGEUR, FPS
from boid import Boid

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Simulation de nuée d'oiseau")
boid = Boid()
pygame.display.flip()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    boid.update_position()
    boid.bordure()
    fenetre.fill((0, 0, 0))
    boid.draw(fenetre)
    pygame.display.flip()
    clock.tick(FPS)
    

