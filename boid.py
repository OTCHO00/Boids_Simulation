import random, pygame, math
from config import HAUTEUR, LARGEUR, VITESSE_INIT, VITESSE_MIN, FORCE_MAX, VITESSE_MAX, VERT, POINTE_BOIDS, BASE_1_BOIDS, BASE_2_BOIDS, RAYON_ALIGNEMENT, RAYON_COHESION, RAYON_SEPARATION, POIDS_ALIGNEMENT, POIDS_COHESION, POIDS_SEPARATION

class Boid:
    def __init__(self):
        self.position = pygame.math.Vector2(random.uniform(0, LARGEUR), random.uniform(0, HAUTEUR))
        self.angle = random.uniform(0, 2 * math.pi)
        self.vitesse = pygame.math.Vector2(math.cos(self.angle) * VITESSE_INIT, math.sin(self.angle) * VITESSE_INIT)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.max_vitesse = VITESSE_MAX 
        self.force = pygame.math.Vector2(0, 0)
        self.max_force = FORCE_MAX

    def calculer_separation(self, voisins):

        somme = pygame.Vector2(0, 0)
        nb_voisins = 0

        for voisin in voisins:
            distance = (self.position - voisin.position).length()
            if 0 < distance <= RAYON_SEPARATION:
                direction_opposee = (self.position - voisin.position) / distance

                somme += direction_opposee
                nb_voisins += 1

        if nb_voisins > 0:
            moyenne = somme / nb_voisins
            force = moyenne.normalize() * self.max_force * POIDS_SEPARATION
            
            self.acceleration += force

    def calculer_alignement(self, voisins):

        somme = pygame.Vector2(0, 0)
        nb_voisin = 0

        for voisin in voisins:
            distance = (self.position - voisin.position).length()
            if 0 < distance <= RAYON_ALIGNEMENT:
                somme += voisin.vitesse
                nb_voisin += 1
            
        if nb_voisin > 0:
            vitesse_moyenne = somme / nb_voisin
            force_alignement = vitesse_moyenne - self.vitesse
        
            if force_alignement.length() > 0:

                force_alignement = force_alignement.normalize() * self.max_force * POIDS_ALIGNEMENT
                self.acceleration += force_alignement

    def calculer_cohesion(self, voisins):
        
        somme = pygame.Vector2(0, 0)
        nb_voisin = 0

        for voisin in voisins:
            distance = (self.position - voisin.position).length()
            if 0 < distance <= RAYON_COHESION:
                somme += voisin.position
                nb_voisin += 1

        if nb_voisin > 0:
            position_moyenne = somme / nb_voisin
            force_cohesion = position_moyenne - self.position
            
            if force_cohesion.length() > 0:
                
                force_cohesion = force_cohesion.normalize() * self.max_force * POIDS_COHESION
                self.acceleration += force_cohesion

    def update_position(self):
        self.vitesse += self.acceleration

        if self.vitesse.length() > self.max_vitesse:
            self.vitesse = self.vitesse.normalize() * self.max_vitesse
        elif self.vitesse.length() < VITESSE_MIN and self.vitesse.length() > 0:
            self.vitesse = self.vitesse.normalize() * VITESSE_MIN

        self.position += self.vitesse
        self.acceleration = pygame.Vector2(0, 0)

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

    def wraparound(self):
        if self.position.x > LARGEUR:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = LARGEUR

        if self.position.y > HAUTEUR:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = HAUTEUR
