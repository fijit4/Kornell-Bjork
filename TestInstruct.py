import pygame as pg

class TestInstruct:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Intructions")
        self.title = pg.image.load("TestInstructions.PNG")
        self.screen = pg.display.set_mode((self.title.get_width(), self.title.get_height()))
        self.image=self.title
    def Start(self):
        start_screen_up = True

        while start_screen_up:
            self.title = pg.image.load("TestInstructions.PNG")
            self.image=self.title
            self.screen.blit(self.image, [0, 0])
            pg.display.update()

            pg.display.set_caption("Instructions")
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    start_screen_up=False