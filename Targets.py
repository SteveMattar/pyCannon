import pygame as pg
import random
from Config import *
from Vector import Vector2


class Targets:
    def __init__(self):
        self.size = TARGET_BALL_RADIUS
        self.position = Vector2(WINDOW_WIDTH - self.size / 2, random.randrange(WINDOW_HEIGHT - WINDOW_HEIGHT * 0.9, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.1))
        self.velocity = Vector2((random.randrange(1, MAX_MOVE_SPEED) * -1), 0)
        self.image = pg.Surface([self.size, self.size])
        self.rect = self.image.get_rect()
        self.image.fill(TARGET_BALL_COLOR)

        self.state = 0
        self.crushed = False
        self.on_ground = False
        self.collision = True

    def die(self, core, instantly, crushed):
        if not instantly:
            core.get_game().get_player().add_score(core.get_game().score_for_killing_mob)
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
        if self.state == 0:

            # if not self.on_ground:
            #     self.velocity.y += GRAVITY

            self.position.add(self.velocity)
            self.rect.x = self.position.x
            self.rect.y = self.position.y

            self.check_map_borders(core)

        elif self.state == -1:
            if self.crushed:
                core.get_game().get_targets().remove(self)
            else:
                # self.velocity.y += GRAVITY
                self.rect.y += self.position.y
                self.check_map_borders(core)

    def render(self, core):
        core.screen.blit(self.image, self.rect)

    def check_map_borders(self, core):
        if self.rect.y >= WINDOW_HEIGHT:
            self.die(core, True, False)
        if self.rect.x <= 1 and self.velocity.x < 0:
            self.velocity.x = - self.velocity.x
