import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import random
import time


#----------------------------Setup------------------------------
rect_group = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,w,h)

class Rect(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,w,h)
        rect_group.add(self)

width, height = 1600, 870
pygame.init()

font = pygame.font.SysFont("Verdana", 30)
dead_message = pygame.font.SysFont("Impact", 150)
question = pygame.font.SysFont("Verdana", 45)
yes = pygame.font.SysFont("Verdana", 35)
no = pygame.font.SysFont("Verdana", 35)

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Gravity Game")
clock = pygame.time.Clock()
#--------------------------------------------------------------


#---------------------------Variables--------------------------
black = (0, 0, 0)
white = (255, 255, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
color = white

g = 11
v = 5
points = 0
move = True
last_platform_x, last_platform_y = 0, 0

player = Player(200, 476, 25, 25)

r1 = Rect(125, 500, 300, 10)
r2 = Rect(420, random.randint(10, (height-20)), 200, 10)
r3 = Rect(615, random.randint(10, (height-20)), 100, 10)
r4 = Rect(710, random.randint(10, (height-20)), 300, 10)
r5 = Rect(1005, random.randint(10, (height-20)), 200, 10)
r6 = Rect(1200, random.randint(10, (height-20)), 100, 10)
r7 = Rect(1295, random.randint(10, (height-20)), 300, 10)
r8 = Rect(1590, random.randint(10, (height-20)), 200, 10)
r9 = Rect(1785, random.randint(10, (height-20)), 100, 10)
r10 = Rect(1880, random.randint(10, (height-20)), 200, 10)
#--------------------------------------------------------------



while True:
    move = True
    screen.fill(black)
        
#---------------------------------Blocks----------------------------------
    for rectangle in rect_group:
        if rectangle.rect.right < 0:
            rectangle.rect.y = random.randint(10, (height-20))
            rectangle.rect.left = last_platform_x
            if 35 > abs((rectangle.rect.y - last_platform_y)):
                rectangle.rect.y = random.randint(10, (height-20))
                
        pygame.draw.rect(screen, color, rectangle.rect)
        last_platform_x = (rectangle.rect.x + rectangle.rect.width) - 5
        last_platform_y = rectangle.rect.y
        
        if player.rect.colliderect(rectangle.rect):
            move = False
            if g < 0:
                player.rect.y = rectangle.rect.y + 9
            else:
                player.rect.y = rectangle.rect.y - 24
                
        rectangle.rect = rectangle.rect.move(-v, 0)
#-------------------------------------------------------------------------


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if move == False:
                    g = -g
                    move = True
                    
        
    pygame.draw.rect(screen, cyan, player.rect)
    if move:
        player.rect = player.rect.move(0, g)
    distance = font.render(str(points), True, yellow)
    screen.blit(distance,(15, 0))
    points += 1

        
#-----------------------------------------Reset--------------------------------------------
    if player.rect.y > (height + 50) or player.rect.y < (-50):
        screen.fill(black, (0, 0, 300, 40))
        distance = font.render("You scored " + str(points) + " points", True, yellow)
        screen.blit(distance,(15, 0))
        pygame.display.update()
        time.sleep(3)


        while True:
            screen.fill(black)
            pygame.draw.rect(screen, (150, 0, 0), (500, 550, 150, 75))
            pygame.draw.rect(screen, (0, 150, 0), (950, 550, 150, 75))
            dead = dead_message.render("Y O U    D I E D", True, red)
            screen.blit(dead,(435, 100))
            ques = question.render("Would you like to play again?", True, white)
            screen.blit(ques,(475, 425))
            da = yes.render("Yes", True, white)
            screen.blit(da,(995, 565))
            nyet = no.render("No", True, white)
            screen.blit(nyet,(550, 565))
            pygame.display.update()

            for event in pygame.event.get():
                cursor1, cursor2, cursor3 = pygame.mouse.get_pressed()
                if cursor1 == True:
                    pos1, pos2 = pygame.mouse.get_pos()


            try:
                if (pos1 < 650) and (pos1 > 500) and (pos2 < 625) and (pos2 > 550):
                    pygame.quit()
                    sys.exit()
                    
                if (pos1 < 1100) and (pos1 > 950) and (pos2 < 625) and (pos2 > 550):
                    del pos1
                    del pos2
                    points = 0
                    move = True
                    g = abs(g)
                    r1.rect = pygame.Rect(125, 500, 300, 10)
                    r2.rect = pygame.Rect(420, random.randint(10, (height-20)), 200, 10)
                    r3.rect = pygame.Rect(615, random.randint(10, (height-20)), 100, 10)
                    r4.rect = pygame.Rect(710, random.randint(10, (height-20)), 300, 10)
                    r5.rect = pygame.Rect(1005, random.randint(10, (height-20)), 200, 10)
                    r6.rect = pygame.Rect(1200, random.randint(10, (height-20)), 100, 10)
                    r7.rect = pygame.Rect(1295, random.randint(10, (height-20)), 300, 10)
                    r8.rect = pygame.Rect(1590, random.randint(10, (height-20)), 200, 10)
                    r9.rect = pygame.Rect(1785, random.randint(10, (height-20)), 100, 10)
                    r10.rect = pygame.Rect(1880, random.randint(10, (height-20)), 200, 10)
                    player.rect = pygame.Rect(200, 476, 25, 25)

                    screen.fill(black)
                    distance = font.render(str(points), True, yellow)
                    screen.blit(distance,(15, 0))
                    for rectangle in rect_group:
                        pygame.draw.rect(screen, color, rectangle.rect)
                    pygame.draw.rect(screen, cyan, player.rect)
                    pygame.display.update()
                    time.sleep(2)
                    break
            except NameError:
                pass
#-------------------------------------------------------------------------------------------
            
        
    pygame.display.update()
    clock.tick(70)








