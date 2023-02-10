import pygame as pg
import random
from Config import *
from Vector import Vector2


class Targets:
    def __init__(self):
        self.size = TARGET_BALL_RADIUS
        self.position = Vector2(WINDOW_WIDTH, random.randrange(WINDOW_HEIGHT - WINDOW_HEIGHT * 0.9,
                                                               WINDOW_HEIGHT - WINDOW_HEIGHT * 0.1, self.size + 5))
        self.velocity = Vector2((random.uniform(MIN_MOVE_SPEED, MAX_MOVE_SPEED)), random.uniform(MIN_FALL_SPEED, MAX_FALL_SPEED))
        self.image = pg.Surface([self.size, self.size], pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image, TARGET_BALL_COLOR, [self.size / 2, self.size / 2], self.size / 2)

        self.state = 0
        self.crushed = False
        self.out = False
        self.collision = True

    def die(self, core, instantly, crushed):
        if not instantly:
            core.get_game().get_player().add_score(core.get_game().score_for_killing_targets)
            core.get_game().spawn_score_text(self.rect.x + 16, self.rect.y)

            if crushed:
                self.crushed = True
                self.state = -1
                core.get_sound().play('kill_mob', 0, 0.5)
                self.collision = False
            else:
                self.velocity.y = -4
                core.get_sound().play('shot', 0, 0.5)
                self.state = -1
                self.collision = False

        else:
            core.get_game().get_targets().remove(self)

    def check_collision_with_player(self, core):
        if self.collision:
            if self.rect.colliderect(core.get_game().get_player().rect):
                if self.state != -1:
                    if core.get_game().get_player().velocity.y > 0:
                        self.die(core, instantly=False, crushed=True)

    def update(self, core):
        self.out = self.out_of_play()

        # in play
        if self.state == 0:
            if not self.out:
                self.velocity.y += GRAVITY
            else:
                self.die(core, instantly=True, crushed=False)

            self.position.add(self.velocity)
            self.rect.x = self.position.x
            self.rect.y = self.position.y


        # dying
        elif self.state == -1:
            if self.crushed:
                core.get_game().get_targets().remove(self)
            else:
                self.velocity.y += GRAVITY
                self.rect.y += self.position.y
                if self.out:
                    self.die(core, instantly=True, crushed=False)

    def render(self, core):
        core.screen.blit(self.image, self.rect)

    def out_of_play(self):
        return self.position.x < 0 or self.position.x > WINDOW_WIDTH or self.position.y >= WINDOW_HEIGHT - self.size or self.position.y < 0
