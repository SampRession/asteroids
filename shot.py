import pygame as pg

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pg.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt