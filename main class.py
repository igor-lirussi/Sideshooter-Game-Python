#IMPORTS
import sys, os
import random
import pygame
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    QUIT,
)
from whitebloodcell import WhiteBloodCell
from bullet import *
from virus import *

#MACROS
SIZE = WIDTH, HEIGHT = 720, 480
PLAYER_SIZE = 60
PLAYER_SPEED = 5
BULLET_SIZE = 25
BULLET_SPEED = 5
BULLET_NUMBER = 3
ENEMY_SIZE = 30
ENEMY_SPEED = 3
ENEMY_NUMBER = 5
#colors
BLACK = 0, 0, 0


#initialize modules
pygame.init()
clock = pygame.time.Clock()

#create a graphical window 
screen = pygame.display.set_mode(SIZE)
#caption
pygame.display.set_caption("Sideshooter Game")
#icon
icon = pygame.image.load(os.path.join('img', 'wbc.png')).convert_alpha()
icon = pygame.transform.smoothscale(icon, (64, 64))
pygame.display.set_icon(icon)

#create game_elements to be drawn array
game_elements = []

#create player
player = WhiteBloodCell('wbc.png', position_x=20, position_y=20, height=PLAYER_SIZE, width=PLAYER_SIZE, speed_x=PLAYER_SPEED, speed_y=PLAYER_SPEED)
game_elements.append(player)

#create bullets
bullets = []
for num_bullet in range(BULLET_NUMBER):
    b = NormalBullet("wbc.png", position_x=WIDTH/2+BULLET_SIZE*num_bullet, position_y=5, damage=20, height=BULLET_SIZE, width=BULLET_SIZE, speed_x=BULLET_SPEED)
    bullets.append(b)
game_elements = game_elements + bullets
    
#create enemies
enemies = []
for num_enemy in range(ENEMY_NUMBER):
    e = Omicron(image="virus.png", position_x=random.randint(WIDTH, 2*WIDTH), position_y=random.randint(0, WIDTH-ENEMY_SIZE), height=ENEMY_SIZE, width=ENEMY_SIZE, speed_x=ENEMY_SPEED, speed_y=ENEMY_SPEED)
    enemies.append(e)
    print(e)
game_elements = game_elements + enemies


#Game Loop
while True:
    clock.tick(60) #FPS

    # EVENTS
    for event in pygame.event.get():
        if (event.type==pygame.QUIT) or (event.type==pygame.KEYDOWN and event.key==K_ESCAPE): 
            #closing game
            fadeout = pygame.Surface(SIZE).convert()
            fadeout.fill(BLACK)
            for i in range(90):
                pygame.time.delay(10)
                fadeout.set_alpha(i)
                screen.blit(fadeout, (0, 0))
                pygame.display.update()
            if pygame.mixer:
                pygame.mixer.music.fadeout(1000)
            pygame.quit()
            sys.exit()

        #even triggered only on key press
        if event.type == pygame.KEYDOWN:
            #KEY is V (shoot)
            if event.key == pygame.K_v:
                player_pos = player.get_position()
                for b in bullets:
                    if b.is_ready():
                        b.fire(player_pos[0]+PLAYER_SIZE, player_pos[1]+(PLAYER_SIZE-BULLET_SIZE)/2)
                        break

    #get keyboard state to understand the keys kept pressed
    keyboardstate = pygame.key.get_pressed()
    if keyboardstate[K_RIGHT]:
        player.right()
    if keyboardstate[K_LEFT]:
        player.left()
    if keyboardstate[K_UP]:     
        player.up()
    if keyboardstate[K_DOWN]:
        player.down()       

    # MOVE
    for elem in game_elements:
        elem.move_autonomously()

    # DRAW 
    #draw backround in black
    screen.fill(BLACK)
    #draw game_elements on screen
    for elem in game_elements:
        elem.draw(screen)
    #makes everything we have drawn on the screen Surface become Visible
    pygame.display.flip()

