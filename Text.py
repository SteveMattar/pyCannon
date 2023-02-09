import pygame as pg


class Text(object):
    def __init__(self, text, fontsize, rectcenter, textcolor=(255, 255, 255)):
        self.font = pg.font.Font('fonts/emulogic.ttf', fontsize)
        self.text = self.font.render(text, False, textcolor)
        self.rect = self.text.get_rect(center=rectcenter)
        self.y_offset = 0

    def update(self, core):
        self.rect.y -= 1
        self.y_offset -= 1

        if self.y_offset == -100:
            core.get_game().remove_text(self)

    def render(self, core):
        core.screen.blit(self.text, self.rect)
