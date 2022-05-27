import sys, os
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

SIZE = WIDTH, HEIGHT = 720, 480
BLACK = 0, 0, 0

#initialize modules
pygame.init()
clock = pygame.time.Clock()

#create a graphical window 
screen = pygame.display.set_mode(SIZE)

#create player
player = WhiteBloodCell('wbc.png', position_x=10, position_y=10, height=60, width=90, speed_x=5, speed_y=5)

#Game Loop
while True:
    clock.tick(60) #FPS

    for event in pygame.event.get():
        if (event.type==pygame.QUIT) or (event.type==pygame.KEYDOWN and event.key==K_ESCAPE): 
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                player.up()
            elif event.key == K_DOWN:
                player.down()

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

    #DRAW PART
    #draw backround in black
    screen.fill(BLACK)
    #draw player on screen
    player.draw(screen)
    #makes everything we have drawn on the screen Surface become Visible
    pygame.display.flip()

"""

class Game:
    def __init__(self):
        self.speed_up()
        self.pause()
        self.resume()
        self.speed_down()
        self.turn_right
        self.turn_left()

    def start_game_image(self):
        self.start()

    def finish_game_image(self):
        self.exit()


"""