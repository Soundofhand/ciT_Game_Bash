#imports
import pygame as pg
from constants import *
from level import Level
from enemies import Enemies

pg.init()

#clock
clock = pg.time.Clock()

#game window
screen = pg.display.set_mode(( SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("hormiguero")

#load images
level_image = pg.image.load('assets/levels/lvl01.png').convert_alpha()
enemy_image = pg.image.load('assets/sprites/enemy1_n.png').convert_alpha()

#create level
cur_level = Level(level_image)

#create group tracking
enemy_group1 = pg.sprite.Group()
#create Enemies
path_nodes = Enemies.draw_enemy_path() #Load a relevant variable for the Enemies class to init
enemy1 = Enemies(path_nodes,enemy_image)
enemy_group1.add(enemy1) #add created enemy to group

#game loop
run = True
while run:

    clock.tick(TICK_RATE) # Is 60 fps

    screen.fill("green")

    #draw level
    cur_level.draw(screen)
    #draw enemy_node_path
    pg.draw.lines(screen, "red", False, path_nodes)

    #Moves all the guys in the group by ?!? 
    enemy1.move_enemy()
    #draw group
    enemy_group1.draw(screen)

    for event in pg.event.get():
        #quit game
        if event.type == pg.QUIT:
            run = False



    #display update
    pg.display.flip()
pg.quit()  
