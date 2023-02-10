import pygame as pg
from Config import *
from GameUI import GameUI
from Player import Player
from Targets import Targets
from Text import Text


class Game(object):
    """
    This class contains every object: player, targets. Also,
    there are event and UI.
    """

    def __init__(self):
        self.targets = []
        self.text_objects = []
        self.level = LEVEL

        self.sky = 0
        self.load()
        self.score_for_killing_targets = 100
        self.score_time = 0

        self.tick = 0
        self.time = TIME(self.level)

        self.player = Player()
        self.gameUI = GameUI()

    def load(self):
        self.sky = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.sky.fill(Colors.SKY)

        # # Targets
        self.targets.append(Targets(self.level))

    def reset(self, reset_all):
        self.targets = []
        self.level = LEVEL

        self.sky = None

        self.tick = 0
        self.time = TIME(self.level)

        self.load()

        self.get_player().reset(reset_all)

    def get_level(self):
        return str(LEVEL)

    def get_player(self):
        return self.player

    def get_ui(self):
        return self.gameUI

    def get_targets(self):
        return self.targets

    def spawn_score_text(self, x, y, score=None):
        """
        This text appears when you, for example, kill a target. It shows how many points
        you got.
        """

        # Score is none only when you kill a target. If you got a killstreak,
        # amount of points for killing a target will increase: 100, 200, 400, 800...
        # So you don't know how many points you should add.
        if score is None:
            self.text_objects.append(Text(str(self.score_for_killing_targets), 16, (x, y)))

            # Next score will be bigger
            self.score_time = pg.time.get_ticks()
            if self.score_for_killing_targets < 1600:
                self.score_for_killing_targets *= 2

        # That case for all other situations.
        else:
            self.text_objects.append(Text(str(score), 16, (x, y)))

    def remove_text(self, text_object):
        self.text_objects.remove(text_object)

    def update_player(self, core):
        self.get_player().update(core)

    def update_targets(self, core):
        if len(self.targets) < MAX_TARGETS(self.level):
            self.targets.append(Targets(self.level))
        for target in self.targets:
            target.update(core)
            self.targets_collisions(core)

    def update_time(self, core):
        """
        Updating a map time.
        """

        # Time updates only if map not in event
        self.tick += 1
        if self.tick % 40 == 0 and self.time != 0:
            self.time -= 1
            self.tick = 0
        if self.time == 100 and self.tick == 1:
            core.get_sound().start_fast_music(core)
        elif self.time == 0:
            self.end_game(core)

    def update_score_time(self):
        """
        When player kill targets in a row, score for each target
        will increase. When player stops kill targets, points
        will reset to 100. This function updates these points.
        """
        if self.score_for_killing_targets != 100:

            # Delay is 750 ms
            if pg.time.get_ticks() > self.score_time + 750:
                self.score_for_killing_targets //= 2

    def targets_collisions(self, core):
        for target in self.targets:
            target.check_collision_with_player(core)

    def end_game(self, core):
        self.get_player().reset_move()
        for target in self.get_targets():
            target.reset_move()

    def update(self, core):

        # All targets
        self.update_targets(core)
        self.update_player(core)

        # Text which represent how mapy points player get
        for text_object in self.text_objects:
            text_object.update(core)

        self.update_time(core)
        self.update_score_time()

    def render_sky(self, core):
        """
        Rendering only sky. It's used in main menu.
        """
        core.screen.blit(self.sky, (0, 0))

    def render(self, core):
        """
        Renders every object.
        """
        core.screen.blit(self.sky, (0, 0))

        for target in self.targets:
            target.render(core)

        for text_object in self.text_objects:
            text_object.render(core)

        self.get_player().render(core)

        self.get_ui().render(core)
