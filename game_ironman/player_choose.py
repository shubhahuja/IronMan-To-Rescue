import random
import sys
import pygame
from pygame.locals import *
from game import *
import math


pygame.init() #initializing pygame
pygame.display.set_caption("GAME PLAYER SELCECTION")
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


bg_player = pygame.image.load(r'bg_player.jpg')
bg_player = pygame.transform.scale(bg_player, (1000, 700))

ironman_dp = pygame.transform.scale(pygame.image.load(r'ironman_dp.png'), (180, 500))

ironman_dp_rect=ironman_dp.get_rect()
ironman_dp_rect.center=90+30,350

thor =pygame.transform.scale( pygame.image.load(r'thor_dp2.png'),(200,500))
thor_rect=thor.get_rect()
thor_rect.center=280+30,350

falcon =pygame.transform.scale( pygame.image.load(r'falcon_dp2.png'),(200,500))
falcon_rect=falcon.get_rect()
falcon_rect.center=470+30,350


war_machine=pygame.transform.scale(pygame.image.load(r'war_dp2.png'),(180,500))
war_machine_rect=war_machine.get_rect()
war_machine_rect.center=660+30,350

vision=pygame.transform.scale(pygame.image.load(r'vision_dp.png'),(200,500))
vision_rect=vision.get_rect()
vision_rect.center=850+30,350


#players

ironman_fly = pygame.image.load(r'ironmanflysmall.png')
ironman_fly_rect=ironman_fly.get_rect()
ironman_fly_rect.center=300,300

thor_fly = pygame.image.load(r'thor1.png')
thor_fly_rect=thor_fly.get_rect()
thor_fly_rect.center=300,300

falcon_fly = pygame.image.load(r'falcon2.png')
falcon_fly_rect=falcon_fly.get_rect()
falcon_fly_rect.center=300,300

vision_fly = pygame.image.load(r'vision_fly_small.png')
vision_fly_rect=vision_fly.get_rect()
vision_fly_rect.center=300,300

war_machine_fly=pygame.image.load(r'war_machine2.png')
war_machine_fly_rect=war_machine_fly.get_rect()
war_machine_fly_rect.center=300,300

iron_color=(100,0,0)
thor_color=(0,0,80)
war_color=(134,138,136)
falcon_color=(0,100,0)
vision_color=(255,173,1)

