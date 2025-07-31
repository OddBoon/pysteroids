import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_COLOR, ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self, shot):
        rand_rotate = random.uniform(20, 50)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        if(split_radius != 0):
            brother = Asteroid(self.position.x, self.position.y, split_radius)
            sister = Asteroid(self.position.x, self.position.y, split_radius)
            #TODO: Make CircleShape have a mass to generate ricochet calc
            # instead of using a uniform proxy via radius
            ricochet = shot.velocity * shot.radius/(self.radius*2)
            brother.velocity = 1.2*self.velocity.rotate(rand_rotate)+ricochet
            sister.velocity = 1.2*self.velocity.rotate(-rand_rotate)+ricochet
        self.kill()
    
    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt