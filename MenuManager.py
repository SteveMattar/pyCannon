import pygame as pg

from LoadingMenu import LoadingMenu
from MainMenu import MainMenu


class MenuManager(object):
    """
    That class allows to easily handle game states. Depending on the situation,
    it updates and renders different things.
    """
    def __init__(self, core):

        self.currentGameState = 'MainMenu'

        self.main_menu = MainMenu()
        self.loading_menu = LoadingMenu(core)

    def update(self, core):
        if self.currentGameState == 'MainMenu':
            pass

        elif self.currentGameState == 'Loading':
            self.loading_menu.update(core)

        elif self.currentGameState == 'Game':
            core.get_game().update(core)

    def render(self, core):
        if self.currentGameState == 'MainMenu':
            core.get_game().render_sky(core)
            self.main_menu.render(core)

        elif self.currentGameState == 'Loading':
            self.loading_menu.render(core)

        elif self.currentGameState == 'Game':
            core.get_game().render(core)
            core.get_game().get_ui().render(core)

        pg.display.update()

    def start_loading(self):
        # Start to load the level
        self.currentGameState = 'Loading'
        self.loading_menu.update_time()
