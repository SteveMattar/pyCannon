from config.Config import *
from entities.Text import Text


class GameUI(object):
    def render(self, core):
        time_text = Text('TIME', 20, (WINDOW_WIDTH - 60, 10))
        score_text = Text('SCORE', 20, (WINDOW_WIDTH - 260, 10))
        level_text = Text('LEVEL', 16, (80, 10))
        time_value_text = Text(str(core.get_game().time), 20, (WINDOW_WIDTH - 60, 35))
        score_value_text = Text(str(core.get_game().get_player().score), 20, (WINDOW_WIDTH - 260, 35))
        level_value_text = Text(str(core.get_game().get_level()).split('.')[1], 16, (80, 35))
        time_text.render(core)
        score_text.render(core)
        level_text.render(core)
        time_value_text.render(core)
        score_value_text.render(core)
        level_value_text.render(core)

