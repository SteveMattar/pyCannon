import pygame as pg

from screens.LoadingMenu import LoadingMenu
from screens.LevelMenu import LevelMenu
from screens.MainMenu import MainMenu


class MenuManager(object):
    """
    That class allows to easily handle game states. Depending on the situation,
    it updates and renders different things.
    """
    def __init__(self, core):

        self.currentGameState = 'MainMenu'

        self.main_menu = MainMenu()
        self.level_menu = LevelMenu()
        self.loading_menu = LoadingMenu(core)

    def update(self, core):
        if self.currentGameState == 'MainMenu':
            self.main_menu.update(core)

        elif self.currentGameState == 'LevelMenu':
            self.level_menu.update(core)

        elif self.currentGameState == 'Loading':
            self.loading_menu.update(core)

        elif self.currentGameState == 'Game':
            core.get_game().update(core)

    def render(self, core):
        if self.currentGameState == 'MainMenu':
            core.get_game().render_sky(core)
            self.main_menu.render(core)

        elif self.currentGameState == 'LevelMenu':
            core.get_game().render_sky(core)
            self.level_menu.render(core)

        elif self.currentGameState == 'Loading':
            self.loading_menu.render(core)

        elif self.currentGameState == 'Game':
            core.get_game().render(core)
            core.get_game().get_ui().render(core)

        pg.display.update()

    def show_main_menu(self):
        self.currentGameState = 'MainMenu'

    def select_level(self):
        # select the difficulty level
        self.currentGameState = 'LevelMenu'

    def start_loading(self):
        # Start to load the level
        self.currentGameState = 'Loading'
        self.loading_menu.update_time()
