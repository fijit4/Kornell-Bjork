import pygame as pg

class Spaced:
    def __init__(self):
        self.k=0
        self.j=0
    def display(self, screen, aname, snames):
        w = int(snames[0][0].get_width() / 2)
        h = int(snames[0][0].get_height() + 50)

        screen = pg.display.set_mode((snames[0][0].get_width() + 100, snames[0][0].get_height() + 100))
        pg.display.set_caption("Spaced")
        screenup = True

        while screenup:

            for i in range(4):
                pg.draw.rect(screen, (0, 0, 0), pg.Rect(w - int(w / 2) - 20, w, h, h))
                screen.blit(snames[self.k][self.j], [50, 10])
                font = pg.font.Font(None, 50)
                image = font.render(aname[1+self.k], True, [0, 255, 255])
                screen.blit(image, (w, h))
                pg.display.update()
                pg.time.wait(3000)
                self.k=self.k+1
                if self.k==3:
                    self.k=0
                    self.j=self.j+1
            screenup = False