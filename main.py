import pygame,sys
pygame.init()#initializing pygame

screen=pygame.display.set_mode((1000,600))#Window Resolution
title=pygame.display.set_caption('Blind Love')#Window Title

clock=pygame.time.Clock()

ground=pygame.transform.scale(pygame.image.load('png files/Ground.png'),(1000,500))
sky=pygame.image.load('png files/Sky.png')
sky=pygame.transform.scale(sky,(1000,1000))
clouds=pygame.transform.scale(pygame.image.load('png files/clouds.png'),(700,600))

#sky=pygame.transform.scale2x(sky)
character = pygame.image.load('png files/Still Animation/Still Character Animation1.png')

#Character info
char_x=50
char_y=432
char_vel=5

while True:
    key = pygame.key.get_pressed()

    screen.blit(sky, (0, -50))
    screen.blit(clouds, (-100, -50))
    screen.blit(clouds, (500, -100))
    screen.blit(ground, (0, 120))
    screen.blit(character, (char_x, char_y))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
            sys.exit()
        if key[pygame.K_d]or key[pygame.K_RIGHT]:
            char_x=char_x+char_vel
        if key[pygame.K_a]or key[pygame.K_LEFT]:
            char_x=char_x-char_vel





    pygame.display.update()
    clock.tick(120)