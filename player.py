import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_FRICTION_DELTA

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0
    
    def draw(self, screen):
        #JADE GREEN:HEX 00A86B
        pygame.draw.polygon(screen, (0, 168, 107), self.vec_ship(), 2)
    
    def slide(self, dt):
        self.velocity *= PLAYER_FRICTION_DELTA
        self.position += self.velocity

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        pass
    
    def accelerate(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        if(dt < 0):
            dt *= 0.5
        self.velocity = forward * PLAYER_SPEED * dt

    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.accelerate(dt)
        if keys[pygame.K_s]:
            self.accelerate(-dt)
        self.slide(dt)
        
    
    def vec_ship(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius / 2
        d = self.position - forward * self.radius + right
        return [a, b, c, d]