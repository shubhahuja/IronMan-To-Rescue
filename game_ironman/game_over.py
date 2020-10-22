import random
import sys
import pygame
from pygame.locals import *
import sqlite3
import math


connection = sqlite3.connect('mydatabase.db')
c=connection.cursor()
def sql_table():
    c.execute('CREATE TABLE IF NOT EXISTS score(points REAL,name TEXT)')
def table_add(points,name):
    connection = sqlite3.connect('mydatabase.db')
    c=connection.cursor()
    sqlite_insert_with_param = """INSERT INTO score
                          (points, name) 
                          VALUES (?, ?);"""

    data_tuple = (points, name)
    c.execute(sqlite_insert_with_param, data_tuple)
    connection.commit()
    c.close()
    connection.close()
def print_top_5():
    connection = sqlite3.connect('mydatabase.db')
    c=connection.cursor()
    cursor = c.execute("SELECT * FROM score ORDER BY points DESC")
    a=0
    l=[]
    for i in c.fetchall():
        l=l+[i]
        a=a+1
        if a==5:
            break
    connection.commit()
    c.close()
    connection.close()
    return l


sql_table()





pygame.init() #initializing pygame
pygame.display.set_caption("GAME OVER")
#Global Variables

width = 1000
height = 750

MARGIN = 0
surface = pygame.display.set_mode((1000, 700))
score =0
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (139,0,0)
RED_BRIGHT=(255,7,58)




iron_menu_img = pygame.image.load(r'ironmanflysmall.png')
iron_menu_rect=iron_menu_img.get_rect()
iron_menu_rect.center=0,50

thor_menu_img = pygame.image.load(r'thor1.png')
thor_menu_rect=thor_menu_img.get_rect()
thor_menu_rect.center=0,500

falcon_menu_img = pygame.image.load(r'falcon2.png')
falcon_menu_rect=falcon_menu_img.get_rect()
falcon_menu_rect.center=0,130

vision_menu_img = pygame.image.load(r'vision_fly_small.png')
vision_menu_rect=vision_menu_img.get_rect()
vision_menu_rect.center=0,600

war_machine_menu_img=pygame.image.load(r'war_machine2.png')
war_machine_menu_rect=war_machine_menu_img.get_rect()
war_machine_menu_rect.center=40,340
class button_start():
    def __init__(self):
        self.rect=pygame.Rect(700,150,200,100)


class button_quit():
    def __init__(self):
        self.rect=pygame.Rect(100,150,200,100)


quit=button_quit()

start=button_start()







def over(surface,text,name,points):
   
    table_add(points,name)
    top_scores=print_top_5()
    a=""
    color =RED
    color2=RED
    while True:
        
            
            for event in pygame.event.get():

                
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()   
                

                elif pygame.mouse.get_pos()[0]>=quit.rect.x and pygame.mouse.get_pos()[0]<=quit.rect.x+200 \
                    and pygame.mouse.get_pos()[1]>=quit.rect.y and pygame.mouse.get_pos()[1]<=quit.rect.y+100:
                    
                    color=(64,224,208)
                    if pygame.mouse.get_pressed()[0]==1:
                        pygame.quit()
                        sys.exit() 
                
                elif pygame.mouse.get_pos()[0]>=start.rect.x and pygame.mouse.get_pos()[0]<=start.rect.x+200 \
                    and pygame.mouse.get_pos()[1]>=start.rect.y and pygame.mouse.get_pos()[1]<=start.rect.y+100:
                    color2=RED_BRIGHT
                    if pygame.mouse.get_pressed()[0]==1:
                        pygame.quit()
                        sys.exit() 
                else:
                    color=RED
                    color2=RED
                
            thor_menu_rect.x+=18
            iron_menu_rect.x+=20
            vision_menu_rect.x+=14
            war_machine_menu_rect.x+=16
            falcon_menu_rect.x+=12

            if thor_menu_rect.x>=990:
                thor_menu_rect.x=0
            if vision_menu_rect.x>=990:
                vision_menu_rect.x=0
            if falcon_menu_rect.x>=990:
                falcon_menu_rect.x=0
            if war_machine_menu_rect.x>=990:
                war_machine_menu_rect.x=0
            if iron_menu_rect.x>=990:
                iron_menu_rect.x=0

            surface.fill((0,0,0))

            

            surface.blit(iron_menu_img, iron_menu_rect)
            surface.blit(war_machine_menu_img, war_machine_menu_rect)
            surface.blit(vision_menu_img, vision_menu_rect)
            surface.blit(thor_menu_img, thor_menu_rect)
            surface.blit(falcon_menu_img, falcon_menu_rect)
            pygame.draw.rect(surface,color2,start.rect)      

            pygame.draw.rect(surface,color,quit.rect)

            pygame.font.init() 
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            myfontover = pygame.font.SysFont('inkfree', 61)
            start_text = myfont.render('START ', False,  (0,35,102))
            quit_text = myfont.render('QUIT ', False,  (0,35,102))
            surface.blit(start_text,(start.rect.x+50,start.rect.y+30))
            surface.blit(quit_text,(quit.rect.x+50,quit.rect.y+30))

            game_over_text = myfontover.render(text, False,  (204,229,255))
        
            
            name_text=myfont.render('Name = '  +name, False,  (64,224,208))
            score_text=myfont.render('Score = '  +str(points), False,  (64,224,208)) 

            surface.blit(game_over_text,(310,30))
            
            surface.blit(name_text,(100,80))
            surface.blit(score_text,(700,80))
            top=myfont.render("Name",False,  (255,255,0))
            surface.blit(top,(350,300))
            top1=myfont.render("Score",False,  (255,255,0))
            surface.blit(top1,(450,300))
            x=350
            y=350
            for i in top_scores:
                topname=myfont.render(i[1],False,  (255,255,0))
                topscore=myfont.render(str(i[0]),False,  (255,255,0))
                surface.blit(topname,(x,y))
                surface.blit(topscore,(x+100,y))
                y+=50




            pygame.display.update()
            clock=pygame.time.Clock()
            clock.tick(30)

over(surface,"GAME OVER","ab",100)