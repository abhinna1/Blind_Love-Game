import pygame , sys

pygame.init()
clock=pygame.time.Clock()

cloud1_x = -200
cloud1_y = -100
cloud2_x = 800
cloud2_y = -50

char_sprite=0
char_x=0 #x position of character
char_y=467 #y position of character
char_velocity=10
walkcount=0


class game:
    def __init__(self,win_x,win_y):
        self.win_x=win_x
        self.win_y=win_y
        self.screen=pygame.display.set_mode((self.win_x,self.win_y))
        pygame.display.set_caption('Blind Love')
        self.moving = False

    def sky(self):
        self.sky_bg=pygame.image.load('png files/Sky.png').convert_alpha()
        self.sky_bg=pygame.transform.scale((self.sky_bg),(1000,1000))
        self.screen.blit(self.sky_bg,(0,0))
    def ground(self):
        self.ground_img=pygame.image.load('png files/Ground.png').convert_alpha()
        self.screen.blit(self.ground_img,(0,70))
    def heart(self,heart_x,heart_y):
        self.heart_rect=pygame.Rect(heart_x,heart_y,30,30)
        self.heart_img=pygame.image.load('png files/Heart Animation/Heart1.png')
        #self.heart_img=pygame.transform.scale2x(self.heart_img)
        self.screen.blit(self.heart_img,(heart_x,heart_y))

    def cloud_movement(self):
        global cloud1_x
        global cloud2_x
        cloud1_x += 1
        cloud2_x -= 1

        #cloudLoop
        if cloud1_x==1000:
            cloud1_x=-800
        if cloud2_x==-800:
            cloud2_x=1000
    def clouds(self):
        self.cloud1_img=pygame.image.load('png files/clouds.png').convert_alpha()
        self.cloud2_img=pygame.image.load('png files/clouds.png').convert_alpha()
        self.cloud1_img = pygame.transform.scale(self.cloud1_img, (700, 600))
        self.cloud2_img = pygame.transform.scale(self.cloud2_img, (700, 600))
        self.screen.blit(self.cloud1_img,(cloud1_x,cloud1_y))
        self.screen.blit(self.cloud2_img,(cloud2_x,cloud2_y))
        game_instance.cloud_movement()

    def character(self):#load in character frames
        self.char_rect=pygame.Rect(char_x,char_y,30,30)
        self.key=pygame.key.get_pressed()
        self.char_list=[pygame.image.load('png files/Still Animation/Still Character Animation1.png').convert_alpha(),pygame.image.load('png files/Still Animation/Still Character Animation2.png').convert_alpha()]
    def character_anim(self):#character animations
        global walkcount

        if self.moving==False: #boolean self.moving is defined in th __init__ function
            self.char_out=self.screen.blit(self.char_list[walkcount],(char_x,char_y))
            walkcount+=1
        pygame.display.update()
    def char_movement(self):
        global char_x
        global char_y
        global walkcount
        self.key=pygame.key.get_pressed()
        if self.moving==False:
            if walkcount>=2:
                walkcount=0
        #right movement
        if (self.key[pygame.K_d]or self.key[pygame.K_RIGHT]) and char_x<930:
            self.moving=False
            char_x+=char_velocity

        #Left movement
        if (self.key[pygame.K_a]or self.key[pygame.K_LEFT])and char_x>-25:
            char_x-=char_velocity
        #Jump
        if self.key[pygame.K_w]or self.key[pygame.K_UP]:
            pass
    def heart_collide(self):
        if self.char_rect==self.heart_rect:
            print('hi')

#gameloop
run=True
while run:
    game_instance=game(1000, 600)

    game_instance.sky()#sky background
    game_instance.ground()#ground
    game_instance.clouds()#clouds

    #All character Functions are here
    game_instance.character()
    game_instance.char_movement()
    game_instance.character_anim()

    
    game_instance.heart(200,450)
    game_instance.heart_collide()





    for event in pygame.event.get():
        if event.type==pygame.QUIT or game_instance.key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    pygame.display.flip()
    clock.tick(120)
