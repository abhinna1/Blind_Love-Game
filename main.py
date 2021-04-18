import pygame,sys

#Character position Data
character_x=0
character_y=443
character_velocity=5

#Clouds Position Data
cloud1_x=-200
cloud1_y=-100
cloud2_x=500
cloud2_y=-50

class game:

    def __init__(self,win_x,win_y):
        self.win_x=win_x
        self.win_y=win_y
        self.screen = pygame.display.set_mode((self.win_x, self.win_y))
        self.clock=pygame.time.Clock()

        def heart(heart_x,heart_y):
            self.heart_img=pygame.image.load('png files/Heart Animation/Heart1.png')

        def get_Char(char_x,char_y,vel):
            self.char_x=char_x
            self.char_y=char_y
            self.vel=vel
            self.char=pygame.transform.scale(pygame.image.load('png files/Still Animation/Still Character Animation1.png'),(120,120))
            self.screen.blit(self.char,(self.char_x,self.char_y))

        def sill_anim():
            self.char_sprite=[pygame.image.load('png files/Still Animation/Still Character Animation1.png'),pygame.image.load('png files/Still Animation/Still Character Animation2.png')]
            self.charSprite_count=0
            self.screen.blit(self.char(character_x,character_y)
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

        #Character Movement Script
        def char_movement():
            global character_x
            if self.key[pygame.K_d]:
                character_x+=5
            if self.key[pygame.K_a]:
                character_x-=5

        def cloud_movement():
            global cloud1_x,cloud2_x
            cloud1_x+=1
            cloud2_x-=1
            if cloud1_x==1000:
                cloud1_x=-800
            if cloud2_x==-800:
                cloud2_x=1000


    #GameLoop
        self.running=True
        while self.running==True:
            global character_x
            self.key = pygame.key.get_pressed()
            sky(0, -50)
            cloud(cloud1_x ,cloud1_y,cloud2_x,cloud2_y)
            cloud_movement()
            ground(0,70)

            #character loading and movement script
            get_Char(character_x,character_y,character_velocity)
            char_movement()


            for self.event in pygame.event.get():
                if self.event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)


game(1000,600)
