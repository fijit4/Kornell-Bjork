import pygame as pg

class Massed:
    def display(self,screen,aname,index,name):

        pg.display.set_caption("Massed")
        w=int(name[0].get_width()/2)
        h=int(name[0].get_height()+50)

        font = pg.font.Font(None, 50)
        image = font.render(aname, True, [0, 255, 255])

        pg.draw.rect(screen,(0,0,0), pg.Rect(w-int(w/2)-20,w,h,h))
        screen.blit(image, (w, h))

        for i in range(len(name)-2):
            screen.blit(name[i],[50,10])
            pg.display.update()
            pg.time.wait(3000)

        return index+1
