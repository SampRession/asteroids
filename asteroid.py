import random

import pygame as pg

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_pos_vector = self.velocity.rotate(random_angle)
        new_neg_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        splitted_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        splitted_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)

        splitted_ast_1.velocity = new_pos_vector * 1.2
        splitted_ast_2.velocity = new_neg_vector * 1.2
