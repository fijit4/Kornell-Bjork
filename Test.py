import pygame as pg
import sys
import random
import pandas as pd
import os
from massorspace import massorspace
from TestInstruct import TestInstruct

class Test:
    def __init__(self):
        l=0
        q=0
        self.posi=[]
        for i in range(6):
            if i == 3:
                q = 0
                l=1
            self.post = (90 + 350 * l, 350 + 20 * q)
            self.posi.append(self.post)
            q=q+1
        self.j=0
        self.p=4
        self.timer=0
        self.screenup=True
        self.names=[]
        self.wrongig=pg.image.load("Wrong.PNG")
        self.correctig=pg.image.load("CORRECT.PNG")
        self.mcorrect=0
        self.scorrect=0
        self.second=False
        self.mcorrect2 = 0
        self.scorrect2 = 0
    def write(self):
        mass=massorspace()
        answer=mass.Start()
        path="psychresults.xlsx"
        if os.path.exists(path)==False:
            df1 = pd.DataFrame([[self.mcorrect,self.scorrect,self.mcorrect2,self.scorrect2,answer]],index=["Participant"], columns=['Test 1 Massed','Test 1 Spaced', 'Test 2 Massed', 'Test 2 Spaced', "Massed or Spaced"])
            df1.to_excel(path,sheet_name="Results")
        else:
            df1=pd.read_excel(path)
            df2=pd.DataFrame([[self.mcorrect,self.scorrect,self.mcorrect2,self.scorrect2]],index=["Participant"],columns=['Test 1 Massed','Test 1 Spaced', 'Test 2 Massed', 'Test 2 Spaced',"Massed or Spaced"])
            df=pd.concat([df1,df2])
            df.to_excel("psychresults.xlsx",index=False)



    def display(self, screen, aname,cross, hawkins, juras, mylrea, schlorff,seurat,mass,space):
        w = int(cross[0].get_width() / 2)
        h = int(cross[0].get_height() + 50)
        if self.timer==0:
            Test = TestInstruct()
            Test.Start()
            for i in range(len(aname)):
                self.names.insert(i,aname[i])
        self.timer=self.timer+1
        k=cross[0].get_width()
        m = cross[0].get_height()
        screen = pg.display.set_mode((cross[0].get_width() + 109, cross[0].get_height() + 100))
        pg.display.set_caption("Test")
        letters=["1: ","2: ", "3: ", "4: ", "5: ", "6: "]
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(k,k, m, m))
        pg.display.update()
        for i in range(6):
            font = pg.font.Font(None, 20)
            image = font.render(letters[i]+self.names[i], True, [0, 255, 255])
            screen.blit(image,(self.posi[i][0],self.posi[i][1]))
            pg.display.update()
        if self.j==0:
            random.shuffle(aname)
        self.call_question(screen,aname,cross, hawkins, juras, mylrea, schlorff,seurat,mass,space)

    def call_question(self,screen,aname,cross, hawkins, juras, mylrea, schlorff,seurat,mass,space):
        self.choose_array(screen, aname, cross, hawkins, juras, mylrea, schlorff, seurat)
        pg.display.update()

        if (self.timer == 13):
            self.write()
            sys.exit()
        while self.screenup:
            for event in pg.event.get():
                if event.type==pg.KEYDOWN:
                    response=str(pg.key.name(event.key))
                    respons=self.select(response,self.names)
                    if respons==aname[self.j].lower():
                        self.correct(screen,aname,cross, hawkins, juras, mylrea, schlorff,seurat,mass,space)
                    else:
                        self.wrong(screen, aname,cross, hawkins, juras, mylrea, schlorff,seurat,mass,space)

    def select (self, anames,responce):
        if anames == "1":
            return responce[0].lower()
        elif anames== "2":
           return responce[1].lower()
        elif anames == "3":
            return responce[2].lower()
        elif anames == "4":
            return responce[3].lower()
        elif anames == "5":
            return responce[4].lower()
        elif anames == "6":
            return responce[5].lower()

    def correct(self,screen,aname,cross, hawkins, juras, mylrea, schlorff,seurat,mass,space):
        screen.blit(self.correctig,(40,50))
        pg.display.update()
        pg.time.wait(2000)
        for i in range(3):
            if aname[self.j]==mass[i]and self.second==False:
                self.mcorrect=self.mcorrect+1
                break
            elif aname[self.j]==mass[i]and self.second==True:
                self.mcorrect2 = self.mcorrect2 + 1
                break
            if aname[self.j]==space[i]and self.second==False:
                self.scorrect=self.scorrect+1
                break
            elif aname[self.j]==space[i]and self.second==True:
                self.scorrect2 = self.scorrect2 + 1
                break

        self.j=self.j+1
        self.display(screen,aname,cross, hawkins, juras, mylrea, schlorff,seurat,mass,space)

    def wrong(self, screen, aname, cross, hawkins, juras, mylrea, schlorff, seurat,mass,space):
        screen.blit(self.wrongig,(60,50))
        pg.display.update()
        pg.time.wait(2000)
        self.j = self.j + 1
        self.display(screen, aname, cross, hawkins, juras, mylrea, schlorff, seurat,mass,space)

    def choose_array(self, screen, anames, cross, hawkins, juras, mylrea, schlorff, seurat):
        if self.j == 6:
            self.j = 0
            self.p = 5
            self.second=True
        if anames[self.j] == "Cross":
            screen.blit(cross[self.p],[50,10])
        elif anames[self.j] == "Hawkins":
            screen.blit(hawkins[self.p],[50,10])
        elif anames[self.j] == "Juras":
            screen.blit(juras[self.p],[50,10])
        elif anames[self.j] == "Seurat":
            screen.blit(seurat[self.p],[50,10])
        elif anames[self.j] == "Schlorff":
            screen.blit(schlorff[self.p],[50,10])
        elif anames[self.j] == "Mylrea":
            screen.blit(mylrea[self.p],[50,10])