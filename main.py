import pygame,sys

class game:

    def __init__(self,win_x,win_y):
        self.win_x=win_x
        self.win_y=win_y
        self.screen = pygame.display.set_mode((self.win_x, self.win_y))

        self.key=pygame.key.get_pressed()
        def get_Char(char_x,char_y,vel):
            self.char=pygame.image.load('png files/Still Animation/Still Character Animation1.png')
            self.screen.blit(self.char,(char_x,char_y))
        def sky(sky_x,sky_y):
            self.sky=pygame.image.load('png files/Sky.png')
            self.sky=pygame.transform.scale(self.sky,(1000,1000))
            self.screen.blit(self.sky,(sky_x,sky_y))
        def ground(ground_x,ground_y):
            self.ground=pygame.image.load('png files/Ground.png')
            self.screen.blit(self.ground,(ground_x,ground_y))
        def cloud(cloud1_x,cloud1_y,cloud2_x,cloud2_y):
            self.cloud1=pygame.image.load('png files/clouds.png')
            self.cloud2=pygame.image.load('png files/clouds.png')
            self.cloud1 = pygame.transform.scale(self.cloud1, (700, 600))
            self.cloud2 = pygame.transform.scale(self.cloud2, (700, 600))
            self.screen.blit(self.cloud1,(cloud1_x,cloud1_y))
            self.screen.blit(self.cloud2,(cloud2_x,cloud2_y))


    #GameLoop
        self.running=True
        while self.running==True:
            sky(0, -50)
            cloud(-200,-50,500,-50)
            ground(0,70)
            get_Char(50,470,5)

            for self.event in pygame.event.get():
                if self.event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
game(1000,600)
