from config.Config import *
from entities.Text import Text


class MainMenu(object):
    def __init__(self):
        self.title = Text('Cannon', 32, (WINDOW_WIDTH - WINDOW_WIDTH * 0.5, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.7), Colors.YELLOW)
        self.to_start_text = Text('Press ENTER to start', 16, (WINDOW_WIDTH - WINDOW_WIDTH * 0.5, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.3))
        self.creator = Text('By Steve Mattar', 10, (WINDOW_WIDTH - WINDOW_WIDTH * 0.1, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.05))

    def render(self, core):
        self.title.render(core)
        self.to_start_text.render(core)
        self.creator.render(core)

    def update(self, core):
        core.get_game().reset(True)
        core.get_sound().stop('overworld')
        core.get_sound().stop('overworld_fast')
