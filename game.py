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

from resourcepath import resource_path

class Game():
    """main Game"""
    def __init__(self):
        #MACROS
        self.SIZE = self.WIDTH, self.HEIGHT = 1280, 720
        self.PLAYER_SIZE = 60
        self.PLAYER_SPEED = 5
        self.BULLET_SIZE = 25
        self.ROCKET_SIZE = 35
        self.BULLET_SPEED = 5
        self.BULLET_NUMBER = 3
        self.ENEMY_SIZE = 30
        self.OMICRON_SIZE = 50
        self.DELTA_SIZE = 80
        self.ENEMY_SPEED = 3
        self.ENEMY_NUMBER = 5
        self.POWERUP_SIZE = 50
        self.POWERUP_SPEED = 5

        #initialize modules
        pygame.mixer.pre_init(44100, 32, 2, 4096)
        pygame.init()
        self.clock = pygame.time.Clock()

        #music play
        if pygame.mixer:
            music_path = os.path.join('sounds', "bgm.wav")
            pygame.mixer.music.load(resource_path(music_path))
            pygame.mixer.music.play(-1) #-1 reapeat

        #create a graphical window 
        self.screen = pygame.display.set_mode(self.SIZE)
        #caption
        pygame.display.set_caption("Sideshooter Game")
        #icon
        icon = pygame.image.load(resource_path(os.path.join('img', 'wbc.png'))).convert_alpha()
        icon = pygame.transform.smoothscale(icon, (64, 64))
        pygame.display.set_icon(icon)

        #fonts
        self.font = pygame.font.SysFont(None, 24)
        self.font_big = pygame.font.SysFont(None, 64)

        #create background
        self.background = ScrollingBackground(image="bg.jpg", width=self.WIDTH, height=self.HEIGHT)
        self.backgr_particles = ScrollingBackground(image="particles_red.png", width=self.WIDTH, height=self.HEIGHT, speed=2)

        print("\t #### CREATING GAME ELEMENTS ####")
        #create game_elements group
        self.game_elements_group = pygame.sprite.Group()

        #create player
        self.player = WhiteBloodCell('wbc.png', position_x=20, position_y=20, height=self.PLAYER_SIZE, width=self.PLAYER_SIZE, speed_x=self.PLAYER_SPEED, speed_y=self.PLAYER_SPEED)
        self.game_elements_group.add(self.player)


        #create bullets
        self.bullets_and_rocket_group = pygame.sprite.Group()
        self.r = Rocket("wbc2.png", position_x=self.WIDTH/2+80+self.ROCKET_SIZE, position_y=5, height=self.ROCKET_SIZE, width=self.ROCKET_SIZE, speed_x=2, speed_y=2)
        self.bullets_and_rocket_group.add(self.r)
        self.game_elements_group.add(self.r)
        self.bullets_group = pygame.sprite.Group()
        for num_bullet in range(self.BULLET_NUMBER):
            b = NormalBullet("wbc.png", position_x=self.WIDTH/2+30+self.BULLET_SIZE*num_bullet, position_y=5, height=self.BULLET_SIZE, width=self.BULLET_SIZE, speed_x=self.BULLET_SPEED)
            self.bullets_group.add(b)
            self.bullets_and_rocket_group.add(b)
            self.game_elements_group.add(b)
            
        #create enemies
        self.enemies_group = pygame.sprite.Group()
        for num_enemy in range(self.ENEMY_NUMBER):
            e = Covid19(image="virus.png", position_x=random.randint(self.WIDTH, 2*self.WIDTH), position_y=random.randint(0, self.HEIGHT-self.ENEMY_SIZE), height=self.ENEMY_SIZE, width=self.ENEMY_SIZE, speed_x=self.ENEMY_SPEED)
            self.enemies_group.add(e)
            self.game_elements_group.add(e)

        om_enemy = Omicron(image="virus2.png", position_x=random.randint(2*self.WIDTH, 3*self.WIDTH), position_y=random.randint(0, self.HEIGHT-self.OMICRON_SIZE), height=self.OMICRON_SIZE, width=self.OMICRON_SIZE, speed_x=4)
        self.enemies_group.add(om_enemy)
        self.game_elements_group.add(om_enemy)

        del_enemy = Delta(image="virus3.png", position_x=random.randint(3*self.WIDTH, 4*self.WIDTH), position_y=random.randint(0, self.HEIGHT-self.DELTA_SIZE), height=self.DELTA_SIZE, width=self.DELTA_SIZE, speed_x=2)
        self.enemies_group.add(del_enemy)
        self.game_elements_group.add(del_enemy)

        #create powerups
        self.powerup_group = pygame.sprite.Group()

        mask = Mask(image="mask.png", position_x=random.randint(6*self.WIDTH, 8*self.WIDTH), position_y=random.randint(0, self.HEIGHT-self.POWERUP_SIZE), height=self.POWERUP_SIZE, width=self.POWERUP_SIZE, speed_x=self.POWERUP_SPEED)
        self.powerup_group.add(mask)
        self.game_elements_group.add(mask)

        vaccine = Vaccine(image="vaccine.png", position_x=random.randint(4*self.WIDTH, 6*self.WIDTH), position_y=random.randint(0, self.HEIGHT-self.POWERUP_SIZE), height=self.POWERUP_SIZE, width=self.POWERUP_SIZE, speed_x=self.POWERUP_SPEED)
        self.powerup_group.add(vaccine)
        self.game_elements_group.add(vaccine)

        print("\t #### GAME CREATED ####")
        for elem in self.game_elements_group:
            print(elem)

    def run(self):
        print("\t #### GAME RUNNING ####")
        #Game Loop (while 1 saves one operation instead of while true)
        while 1: 
            self.clock.tick(60) #FPS

            # EVENTS (get input)
            for event in pygame.event.get():
                if (event.type==pygame.QUIT) or (event.type==pygame.KEYDOWN and event.key==K_ESCAPE): 
                    #closing game
                    self.reset()
                    self.close()

                #event triggered only on key press
                if event.type == pygame.KEYDOWN:
                    player_pos = self.player.get_position()  
                    #KEY is B (shoot) or SPACE
                    if event.key == pygame.K_b or event.key == pygame.K_SPACE:
                        for b in self.bullets_group:
                            if b.is_ready():
                                b.fire(player_pos[0]+self.PLAYER_SIZE, player_pos[1]+(self.PLAYER_SIZE-self.BULLET_SIZE)/2)
                                break
                    #KEY is V (shoot rocket)
                    if event.key == pygame.K_v:
                            if self.r.is_ready():
                                self.r.fire(player_pos[0]+self.PLAYER_SIZE, player_pos[1]+(self.PLAYER_SIZE-self.BULLET_SIZE)/2)
                                break

            #get keyboard state to understand the keys kept pressed
            keyboardstate = pygame.key.get_pressed()
            if keyboardstate[K_RIGHT]:
                self.player.right()
            if keyboardstate[K_LEFT]:
                self.player.left()
            if keyboardstate[K_UP]:     
                self.player.up()
            if keyboardstate[K_DOWN]:
                self.player.down()       


            # MOVE (update)
            for elem in self.game_elements_group:
                elem.move_autonomously()

            # COLLISION DETECTION
            # update rectangle position for every game object
            ## Note: the self.rect is used for collisions, but since we used position_x and position_y when moving, this is not updated
            ## moving the rectangle and drawing the sprite based on it's position is a faster approach but less understandable in the code
            for elem in self.game_elements_group:
                elem.update_rect()

            #check collisions plyer vs enemies
            enemy_collided_player = pygame.sprite.spritecollideany(self.player, self.enemies_group)
            if enemy_collided_player:
                print("Player hit. Health loss: {}".format(enemy_collided_player.damage))
                self.player.lose_health(enemy_collided_player.damage)
                self.player.gain_score(enemy_collided_player.MAX_HEALTH)
                enemy_collided_player.reset()
                #pygame.time.delay(100)

            #check collisions bullets vs enemies
            collisions_bull_enem = pygame.sprite.groupcollide(self.bullets_and_rocket_group, self.enemies_group, False, False)
            for bullet in collisions_bull_enem:
                for enemy in collisions_bull_enem[bullet]:
                    print("Enemy hit. Health loss: {}".format(bullet.damage))
                    enemy.lose_health(bullet.damage)
                    self.player.gain_score(bullet.damage)
                    bullet.reset()

            #check collisions bullets vs powerups
            collisions_bull_powerup = pygame.sprite.groupcollide(self.bullets_and_rocket_group, self.powerup_group, False, False)
            for bullet in collisions_bull_powerup:
                for powerup in collisions_bull_powerup[bullet]:
                    print("Powerup hit. Health loss: {}".format(bullet.damage))
                    powerup.lose_health(bullet.damage)
                    bullet.reset()


            #check collisions player vs powerup
            powerup_collided_player = pygame.sprite.spritecollideany(self.player, self.powerup_group)
            if powerup_collided_player:
                print("Powerup collected: health increase {} protection time: {}".format(powerup_collided_player.health_increase, powerup_collided_player.collision_protection_time))
                self.player.gain_health(powerup_collided_player.health_increase)
                self.player.set_protected_sec(powerup_collided_player.collision_protection_time)
                powerup_collided_player.reset()

            #check health
            if not self.player.is_alive():
                print("Player Dead")
                self.reset()

            # DRAW (render)
            self.screen.fill(Colors.BLACK)
            #draw background 
            self.background.move()
            self.background.draw(self.screen)
            #dreaw background particles
            self.backgr_particles.move()
            self.backgr_particles.draw(self.screen)
            #draw score
            score_surface = self.font.render(f"Score: {self.player.score}", True, Colors.WHITE)
            self.screen.blit(score_surface, (32,10))
            #draw game_elements_group on self.screen
            for elem in self.game_elements_group:
                elem.draw(self.screen)
            #makes everything we have drawn on the Screen Surface become Visible
            pygame.display.flip()



    def reset(self):
        if pygame.mixer:
            pygame.mixer.music.fadeout(1000)
        #draw game over
        gameover_surface = self.font_big.render(f"GAME OVER", True, Colors.RED)
        gameover_rect = gameover_surface.get_rect(center=(self.WIDTH/2, self.HEIGHT/3))
        score_surface = self.font.render(f"Score: {self.player.score}", True, Colors.WHITE)
        score_rect = score_surface.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
        fadeout = pygame.Surface(self.SIZE).convert()
        fadeout.fill(Colors.BLACK)
        for i in range(90):
            pygame.time.delay(25)
            self.screen.blit(gameover_surface, gameover_rect)
            self.screen.blit(score_surface, score_rect)
            fadeout.set_alpha(i)
            self.screen.blit(fadeout, (0, 0))
            pygame.display.update()
        print("Resetting")
        for elem in self.game_elements_group:
                elem.reset()
        pygame.mixer.music.play(-1) #-1 reapeat

    def close(self):
        print("Closing")
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()