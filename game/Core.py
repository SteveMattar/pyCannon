from os import environ

import pygame as pg
from pygame.locals import *

from config.Config import *
from game.Game import Game
from screens.MenuManager import MenuManager
from entities.Sound import Sound


class Core(object):
    """
    Main class.
    """
    def __init__(self):
        environ['SDL_VIDEO_CENTERED'] = '1'
        pg.mixer.pre_init(44100, -16, 2, 1024)
        pg.init()
        pg.display.set_caption('Cannon Game')
        # pg.mouse.set_visible(False)

        self.screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pg.time.Clock()

        self.game = Game()
        self.sound = Sound()
        self.menu_manager = MenuManager(self)

        self.run = True
        self.click = False
        self.mouse = pg.mouse.get_pos()

    def main_loop(self):
        while self.run:
            self.input()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def input(self):
        if self.get_menu_manager().currentGameState == 'Game':
            self.input_player()
        elif self.get_menu_manager().currentGameState == 'MainMenu':
            self.input_main_menu()
        elif self.get_menu_manager().currentGameState == 'LevelMenu':
            self.input_level_menu()

    def input_player(self):
        self.mouse = pg.mouse.get_pos()

        for e in pg.event.get():

            if e.type == pg.QUIT:
                self.run = False

            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.menu_manager.show_main_menu()

            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:  # left click
                    self.click = True

            if e.type == MOUSEBUTTONUP:
                if e.button == 1:  # left click
                    self.click = False

    def input_main_menu(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RETURN:
                    self.menu_manager.select_level()
                elif e.key == K_ESCAPE:
                    self.run = False

    def input_level_menu(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RETURN:
                    self.game.set_level(self.menu_manager.level_menu.selection)
                    self.menu_manager.start_loading()
                elif e.key == K_UP:
                    self.menu_manager.level_menu.up()
                elif e.key == K_DOWN:
                    self.menu_manager.level_menu.down()
                elif e.key == K_ESCAPE:
                    self.menu_manager.show_main_menu()

    def update(self):
        self.get_menu_manager().update(self)

    def render(self):
        self.get_menu_manager().render(self)

    def get_game(self):
        return self.game

    def get_menu_manager(self):
        return self.menu_manager

    def get_sound(self):
        return self.sound
