import random
import sys
import pygame
from pygame.locals import *
from game_over import *

pygame.init() #initializing pygame
pygame.display.set_caption("GAME")
#Global Variables

width = 1000
height = 750

MARGIN = 0
surface = pygame.display.set_mode((1000, 700))
score =0
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

game_status=True
player_img = "ironmanflysmall.png"
x=0
y=350
x1=950
y1=40
bgx1=0
bgx2=1000
randy=random.randint(100,400)

bg = pygame.image.load(r'rockbg.png')
bg = pygame.transform.scale(bg, (1000, 700))

try_img = pygame.image.load(r'fireball.png')
try_img=pygame.transform.scale(try_img,(70,70))
image_rect2=try_img.get_rect()
image_rect2.center=1000,randy


game_over_text_1=""


class button_start():
    def __init__(self):
        self.rect=pygame.Rect(250,300,300,200)

start=button_start()

class bar():
    def __init__(self,x):
        self.x=x
        self.y=random.randint(500,660)
        self.size=700-450
        self.rect=pygame.Rect(self.x,self.y,10,self.size)
    def update(self):
        self.x-=10
        if self.x<0:
            self.x=1000
            self.y=random.randint(450,650)
            self.size=700-self.y
        self.rect.x=self.x
        self.rect.y=self.y
    
count=0

bar1=bar(1000)       
points=0
class Bars():
    def __init__(self):
        self.bar_list=[]
        for i in range(0,1000,10):
            bar_i=bar(i)
            self.bar_list.append(bar_i)
    def updater(self):
        for i in self.bar_list:
            i.update()




bars=Bars()
text=""
up_stat=False

def game(image_rect,game_status,image_rect2,bgx1,bgx2,bars,image,try_img,BLACK,start,points,count,bg,text,x1,up_stat,name):
    life=5
    cooldown=0
    c=False
    safe=False
    while game_status:
        
            
            for event in pygame.event.get():
                
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()    
                elif event.type == KEYDOWN and event.key== K_UP:
                    
                    image_rect.y-=20
                    up_stat=True
                

                #elif event.type == KEYDOWN and event.key== K_RIGHT:
                    #bgx1-=20
                   # bgx2-=20
                  #  image_rect2.x=bgx2
               # elif event.type == KEYDOWN and event.key== K_LEFT:
                 #   x-=20 
                elif event.type==KEYUP and event.key== K_UP:
                    up_stat=False
            x1-=10
            bgx1-=10
            bgx2-=10
            if bgx2==0:
                bgx1=1000
            if bgx1==0:
                bgx2=1000
            if up_stat:
                image_rect.y-=30

            image_rect2.x-=20
            bar1.update()
            if image_rect2.x<=0:
                points+=10
                image_rect2.x=1000
                image_rect2.y=random.randint(100,400)
            image_rect.y+=10
            bars.updater()
            if image_rect.y>=630:
                image_rect.y=620
            if image_rect.y<=0:
                image_rect.y=50
            
            if image_rect.colliderect(image_rect2):
                if safe==False:
                    text="OUCH -4"
                    points-=2
                    life-=1
                    count=-10
                    image_rect.y=50
                    
                    cooldown=10
                else:
                    text="Safe for " +str(cooldown)
            for i in bars.bar_list:
                if image_rect.colliderect(i.rect):
                    if safe==False:
                        points-=1
                        life-=1
                        text="GOOO UPPP  -2"
                        count=-10
                        image_rect.y=50
                        
                        cooldown=10
                    else:
                        text="Safe for " +str(cooldown)
            
            count+=1
            if count>0:
                text=""
            if cooldown>0:
                safe=True
                cooldown-=1
            if cooldown<=0:
                safe=False

            if points<-100 or life<0:
                game_over_text_1="GAME OVER!"
                over(surface,"GAME OVER",name,points)
                game_status=False
                

    

            surface.fill((20,120,255))
            surface.blit(bg, (bgx1, 0))
            surface.blit(bg, (bgx2, 0))
            for i in bars.bar_list:
                pygame.draw.rect(surface,BLACK,i.rect)
            surface.blit(image, image_rect)
            surface.blit(try_img,image_rect2)
        
            pygame.font.init() 
            myfont = pygame.font.SysFont('Comic Sans MS', 20)
            textsurface = myfont.render('Score : '+ str(points) , False,  (0,35,102))
            lifesurface = myfont.render('life : '+ str(life) , False,  (0,35,102))
            text2=myfont.render(text , False,  (255,0,0))
            surface.blit(textsurface,(430,30))
            surface.blit(text2,(200,30))
            surface.blit(lifesurface,(430,60))
            pygame.display.update()
            clock=pygame.time.Clock()
            clock.tick(30)


