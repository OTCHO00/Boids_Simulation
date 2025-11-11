import pygame, sys
from boid import Boid
from flock import Flock
from config import HAUTEUR, LARGEUR, FPS

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Simulation de nuée d'oiseau")
flock = Flock()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            mx, my = pygame.mouse.get_pos()
            boid = Boid(pygame.Vector2(mx, my))
            flock.ajouter_boids(boid)

    for boid in flock.boids:

        boid.wraparound()
        boid.calculer_separation(flock.boids)
        boid.calculer_alignement(flock.boids)
        boid.calculer_cohesion(flock.boids)

    flock.updates_boids()

    fenetre.fill((0, 0, 0))
    flock.draw(fenetre)
    pygame.display.flip()
    clock.tick(FPS)
    

