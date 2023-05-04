import pygame as pg

class Intro:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Intructions")
        self.title = pg.image.load("Introscreen.png")
        self.screen = pg.display.set_mode((self.title.get_width(), self.title.get_height()))
        self.image=self.title
    def Start(self):
        start_screen_up = True

        while start_screen_up:
            self.title = pg.image.load("Introscreen.png")
            self.image=self.title
            self.screen.blit(self.image, [0, 0])
            pg.display.update()

            pg.display.set_caption("Instructions")
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    start_screen_up=False