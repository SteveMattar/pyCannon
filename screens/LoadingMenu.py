import pygame as pg

from config.Config import *
from entities.Text import Text


class LoadingMenu(object):
    def __init__(self, core):
        self.iTime = pg.time.get_ticks()
        self.loading_type = True
        self.bg = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        # self.text = Text('LEVEL ' + core.game.get_level(), 32, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.text = Text('Loading...', 32, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def update(self, core):
        if pg.time.get_ticks() >= self.iTime + (5250 if not self.loading_type else 2500):
            if self.loading_type:
                core.menu_manager.currentGameState = 'Game'
                core.get_sound().play('overworld', 999999, 0.5)
            else:
                core.menu_manager.currentGameState = 'MainMenu'
                self.set_text_and_type('LEVEL ' + str(core.game.get_level()), True)
                core.get_game().reset(True)

    def set_text_and_type(self, text, loading_type):
        self.text = Text(text, 32, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.loading_type = loading_type

    def render(self, core):
        core.screen.blit(self.bg, (0, 0))
        self.text.render(core)

    def update_time(self):
        self.iTime = pg.time.get_ticks()
