import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shots import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, asteroids, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    dt = 0
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')
        
        for object in drawable:
            object.draw(screen)
            
        for object in updatable:
            object.update(dt)
        
        for object in asteroids:
            if player.is_colliding(object):
                print('Game over!')
                sys.exit()
            for shot in shots:
                if object.is_colliding(shot):
                    object.split()
                    shot.kill()
        pygame.display.flip()
        

        
        dt = clock.tick(60) / 1000
    


if __name__ == '__main__':
    main()