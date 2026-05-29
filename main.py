#imports
import pygame as pg
from constants import *
from level import Level

pg.init()

#clock
clock = pg.time.Clock()

#game window
screen = pg.display.set_mode(( SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("hormiguero")

#load images
level_image = pg.image.load('assets/levels/lvl01.png').convert_alpha()

#create level
cur_level = Level(level_image)

#game loop
run = True
while run:

    clock.tick(TICK_RATE)

    screen.fill("green")

    #draw level
    cur_level.draw(screen)

    for event in pg.event.get():
        #quit game
        if event.type == pg.QUIT:
            run = False

    #display update
    pg.display.flip()
pg.quit()   