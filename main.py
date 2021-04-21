import pygame,sys
from pytmx.util_pygame import load_pygame
pygame.init()
screen_width=1024
screen_height=768
screen=pygame.display.set_mode((screen_width,screen_height))


def mapLoad(window, file, offset):
    for layer in file:
        for tiles in layer:
            print(tiles)


run=True
mapLoad(screen,'Tile Maps/level1Tile.tmx',[0,0])
while run:
    offset=[0,0]

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()