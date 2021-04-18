import pygame , sys

pygame.init()
clock=pygame.time.Clock()

cloud1_x = -200
cloud1_y = -100
cloud2_x = 800
cloud2_y = -50

char_x=0 #x position of character
char_y=467 #y position of character
char_velocity=5
class game:
    def __init__(self,win_x,win_y):
        self.win_x=win_x
        self.win_y=win_y
        self.screen=pygame.display.set_mode((self.win_x,self.win_y))


    def sky(self):
        self.sky_bg=pygame.image.load('png files/Sky.png').convert_alpha()
        self.sky_bg=pygame.transform.scale((self.sky_bg),(1000,1000))
        self.screen.blit(self.sky_bg,(0,0))

    def ground(self):
        self.ground_img=pygame.image.load('png files/Ground.png').convert_alpha()
        self.screen.blit(self.ground_img,(0,70))

    def heart(self):
        self.heart_img=pygame.image.load('png files/Heart Animation/Heart1.png')
        self.heart_img=pygame.transform.scale2x(self.heart_img)
        self.screen.blit(self.heart_img,(200,460))


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


    def character(self):

        self.char_list=[]
        self.char_list.append(pygame.image.load('png files/Still Animation/Still Character Animation1.png').convert_alpha())
        self.char_list.append(pygame.image.load('png files/Still Animation/Still Character Animation2.png').convert_alpha())
        self.char_sprite=0
        self.screen.blit(self.char_list[self.char_sprite],(char_x,char_y))
    def char_movement(self):
        global char_x
        global char_y
        self.key=pygame.key.get_pressed()
        if self.key[pygame.K_d]:
            char_x+=char_velocity
        if self.key[pygame.K_a]:
            char_x-=char_velocity
        if self.key[pygame.K_w]:
            pass
        if self.key[pygame.K_s]:
            pass

    def update(self):
        self.char_sprite=self.char_sprite+1
        if self.char_sprite>len(self.char_list):
            self.char_sprite = 0



run=True
while run:
    game_instance=game(1000, 600)
    game_instance.sky()
    game_instance.ground()
    game_instance.character()
    game_instance.char_movement()
    game_instance.heart()
    game_instance.clouds()

    game_instance.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
