from os import environ

import pygame as pg
from pygame.locals import *

from Config import *
from Game import Game
from MenuManager import MenuManager
from Sound import Sound


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
        self.keySpace = False
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
        else:
            self.input_menu()

    def input_player(self):
        self.mouse = pg.mouse.get_pos()

        for e in pg.event.get():

            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.run = False
                elif e.key == K_SPACE:
                    self.keySpace = True

            elif e.type == KEYUP:
                if e.key == K_SPACE:
                    self.keySpace = False

            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:  # left click
                    self.click = True

            if e.type == MOUSEBUTTONUP:
                if e.button == 1:  # left click
                    self.click = False

    def input_menu(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RETURN:
                    self.get_menu_manager().start_loading()

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
