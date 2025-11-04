import random, pygame, math
from config import HAUTEUR, LARGEUR, VITESSE_INIT, FORCE_MAX, VITESSE_MAX, VERT, POINTE_BOIDS, BASE_1_BOIDS, BASE_2_BOIDS

class Boid:
    def __init__(self):
        self.position = pygame.math.Vector2(random.uniform(0, LARGEUR), random.uniform(0, HAUTEUR))
        self.angle = random.uniform(0, 2 * math.pi)
        self.vitesse = pygame.math.Vector2(math.cos(self.angle) * VITESSE_INIT, math.sin(self.angle) * VITESSE_INIT)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.max_vitesse = VITESSE_MAX 
        self.max_force = FORCE_MAX

    def calculer_separation(self, voisin):
        pass

    def calculer_alignement(self):
        pass

    def calculer_cohesion(self):
        pass

    def appliquer_force(self):
        pass

    def update_position(self):
        self.position += self.vitesse

    def draw(self, fenetre):

        self.angle = math.atan2(self.vitesse.y, self.vitesse.x)

        #Pointe
        x = POINTE_BOIDS[0] * math.cos(self.angle) - POINTE_BOIDS[1] * math.sin(self.angle)
        y = POINTE_BOIDS[0] * math.sin(self.angle) + POINTE_BOIDS[1] * math.cos(self.angle)
        x_pointe = x + self.position.x
        y_pointe = y + self.position.y

        #Base1
        x = BASE_1_BOIDS[0] * math.cos(self.angle) - BASE_1_BOIDS[1] * math.sin(self.angle)
        y = BASE_1_BOIDS[0] * math.sin(self.angle) + BASE_1_BOIDS[1] * math.cos(self.angle)
        x_base_1 = x + self.position.x
        y_base_1 = y + self.position.y

        #Base2
        x = BASE_2_BOIDS[0] * math.cos(self.angle) - BASE_2_BOIDS[1] * math.sin(self.angle)
        y = BASE_2_BOIDS[0] * math.sin(self.angle) + BASE_2_BOIDS[1] * math.cos(self.angle)
        x_base_2 = x + self.position.x
        y_base_2 = y + self.position.y

        pygame.draw.polygon(fenetre, VERT, [(x_pointe, y_pointe), (x_base_1, y_base_1), (x_base_2, y_base_2)], width=2)

    def bordure(self):
        if self.position.y <= 0 or self.position.y >= HAUTEUR:
            self.vitesse.y = -self.vitesse.y
        if self.position.x <= 0 or self.position.x >= LARGEUR:
            self.vitesse.x = -self.vitesse.x
