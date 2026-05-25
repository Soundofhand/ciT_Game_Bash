#imports
import pygame as pg
from constants import *



pg.init()

#clock
clock = pg.time.Clock()


#game window
screen = pg.display.set_mode(( SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("hormiguero")

#game loop
run = True
while run:

    clock.tick(TICK_RATE)

    for event in pg.event.get():
        #quit game
        if event.type == pg.QUIT:
            run = False

pg.quit()   