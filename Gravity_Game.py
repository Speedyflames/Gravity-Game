import pygame
import sys
import random
import time


#--------------------------Setup----------------------------
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

width, height = 1000, 600
pygame.init()   
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravity Game")
clock = pygame.time.Clock()
#----------------------------------------------------------


#-----------------------Variables----------------------
black = (0, 0, 0)
white = (255, 255, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
color = white

g = 9
v = 5
points, deaths = 0, 0
move = True
last_platform_x, last_platform_y = 0, 0

player = Player(200, 476, 25, 25)

r1 = Rect(125, 500, 300, 10)
r2 = Rect(420, random.randint(10, 590), 200, 10)
r3 = Rect(615, random.randint(10, 590), 100, 10)
r4 = Rect(710, random.randint(10, 590), 300, 10)
r5 = Rect(1005, random.randint(10, 590), 200, 10)
r6 = Rect(1200, random.randint(10, 590), 100, 10)
#------------------------------------------------------



while True:
    move = True
    screen.fill(black)

    if deaths == 1:
        color = yellow
    if deaths == 2:
        color = red
    if deaths == 3:
        color = black
        cyan = black
        
#---------------------------------Blocks----------------------------------
    for rectangle in rect_group:
        if rectangle.rect.right < 0:
            rectangle.rect.y = random.randint(0, 590)
            rectangle.rect.left = last_platform_x 
            if 35 > abs((rectangle.rect.y - last_platform_y)):
                rectangle.rect.y = random.randint(0, 590)
        pygame.draw.rect(screen, color, rectangle.rect)
        last_platform_x = (rectangle.rect.x + rectangle.rect.width) - 5
        last_platform_y = rectangle.rect.y
        
        if player.rect.colliderect(rectangle.rect):
            move = False
            if player.rect.y <= rectangle.rect.y:
                player.rect.y = rectangle.rect.y - 24
            else:
                player.rect.y = rectangle.rect.y + 9
                
        rectangle.rect = rectangle.rect.move(-v, 0)
#-------------------------------------------------------------------------


    for event in pygame.event.get():
        if event.type == pygame.QUIT or deaths > 2:
            pygame.quit()
            print("You travelled " + str(points) + " points")
            a = str(input("Are you sure you want to quit?  "))
            if a == 'no' or a == 'No':
                deaths, points = 0, 0
                move = True
                cyan = (0, 255, 255)
                color = white
                pygame.init()   
                screen = pygame.display.set_mode((width, height))
                pygame.display.set_caption("Gravity Game")
                clock = pygame.time.Clock()

                r1.rect = pygame.Rect(125, 500, 300, 10)
                r2.rect = pygame.Rect(420, random.randint(0, 590), 200, 10)
                r3.rect = pygame.Rect(615, random.randint(0, 590), 100, 10)
                r4.rect = pygame.Rect(710, random.randint(0, 590), 300, 10)
                r5.rect = pygame.Rect(1005, random.randint(0, 590), 200, 10)
                r6.rect = pygame.Rect(1200, random.randint(0, 590), 100, 10)
                player.rect = pygame.Rect(200, 476, 25, 25)
            else:
                sys.exit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if move == False:
                    g = -g
                    move = True

        
    pygame.draw.rect(screen, cyan, player.rect)
    if move:
        player.rect = player.rect.move(0, g)
    points += 1

        
#------------------------------------Reset---------------------------------------
    if player.rect.y > (height + 30) or player.rect.y < (-45):
        g = abs(g)
        move = True
        deaths += 1

        if deaths == 1:
            color = yellow
        if deaths == 2:
            color = red
        if deaths == 3:
            color = black
            cyan = black
            
        r1.rect = pygame.Rect(125, 500, 300, 10)
        r2.rect = pygame.Rect(420, random.randint(0, 590), 200, 10)
        r3.rect = pygame.Rect(615, random.randint(0, 590), 100, 10)
        r4.rect = pygame.Rect(710, random.randint(0, 590), 300, 10)
        r5.rect = pygame.Rect(1005, random.randint(0, 590), 200, 10)
        r6.rect = pygame.Rect(1200, random.randint(0, 590), 100, 10)
        player.rect = pygame.Rect(200, 476, 25, 25)
        
        screen.fill(black)
        for rectangle in rect_group:
            pygame.draw.rect(screen, color, rectangle.rect)
        pygame.draw.rect(screen, cyan, player.rect)
        pygame.display.update()
        time.sleep(1.5)
#---------------------------------------------------------------------------------
            
        
    pygame.display.update()
    clock.tick(65)
