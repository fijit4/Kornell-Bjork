import pygame as pg
import sys

class Consent:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Consent")
        self.title = pg.image.load("Consentscreen.PNG")
        self.screen = pg.display.set_mode((self.title.get_width(), self.title.get_height()))
        self.image=self.title
    def Start(self):
        start_screen_up = True

        while start_screen_up:
            self.title = pg.image.load("Consentscreen.PNG")
            self.image=self.title
            self.screen.blit(self.image, [0, 0])
            pg.display.update()

            pg.display.set_caption("Consent")
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    response = str(pg.key.name(event.key))
                    if response=="return":
                        start_screen_up=False
                    else:
                        sys.exit()