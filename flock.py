class Flock():

    def __init__(self):
        self.boids = []
    
    def ajouter_boids(self, boid):
        self.boids.append(boid)

    def retier_boids(self):
        self.boids.pop()

    def updates_boids(self):
        for boid in self.boids:
            boid.update_position()

    def draw(self, fenetre):
        for boid in self.boids:
            boid.draw(fenetre)