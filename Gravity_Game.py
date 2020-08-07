from ctypes import windll
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
windll.shcore.SetProcessDpiAwareness(1)
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

class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,w,h)

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,w,h)

class Rect(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,w,h)
        rect_group.add(self)

def Write(message, text, color, pos, center):
    message = message.render(text, True, color)
    if center:
        pos1, pos2 = pos
        pos1 -= message.get_rect().width/2
        pos2 -= message.get_rect().height/2
        screen.blit(message, (pos1, pos2))
    else:
        screen.blit(message, pos)


pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

font = pygame.font.SysFont("Verdana", 30)
dead_message = pygame.font.SysFont("Impact", 150)
question = pygame.font.SysFont("Verdana", 45)
yes = pygame.font.SysFont("Verdana", 35)
no = pygame.font.SysFont("Verdana", 35)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Gravity Game")
clock = pygame.time.Clock()

pygame.mixer.music.load(os.path.abspath("Music.mp3"))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


black = (0, 0, 0)
white = (255, 255, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
color = cyan

g = 11
v = 5
test = 0
points = 0
move = True
width, height = screen.get_size()
last_platform_x, last_platform_y = 0, 0

player = Player(200, 476, 25, 25)
grav_use = Powerup(0, -100, 50, 50)
yes_button = Button(950, 550, 150, 75)
no_button = Button(500, 550, 150, 75)

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
                
        pygame.draw.rect(screen, white, rectangle.rect)
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


#-----------------------------User Inputs---------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if (move == False) or (color == green):
                    if move:
                        test = 1
                    g = -g
                    move = True

        cursor1, cursor2, cursor3 = pygame.mouse.get_pressed()
        if cursor1 == True:
            if pygame.mouse.get_pos() == (0, 0):
                pygame.mixer.music.set_volume(0)
            else:
                pygame.mixer.music.set_volume(0.4)
#-------------------------------------------------------------------------

    pygame.draw.rect(screen, green, grav_use.rect)
    grav_use.rect = grav_use.rect.move(-v, 0)
    if player.rect.colliderect(grav_use.rect):
        color = green
        grav_use.rect = pygame.Rect(0, -100, 50, 50)
    if test == 1:
        color = cyan
        test = 0
    
    pygame.draw.rect(screen, color, player.rect)
    if move:
        player.rect = player.rect.move(0, g)
        
    Write(font, str(points), yellow, (15, 0), False)
    
    if (points%500) == 0:
        grav_use.rect.x, grav_use.rect.y = 1610, random.randint(10, (height-60))
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
            yes_button.rect.center = ((width/2)+300,(height/2)+250)
            no_button.rect.center = ((width/2)-300,(height/2)+250)
            pygame.draw.rect(screen, (150, 0, 0), no_button.rect)
            pygame.draw.rect(screen, (0, 150, 0), yes_button.rect)
            
            Write(dead_message, "Y O U    D I E D", red, (width/2, (height/2)-200), True)
            Write(question, "Would you like to play again?", white, (width/2, (height/2)+100), True)
            Write(yes, "Yes", white, yes_button.rect.center, True)
            Write(no, "No", white, no_button.rect.center, True)

            pygame.display.update()

            for event in pygame.event.get():
                cursor1, cursor2, cursor3 = pygame.mouse.get_pressed()
                if cursor1 == True:
                    pos1, pos2 = pygame.mouse.get_pos()


            try:
                if no_button.rect.collidepoint((pos1, pos2)):
                    pygame.quit()
                    sys.exit()
                    
                if yes_button.rect.collidepoint((pos1, pos2)):
                    del pos1
                    del pos2
                    points = 0
                    move = True
                    g = abs(g)
                    color = cyan
                    r1.rect.x, r1.rect.y = 125, 500
                    r2.rect.x, r2.rect.y = 420, random.randint(10, (height-20))
                    r3.rect.x, r3.rect.y = 615, random.randint(10, (height-20))
                    r4.rect.x, r4.rect.y = 710, random.randint(10, (height-20))
                    r5.rect.x, r5.rect.y = 1005, random.randint(10, (height-20))
                    r6.rect.x, r6.rect.y = 1200, random.randint(10, (height-20))
                    r7.rect.x, r7.rect.y = 1295, random.randint(10, (height-20))
                    r8.rect.x, r8.rect.y = 1590, random.randint(10, (height-20))
                    r9.rect.x, r9.rect.y = 1785, random.randint(10, (height-20))
                    r10.rect.x, r10.rect.y = 1880, random.randint(10, (height-20))
                    player.rect.x, player.rect.y = 200, 476
                    grav_use.rect.x, grav_use.rect.y = 0, -100

                    screen.fill(black)
                    distance = font.render(str(points), True, yellow)
                    screen.blit(distance,(15, 0))
                    for rectangle in rect_group:
                        pygame.draw.rect(screen, white, rectangle.rect)
                    pygame.draw.rect(screen, color, player.rect)
                    pygame.display.update()
                    time.sleep(2)
                    break
            except NameError:
                pass
#-------------------------------------------------------------------------------------------
            
        
    pygame.display.update()
    clock.tick(70)








