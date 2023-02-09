import pygame as pg
from Vector import Vector2
from Config import *


class Event(object):
    def __init__(self):
        # 0 = Kill/Game Over
        # 1 = Win (using flag)
        self.type = 0
        self.delay = 0
        self.time = 0
        self.velocity = Vector2(0, 0)
        self.game_over = False

        self.player_in_castle = False
        self.tick = 0
        self.score_tick = 0

    def reset(self):
        self.type = 0
        self.delay = 0
        self.time = 0
        self.velocity = Vector2(0, 0)
        self.game_over = False
        self.tick = 0
        self.score_tick = 0

    def start_kill(self, core, game_over):
        """
        Player gets killed.
        """
        self.type = 0
        self.delay = 4000
        self.velocity.y = -4
        self.time = pg.time.get_ticks()
        self.game_over = game_over

        core.get_sound().stop('overworld')
        core.get_sound().stop('overworld_fast')
        core.get_sound().play('death', 0, 0.5)

    def start_win(self, core):
        """
        player touches the flag.
        """
        self.type = 1
        self.delay = 2000
        self.time = 0

        core.get_sound().stop('overworld')
        core.get_sound().stop('overworld_fast')
        core.get_sound().play('level_end', 0, 0.5)

        core.get_game().get_player().velocity.x = 1
        core.get_game().get_player().rect.x += 10

        # Adding score depends on the map's time left.
        if core.get_game().time >= 300:
            core.get_game().get_player().add_score(5000)
            core.get_game().spawn_score_text(core.get_game().get_player().rect.x + 16, core.get_game().get_player().rect.y, score=5000)
        elif 200 <= core.get_game().time < 300:
            core.get_game().get_player().add_score(2000)
            core.get_game().spawn_score_text(core.get_game().get_player().rect.x + 16, core.get_game().get_player().rect.y, score=2000)
        else:
            core.get_game().get_player().add_score(1000)
            core.get_game().spawn_score_text(core.get_game().get_player().rect.x + 16, core.get_game().get_player().rect.y, score=1000)

    def update(self, core):

        # Death
        if self.type == 0:
            self.velocity.y += GRAVITY * FALL_MULTIPLIER if self.velocity.y < 6 else 0
            core.get_game().get_player().rect.y += self.velocity.y

            if pg.time.get_ticks() > self.time + self.delay:
                if not self.game_over:
                    core.get_game().reset(False)
                    core.get_sound().play('overworld', 9999999, 0.5)
                else:
                    core.get_menu_manager().currentGameState = 'Loading'
                    core.get_menu_manager().loading_menu.set_text_and_type('GAME OVER', False)
                    core.get_menu_manager().loading_menu.update_time()
                    core.get_sound().play('game_over', 0, 0.5)

        # Flag win
        elif self.type == 1:
            self.tick += 1
            if self.tick == 1:
                core.get_game().get_player().rect.x += 20
            if core.get_game().time > 0:
                self.score_tick += 1
                if self.score_tick % 10 == 0:
                    core.get_sound().play('scorering', 0, 0.5)

                core.get_game().time -= 1
                core.get_game().get_player().add_score(50)

            else:
                if self.time == 0:
                    self.time = pg.time.get_ticks()

                elif pg.time.get_ticks() >= self.time + self.delay:
                    core.get_menu_manager().currentGameState = 'Loading'
                    core.get_menu_manager().loading_menu.update_time()
                    core.get_sound().play('game_over', 0, 0.5)
