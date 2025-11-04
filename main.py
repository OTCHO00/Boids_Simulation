import pygame, sys
from boid import Boid
from flock import Flock
from config import HAUTEUR, LARGEUR, FPS

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Simulation de nuée d'oiseau")
flock = Flock()
pygame.display.flip()
clock = pygame.time.Clock()

    
for _ in range(0, 50):
    boid = Boid()
    flock.ajouter_boids(boid)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    flock.updates_boids()
    
    for boid in flock.boids:
        boid.bordure()

    fenetre.fill((0, 0, 0))
    flock.draw(fenetre)
    pygame.display.flip()
    clock.tick(FPS)
    

