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
from colors import Colors
from whitebloodcell import WhiteBloodCell
from bullet import *
from virus import *
from booster import *
from background import ScrollingBackground

#MACROS
SIZE = WIDTH, HEIGHT = 1280, 720
PLAYER_SIZE = 60
PLAYER_SPEED = 5
BULLET_SIZE = 25
BULLET_SPEED = 5
BULLET_NUMBER = 3
ENEMY_SIZE = 30
OMICRON_SIZE = 50
DELTA_SIZE = 80
ENEMY_SPEED = 3
ENEMY_NUMBER = 5
POWERUP_SIZE = 50
POWERUP_SPEED = 5

#initialize modules
pygame.mixer.pre_init(44100, 32, 2, 4096)
pygame.init()
clock = pygame.time.Clock()

#music play
if pygame.mixer:
    music_path = os.path.join('sounds', "bgm.wav")
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1) #-1 reapeat

#create a graphical window 
screen = pygame.display.set_mode(SIZE)
#caption
pygame.display.set_caption("Sideshooter Game")
#icon
icon = pygame.image.load(os.path.join('img', 'wbc.png')).convert_alpha()
icon = pygame.transform.smoothscale(icon, (64, 64))
pygame.display.set_icon(icon)

#fonts
font = pygame.font.SysFont(None, 24)
font_big = pygame.font.SysFont(None, 64)

#create background
background = ScrollingBackground(image="bg.jpg", width=WIDTH, height=HEIGHT)
backgr_particles = ScrollingBackground(image="particles_red.png", width=WIDTH, height=HEIGHT, speed=2)

print("\t #### CREATING ELEMENTS ####")
#create game_elements group
game_elements_group = pygame.sprite.Group()

#create player
player = WhiteBloodCell('wbc.png', position_x=20, position_y=20, height=PLAYER_SIZE, width=PLAYER_SIZE, speed_x=PLAYER_SPEED, speed_y=PLAYER_SPEED)
game_elements_group.add(player)


#create bullets
bullets_group = pygame.sprite.Group()
for num_bullet in range(BULLET_NUMBER):
    b = NormalBullet("wbc.png", position_x=WIDTH/2+30+BULLET_SIZE*num_bullet, position_y=5, height=BULLET_SIZE, width=BULLET_SIZE, speed_x=BULLET_SPEED)
    bullets_group.add(b)
    game_elements_group.add(b)
    
#create enemies
enemies_group = pygame.sprite.Group()
for num_enemy in range(ENEMY_NUMBER):
    e = Covid19(image="virus.png", position_x=random.randint(WIDTH, 2*WIDTH), position_y=random.randint(0, HEIGHT-ENEMY_SIZE), height=ENEMY_SIZE, width=ENEMY_SIZE, speed_x=ENEMY_SPEED)
    enemies_group.add(e)
    game_elements_group.add(e)

om_enemy = Omicron(image="virus2.png", position_x=random.randint(2*WIDTH, 3*WIDTH), position_y=random.randint(0, HEIGHT-OMICRON_SIZE), height=OMICRON_SIZE, width=OMICRON_SIZE, speed_x=4)
enemies_group.add(om_enemy)
game_elements_group.add(om_enemy)

del_enemy = Delta(image="virus3.png", position_x=random.randint(3*WIDTH, 4*WIDTH), position_y=random.randint(0, HEIGHT-DELTA_SIZE), height=DELTA_SIZE, width=DELTA_SIZE, speed_x=2)
enemies_group.add(del_enemy)
game_elements_group.add(del_enemy)

#create powerups
powerup_group = pygame.sprite.Group()
mask = Mask(image="mask.png", position_x=random.randint(6*WIDTH, 8*WIDTH), position_y=random.randint(0, HEIGHT-POWERUP_SIZE), height=POWERUP_SIZE, width=POWERUP_SIZE, speed_x=POWERUP_SPEED)
powerup_group.add(mask)
game_elements_group.add(mask)

vaccine = Vaccine(image="vaccine.png", position_x=random.randint(4*WIDTH, 6*WIDTH), position_y=random.randint(0, HEIGHT-POWERUP_SIZE), height=POWERUP_SIZE, width=POWERUP_SIZE, speed_x=POWERUP_SPEED)
powerup_group.add(vaccine)
game_elements_group.add(vaccine)


for elem in game_elements_group:
    print(elem)

print("\t #### GAME STARTED ####")

