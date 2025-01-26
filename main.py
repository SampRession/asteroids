import sys

import pygame as pg

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pg.init()
    print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_obj = pg.time.Clock()
    dt = 0

    # pygame groups
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    shots = pg.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for ast in asteroids:
            if ast.collision_check(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if ast.collision_check(shot):
                    ast.split()
                    shot.kill()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pg.display.flip()

        # FPS limit to 60
        dt = time_obj.tick(60) / 1000


if __name__ == "__main__":
    main()
