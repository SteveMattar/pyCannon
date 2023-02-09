from Vector import Vector2
import pygame as pg
from Config import *


class Player(object):
    def __init__(self):
        self.velocity = Vector2(0, 0)
        self.accuracy = Vector2(0, 0)
        self.size = PLAYER_BALL_RADIUS
        self.position = Vector2(10, WINDOW_HEIGHT - self.size - 10)
        self.mass = MASS
        self.cannon_firepower = CANNON_FIREPOWER
        self.rect = pg.Rect(self.position.x, self.position.y, self.size, self.size)
        self.image = pg.Surface([self.size, self.size], pg.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image, PLAYER_BALL_COLOR, [self.size / 2, self.size / 2], self.size / 2)
        self.dead = False
        self.visible = True

        self.score = 0

    def launch(self, f):
        self.apply_force(f)
        self.visible = True

    def apply_force(self, f):

        # make a copy to preserve the original vector values
        fcopy = f.get_copy()
        fcopy.div(self.mass)
        self.accuracy.add(fcopy)

    def update(self, core):
        if core.click:
            self.fire(core)
        self.velocity.add(self.accuracy)
        self.position.add(self.velocity)
        self.accuracy.mult(0)
        self.constrain()
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def constrain(self):
        if self.position.y > WINDOW_HEIGHT - self.size:
            self.position.y = WINDOW_HEIGHT - self.size
            self.velocity.mult(0)

    def out_of_play(self):
        # return (0 <= self.rect.y <= WINDOW_HEIGHT) and (0 <= self.rect.x <= WINDOW_WIDTH)
        return self.position.x < 0 or self.position.x > WINDOW_WIDTH or self.position.y >= WINDOW_HEIGHT - self.size

    def is_dead(self):
        return self.out_of_play() or self.dead

    def fire(self, core):
        if not self.is_dead():
            force = Vector2(core.mouse[0], core.mouse[1])
            force.sub(self.position)
            force.normalise()
            force.mult(self.cannon_firepower)
            self.launch(force)
            core.get_sound().play('fireball', 0, 0.5)
        else:
            core.get_sound().play('brick_break', 0, 0.5)

    def reset(self, reset_all):
        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.accuracy = Vector2(0, 0)

        if reset_all:
            self.score = 0
            self.dead = False
            self.visible = True

    def reset_move(self):
        self.velocity = Vector2(0, 0)

    def add_score(self, count):
        self.score += count

    def render(self, core):
        if self.visible:
            core.screen.blit(self.image, self.rect)
