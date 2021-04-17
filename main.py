import pygame,sys
pygame.init()#initializing pygame

screen=pygame.display.set_mode((1000,800))

ground=pygame.image.load('png files/Ground.png')
sky=pygame.transform.scale2x(pygame.image.load('png files/Sky.png'))
sky=pygame.transform.scale2x(sky)
character = pygame.transform.scale2x(pygame.image.load('png files/Still Animation/Still Character Animation1.png'))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
            sys.exit()
    screen.blit(sky,(-200,-20))
    screen.blit(character, (20, 485))
    screen.blit(ground,(0,-200))


    pygame.display.update()