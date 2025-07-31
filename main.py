import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)

    start_x = SCREEN_WIDTH / 2
    start_y = SCREEN_HEIGHT / 2 
    player = Player(start_x, start_y)

    field = AsteroidField()
    dt = 0

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        updatables.update(dt)
        for asteroid in asteroids:
            if(asteroid.is_colliding(player)):
                print("Game Over!")
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            for shot in shots:
                if(asteroid.is_colliding(shot)):
                    shot.kill()
                    asteroid.split(shot)

        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()
    sys.exit()
    pass



if __name__ == "__main__":
    main()