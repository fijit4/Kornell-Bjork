import pygame as pg
import random
from Intro import Intro
from Massed import Massed
from Spaced import Spaced
from Test import Test
from Distraction import Distraction
from Consent import Consent

anames = ["Seurat", "Schlorff", "Hawkins", "Cross", "Mylrea", "Juras"]
global index

cross1=pg.image.load("cross 1.png")
w = int(cross1.get_height() / 2)
h = int(cross1.get_width() / 4)

cross=[pg.transform.scale(pg.image.load("cross 1.png"),(w,h)),pg.transform.scale(pg.image.load("cross 2.png"),(w,h)),pg.transform.scale(pg.image.load("cross 3.png"),(w,h)),pg.transform.scale(pg.image.load("cross 4.png"),(w,h)),pg.transform.scale(pg.image.load("cross 5.png"),(w,h)),pg.transform.scale(pg.image.load("cross 6.png"),(w,h))]
hawkins=[pg.transform.scale(pg.image.load("hawkins 1.png"),(w,h)),pg.transform.scale(pg.image.load("hawkins 2.png"),(w,h)),pg.transform.scale(pg.image.load("hawkins 3.png"),(w,h)),pg.transform.scale(pg.image.load("hawkins 4.png"),(w,h)),pg.transform.scale(pg.image.load("hawkins 5.png"),(w,h)),pg.transform.scale(pg.image.load("hawkins 6.png"),(w,h))]
juras=[pg.transform.scale(pg.image.load("juras 1.png"),(w,h)),pg.transform.scale(pg.image.load("juras 2.png"),(w,h)),pg.transform.scale(pg.image.load("juras 3.png"),(w,h)),pg.transform.scale(pg.image.load("juras 4.png"),(w,h)),pg.transform.scale(pg.image.load("juras 5.png"),(w,h)),pg.transform.scale(pg.image.load("juras 6.png"),(w,h))]
schlorff=[pg.transform.scale(pg.image.load("schlorff 1.png"),(w,h)),pg.transform.scale(pg.image.load("schlorff 2.png"),(w,h)),pg.transform.scale(pg.image.load("schlorff 3.png"),(w,h)),pg.transform.scale(pg.image.load("schlorff 4.png"),(w,h)),pg.transform.scale(pg.image.load("schlorff 5.png"),(w,h)),pg.transform.scale(pg.image.load("schlorff 6.png"),(w,h))]
mylrea=[pg.transform.scale(pg.image.load("mylrea 1.png"),(w,h)),pg.transform.scale(pg.image.load("mylrea 2.png"),(w,h)),pg.transform.scale(pg.image.load("mylrea 3.png"),(w,h)),pg.transform.scale(pg.image.load("mylrea 4.png"),(w,h)),pg.transform.scale(pg.image.load("mylrea 5.png"),(w,h)),pg.transform.scale(pg.image.load("mylrea 6.png"),(w,h))]
seurat=[pg.transform.scale(pg.image.load("seurat 1.png"),(w,h)),pg.transform.scale(pg.image.load("seurat 2.png"),(w,h)),pg.transform.scale(pg.image.load("seurat 3.png"),(w,h)),pg.transform.scale(pg.image.load("seurat 4.png"),(w,h)),pg.transform.scale(pg.image.load("seurat 5.png"),(w,h)),pg.transform.scale(pg.image.load("seurat 6.png"),(w,h))]
mass=[]
spac=[]

def choose_array(index):
    if anames[index]=="Cross":
        return cross
    elif anames[index]=="Hawkins":
        return hawkins
    elif anames[index] == "Juras":
        return juras
    elif anames[index] == "Seurat":
        return seurat
    elif anames[index] == "Schlorff":
        return schlorff
    elif anames[index] == "Mylrea":
        return mylrea

def spaced(index):
    testing=False
    anar=[]
    for i in range(3):
        spac.insert(i,anames[index])
        anar.insert(i,choose_array(index))
        index = index +1
    return anar,index
def test(index):
    testing=True
    anar = []
    for i in range(6):
        anar.insert(i,choose_array(index))
    return anar


class Main:
    pg.init()
    index=0
    random.shuffle(anames)
    consent=Consent()
    consent.Start()
    intro=Intro()
    intro.Start()
    screen = pg.display.set_mode((cross[0].get_width() + 100, cross[0].get_height() + 100))

    massed=Massed()
    mass.insert(index,anames[index])
    name=choose_array(index)

    index=massed.display(screen,anames[index],index,name)

    snames,index=spaced(index)
    space=Spaced()
    space.display(screen,anames, snames)
    space.display(screen, anames, snames)

    name=choose_array(index)
    mass.insert(index, anames[index])
    index = massed.display(screen, anames[index], index, name)
    name=choose_array(index)
    mass.insert(index, anames[index])
    index = massed.display(screen, anames[index], index, name)

    space.display(screen, anames, snames)

    distract=Distraction()
    distract.Start()

    allnames=test(0)
    tested=Test()
    tested.display(screen, anames, cross, hawkins, juras, mylrea, schlorff,seurat,spac,mass)











# See PyCharm help at https://www.jetbrains.com/help/pycharm/
