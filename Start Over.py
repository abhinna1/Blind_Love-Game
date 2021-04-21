import pygame,sys

window_size=(500,500)
screen=pygame.display.set_mode((window_size[0],window_size[1]))

player_x=0
player_y=100
player=pygame.image.load('png files/Still Animation/Still Character Animation1.png')

player_velocity=5
gravity=1
run=True

key=pygame.key.get_pressed()
left=False
right=False

if left==True:
    player_x -= player_velocity
if right==True:
    player_x += player_velocity

while run:
    screen.blit(player,(player_x,player_y))
    # if player_y<window_size[1]:
    #     player_y+=gravity

    if key[pygame.K_RIGHT]:
        right=True
    if key[pygame.K_LEFT]:
        left=True

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()