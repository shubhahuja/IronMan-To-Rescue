import random
import sys
import pygame
from pygame.locals import *

import math
from player_choose import *

pygame.init() #initializing pygame
pygame.display.set_caption("GAME MENU")
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

menu_bg=pygame.image.load(r'menu_bg.jpg')
menu_bg=pygame.transform.scale(menu_bg, (1000, 700))


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
        self.rect=pygame.Rect(400,300,200,100)
class button_():
    def __init__(self):
        self.rect=pygame.Rect(400,300,200,100)

start=button_start()



def menu(surface,text="LET THE GAMES BEGIN",points=0):
    print(text)
    print(points)
    a=""
    while True:
        
            
            for event in pygame.event.get():

                
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()   
                elif event.type == KEYDOWN:
                    if (chr(event.key)>="a" and chr(event.key)<="z") or (chr(event.key)>="0" and chr(event.key)<="9") :
                        a=a+(chr(event.key))
                    if event.key==K_BACKSPACE:
                        a=a[:len(a)-1]

                if pygame.mouse.get_pos()[0]>=start.rect.x and pygame.mouse.get_pos()[0]<=start.rect.x+200 \
                    and pygame.mouse.get_pos()[1]>=start.rect.y and pygame.mouse.get_pos()[1]<=start.rect.y+200:
                    color=RED_BRIGHT
                    if pygame.mouse.get_pressed()[0]==1:
                        player_choose(surface,a)
                else:
                    color=RED
                
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

            surface.blit(menu_bg,(0,0))

            surface.blit(iron_menu_img, iron_menu_rect)
            surface.blit(war_machine_menu_img, war_machine_menu_rect)
            surface.blit(vision_menu_img, vision_menu_rect)
            surface.blit(thor_menu_img, thor_menu_rect)
            surface.blit(falcon_menu_img, falcon_menu_rect)
            pygame.draw.rect(surface,color,start.rect)           

            pygame.font.init() 
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            start_text = myfont.render('START ', False,  (0,35,102))
            surface.blit(start_text,(start.rect.x+50,start.rect.y+30))

            game_over_text = myfont.render(text, False,  (0,35,102))
            
            
            name_text=myfont.render('Enter Name = '  +a, False,  (64,224,208))

            surface.blit(game_over_text,(360,70))
            
            surface.blit(name_text,(320,600))
            pygame.display.update()
            clock=pygame.time.Clock()
            clock.tick(30)

menu(surface)

