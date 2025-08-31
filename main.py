# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
from asteroid import Asteroid
from asteroidfield import *
import pygame
from constants import *
from player import *
from shot import Shot

def main():
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable,drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable)

	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	asteroid = AsteroidField()
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill("black")
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game over!")
				sys.exit()
			for shot in shots:
				if asteroid.collision(shot):
					shot.kill()
					asteroid.split()
		for draw in drawable:
			draw.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
