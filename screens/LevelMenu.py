from config.Config import *
from entities.Text import Text


class LevelMenu(object):
    def __init__(self):
        self.selection = GameLevel.MEDIUM
        self.title = Text('Select Level', 18, (WINDOW_WIDTH - WINDOW_WIDTH * 0.5, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.8))
        self.easy_text = Text('Easy', 16, (WINDOW_WIDTH - WINDOW_WIDTH * 0.5, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.6))
        self.medium_text = Text('Medium', 16, (WINDOW_WIDTH - WINDOW_WIDTH * 0.5, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.5))
        self.hard_text = Text('Hard', 16, (WINDOW_WIDTH - WINDOW_WIDTH * 0.5, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.4))
        self.medium_text.change_color(Colors.YELLOW)


    def render(self, core):
        self.title.render(core)
        self.easy_text.render(core)
        self.medium_text.render(core)
        self.hard_text.render(core)

    def update(self, core):
        if self.selection == GameLevel.EASY:
            self.easy_text.change_color(Colors.YELLOW)
            self.medium_text.change_color(Colors.WHITE)
            self.hard_text.change_color(Colors.WHITE)
        elif self.selection == GameLevel.MEDIUM:
            self.easy_text.change_color(Colors.WHITE)
            self.medium_text.change_color(Colors.YELLOW)
            self.hard_text.change_color(Colors.WHITE)
        elif self.selection == GameLevel.HARD:
            self.easy_text.change_color(Colors.WHITE)
            self.medium_text.change_color(Colors.WHITE)
            self.hard_text.change_color(Colors.YELLOW)

    def up(self):
        if self.selection == GameLevel.EASY:
            pass
        elif self.selection == GameLevel.MEDIUM:
            self.selection = GameLevel.EASY
        elif self.selection == GameLevel.HARD:
            self.selection = GameLevel.MEDIUM

    def down(self):
        if self.selection == GameLevel.EASY:
            self.selection = GameLevel.MEDIUM
        elif self.selection == GameLevel.MEDIUM:
            self.selection = GameLevel.HARD
        elif self.selection == GameLevel.HARD:
            pass
