import sys, os, pygame
from whitebloodcell import WhiteBloodCell
#initialize modules
pygame.init()

SIZE = width, height = 720, 480
speed = [2, 2]
BLACK = 0, 0, 0

#create a graphical window 
screen = pygame.display.set_mode(SIZE)

player = WhiteBloodCell('wbc.png', 0,0, width=90)

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()


    #DRAW PART
    #draw backround in black
    screen.fill(BLACK)
    #draw player on screen
    player.draw(screen)
    #makes everything we have drawn on the screen Surface become Visible
    pygame.display.flip()

"""
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    QUIT,
)
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