def player_choose(surface,name):
    iron_color=(100,0,0)
    thor_color=(0,0,80)
    war_color=(134,138,136)
    falcon_color=(0,100,0)
    vision_color=(255,173,1)
    while True:
        
            
            for event in pygame.event.get():

                
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()   
                
                if pygame.mouse.get_pos()[0]>=ironman_dp_rect.x and pygame.mouse.get_pos()[0]<=ironman_dp_rect.x+180 \
                    and pygame.mouse.get_pos()[1]>=ironman_dp_rect.y and pygame.mouse.get_pos()[1]<=ironman_dp_rect.y+500:
                    iron_color=(255,7,58)
                    if pygame.mouse.get_pressed()[0]==1:
                        image=ironman_fly
                        image_rect=ironman_fly_rect
                        a=game(image_rect,game_status,image_rect2,bgx1,bgx2,bars,image,try_img,BLACK,start,points,count,bg,text,x1,up_stat,name)
                else:
                    iron_color=(100,0,0)
                
                if pygame.mouse.get_pos()[0]>=thor_rect.x and pygame.mouse.get_pos()[0]<=thor_rect.x+200 \
                    and pygame.mouse.get_pos()[1]>=thor_rect.y and pygame.mouse.get_pos()[1]<=thor_rect.y+500:
                    thor_color=(70,102,225)

                    if pygame.mouse.get_pressed()[0]==1:
                        image=thor_fly
                        image_rect=thor_fly_rect
                        game(image_rect,game_status,image_rect2,bgx1,bgx2,bars,image,try_img,BLACK,start,points,count,bg,text,x1,up_stat,name)
                else:
                    thor_color=(0,0,80)

                if pygame.mouse.get_pos()[0]>=falcon_rect.x and pygame.mouse.get_pos()[0]<=falcon_rect.x+200 \
                    and pygame.mouse.get_pos()[1]>=falcon_rect.y and pygame.mouse.get_pos()[1]<=falcon_rect.y+500:
                    falcon_color=(39,255,13)

                    if pygame.mouse.get_pressed()[0]==1:
                        image=falcon_fly
                        image_rect=falcon_fly_rect
                        game(image_rect,game_status,image_rect2,bgx1,bgx2,bars,image,try_img,BLACK,start,points,count,bg,text,x1,up_stat,name)
                else:
                    falcon_color=(0,100,0)


                if pygame.mouse.get_pos()[0]>=war_machine_rect.x and pygame.mouse.get_pos()[0]<=war_machine_rect.x+200 \
                    and pygame.mouse.get_pos()[1]>=war_machine_rect.y and pygame.mouse.get_pos()[1]<=war_machine_rect.y+500:
                    war_color=(211,211,211)

                    if pygame.mouse.get_pressed()[0]==1:
                        image=war_machine_fly
                        image_rect=war_machine_fly_rect
                        game(image_rect,game_status,image_rect2,bgx1,bgx2,bars,image,try_img,BLACK,start,points,count,bg,text,x1,up_stat,name)
                else:
                    war_color=(134,138,136)

                if pygame.mouse.get_pos()[0]>=vision_rect.x and pygame.mouse.get_pos()[0]<=vision_rect.x+200 \
                    and pygame.mouse.get_pos()[1]>=vision_rect.y and pygame.mouse.get_pos()[1]<=vision_rect.y+500:
                    vision_color=(250,237,39)

                    if pygame.mouse.get_pressed()[0]==1:
                        image=vision_fly
                        image_rect=vision_fly_rect
                        game(image_rect,game_status,image_rect2,bgx1,bgx2,bars,image,try_img,BLACK,start,points,count,bg,text,x1,up_stat,name)
                        
                else:
                    vision_color=(255,173,1)


                


            surface.fill((0,0,0))
            surface.blit(bg_player,(0,0))
            pygame.draw.rect(surface,iron_color,ironman_dp_rect)
            pygame.draw.rect(surface,thor_color,thor_rect)
            pygame.draw.rect(surface,falcon_color,falcon_rect)
            pygame.draw.rect(surface,war_color,war_machine_rect)
            pygame.draw.rect(surface,vision_color,vision_rect)
            surface.blit(ironman_dp, ironman_dp_rect)
            surface.blit(war_machine, war_machine_rect)
            
            surface.blit(thor, thor_rect)
            surface.blit(falcon, falcon_rect)
            surface.blit(vision, vision_rect)
                       

            pygame.font.init() 
            myfont = pygame.font.SysFont('Comic Sans MS', 20)
            myfont2 = pygame.font.SysFont('Comic Sans MS', 40)
            ironman_text=myfont.render("IRONMAN" , False,iron_color)
            thor_text=myfont.render("THOR" , False,thor_color)
            war_text=myfont.render("WAR MACHINE" , False,war_color)   
            falcon_text=myfont.render("FALCON" , False,falcon_color)    
            vision_text=myfont.render("VISION" , False,vision_color)     
            player_text=myfont2.render("CHOOSE YOUR PLAYER!",False, (255,110,199))   


            surface.blit(ironman_text,(ironman_dp_rect.x+30,ironman_dp_rect.y+510))
            surface.blit(thor_text,(thor_rect.x+70,thor_rect.y+510))
            surface.blit(falcon_text,(falcon_rect.x+60,falcon_rect.y+510))
            surface.blit(vision_text,(vision_rect.x+50,vision_rect.y+510))
            surface.blit(war_text,(war_machine_rect.x+20,war_machine_rect.y+510))
            surface.blit(player_text,(280,30))
            
            


            pygame.display.update()
            clock=pygame.time.Clock()
            clock.tick(30)
 
