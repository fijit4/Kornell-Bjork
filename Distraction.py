import pygame as pg
import sys
import random

class Distraction:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Distraction")
        self.title = pg.image.load("distractor.png")
        self.screen = pg.display.set_mode((self.title.get_width(), self.title.get_height()))
        self.image = self.title

    def Start(self):
        start_screen_up = True

        self.title = pg.image.load("distractor.png")
        self.image = self.title
        self.screen.blit(self.image, [0, 0])
        pg.display.update()
        pg.time.wait(15000)