#Game Loop (while 1 saves one operation instead of while true)
while 1: 
    clock.tick(60) #FPS

    # EVENTS (get input)
    for event in pygame.event.get():
        if (event.type==pygame.QUIT) or (event.type==pygame.KEYDOWN and event.key==K_ESCAPE): 
            #closing game
            fadeout = pygame.Surface(SIZE).convert()
            fadeout.fill(Colors.BLACK)
            for i in range(90):
                pygame.time.delay(10)
                fadeout.set_alpha(i)
                screen.blit(fadeout, (0, 0))
                pygame.display.update() #if no rectagle passed, updates the whole display, like flip()
            if pygame.mixer:
                pygame.mixer.music.fadeout(1000)
            pygame.quit()
            sys.exit()

        #even triggered only on key press
        if event.type == pygame.KEYDOWN:
            #KEY is V (shoot) or SPACE
            if event.key == pygame.K_v or event.key == pygame.K_SPACE:
                player_pos = player.get_position()  
                for b in bullets_group:
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


    # MOVE (update)
    for elem in game_elements_group:
        elem.move_autonomously()

    # COLLISION DETECTION
    # update rectangle position for every game object
    ## Note: the self.rect is used for collisions, but since we used position_x and position_y when moving, this is not updated
    ## moving the rectangle and drawing the sprite based on it's position is a faster approach but less understandable in the code
    for elem in game_elements_group:
        elem.update_rect()

    #check collisions plyer vs enemies
    enemy_collided_player = pygame.sprite.spritecollideany(player, enemies_group)
    if enemy_collided_player:
        print("Health loss: {}".format(enemy_collided_player.damage))
        player.lose_health(enemy_collided_player.damage)
        player.gain_score(enemy_collided_player.MAX_HEALTH)
        enemy_collided_player.reset()
        #pygame.time.delay(100)

    #check collisions bullets vs enemies
    collisions_bull_enem = pygame.sprite.groupcollide(bullets_group, enemies_group, False, False)
    if collisions_bull_enem:
        for bullet in collisions_bull_enem:
            for enemy in collisions_bull_enem[bullet]:
                enemy.lose_health(bullet.damage)
                player.gain_score(bullet.damage)
                bullet.reset()

    #check collisions bullets vs powerups
    collisions_bull_powerup = pygame.sprite.groupcollide(bullets_group, powerup_group, False, False)
    if collisions_bull_powerup:
        for bullet in collisions_bull_powerup:
            for powerup in collisions_bull_powerup[bullet]:
                powerup.lose_health(bullet.damage)
                bullet.reset()


    #check collisions player vs powerup
    powerup_collided_player = pygame.sprite.spritecollideany(player, powerup_group)
    if powerup_collided_player:
        print("Powerup collected: health increase {} protection time: {}".format(powerup_collided_player.health_increase, powerup_collided_player.collision_protection_time))
        player.gain_health(powerup_collided_player.health_increase)
        player.set_protected_sec(powerup_collided_player.collision_protection_time)
        powerup_collided_player.reset()

    #check health
    if not player.is_alive():
        if pygame.mixer:
            pygame.mixer.music.fadeout(1000)
        #closing game
        gameover_surface = font_big.render(f"GAME OVER", True, Colors.RED)
        gameover_rect = gameover_surface.get_rect(center=(WIDTH/2, HEIGHT/3))
        score_surface = font.render(f"Score: {player.score}", True, Colors.WHITE)
        score_rect = score_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
        fadeout = pygame.Surface(SIZE).convert()
        fadeout.fill(Colors.BLACK)
        for i in range(90):
            pygame.time.delay(20)
            screen.blit(gameover_surface, gameover_rect)
            screen.blit(score_surface, score_rect)
            fadeout.set_alpha(i)
            screen.blit(fadeout, (0, 0))
            pygame.display.update()
        print("Resetting player")
        player.reset()

    # DRAW (render)
    screen.fill(Colors.BLACK)
    #draw background 
    background.move()
    background.draw(screen)
    #dreaw background particles
    backgr_particles.move()
    backgr_particles.draw(screen)
    #draw score
    score_surface = font.render(f"Score: {player.score}", True, Colors.WHITE)
    screen.blit(score_surface, (32,10))
    #draw game_elements_group on screen
    for elem in game_elements_group:
        elem.draw(screen)
    #makes everything we have drawn on the Screen Surface become Visible
    pygame.display.flip()

