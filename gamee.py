import pygame, sys


pygame.init()
window_size=(990,600)
clock = pygame.time.Clock()


cloud1_x = -200
cloud1_y = -100
cloud2_x = 800
cloud2_y = -50

char_sprite = 0
char_x = 0  # x position of character
char_y = 465  # y position of character
char_velocity = 10
left=False
right=False
jump=False
walkcount = 0
runcount=0
game_map=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

class game:
    def __init__(self, win_x, win_y):
        self.win_x = win_x
        self.win_y = win_y
        self.screen = pygame.display.set_mode((self.win_x, self.win_y))
        pygame.display.set_caption('Blind Love')
        self.moving = False

    def map(self):
        self.grass = pygame.image.load('Tile Maps/Groud Tile.png').convert_alpha()
        self.tile_size=self.grass.get_width()
        self.dirt = pygame.image.load('Tile Maps/soil.png').convert_alpha()
        self.tile_rects=[]
        self.y = 0
        for row in game_map:
            self.x = 0
            for tile in row:
                if tile == 1:
                    self.screen.blit(self.dirt, (self.x * 30, self.y * 30))
                if tile == 2:
                    self.screen.blit(self.grass, (self.x * 30, self.y * 30))
                if tile != 0:
                    self.tile_rects.append(pygame.Rect(self.x * self.tile_size, self.y * self.tile_size, self.tile_size, self.tile_size))
                self.x += 1
            self.y += 1
    def sky(self):
        self.sky_bg = pygame.image.load('png files/Sky.png').convert_alpha()
        self.sky_bg = pygame.transform.scale((self.sky_bg), (1000, 1000))
        self.screen.blit(self.sky_bg, (0, 0))

    def clouds(self):
        global cloud1_x
        global cloud2_x

        self.cloud_velocity=1
        self.cloud1_img = pygame.image.load('png files/clouds.png').convert_alpha()
        self.cloud2_img = pygame.image.load('png files/clouds.png').convert_alpha()
        self.cloud1_img = pygame.transform.scale(self.cloud1_img, (700, 600))
        self.cloud2_img = pygame.transform.scale(self.cloud2_img, (700, 600))
        self.screen.blit(self.cloud1_img, (cloud1_x, cloud1_y))
        self.screen.blit(self.cloud2_img, (cloud2_x, cloud2_y))
        # game_instance.cloud_movement()

        cloud1_x += self.cloud_velocity
        cloud2_x -= self.cloud_velocity

        # cloudLoop
        if cloud1_x == 1000:
            cloud1_x = -800
        if cloud2_x == -800:
            cloud2_x = 1000


    def heart(self, heart_x, heart_y):
        self.heart_img = pygame.image.load('png files/Heart Animation/Heart1.png')
        self.heart_rect = pygame.Rect(heart_x, heart_y, 30, 30)
        self.screen.blit(self.heart_img, (heart_x, heart_y))

        if self.char_rect.colliderect(self.heart_rect):  # collision detection with heart
            pass


    def character(self):  # load in character frames

        global char_y
        self.player_y_momentum = 5

        self.char_list = [pygame.image.load('png files/Still Animation/Still Character Animation1.png').convert_alpha(),
                          pygame.image.load('png files/Still Animation/Still Character Animation2.png').convert_alpha()]
        self.char_width=self.char_list[0].get_width()
        self.char_height=self.char_list[0].get_height()
        self.char_rect = pygame.Rect(char_x, char_y, self.char_width, self.char_height)

        def char_collide():
            for self.objects in self.tile_rects:
                if self.char_rect.colliderect(self.objects):
                    char_x=0

        #gravity
        if char_y > window_size[1] - self.char_list[0].get_height():
            char_y = - self.player_y_momentum
        else:
            char_y += self.player_y_momentum
        char_collide()

    def character_anim(self):  # character still animations
        global walkcount
        if self.moving == False:  # boolean self.moving is defined in th __init__ function
            self.char_out = self.screen.blit(self.char_list[walkcount], (char_x, char_y))
            walkcount += 1
        #jumpAnim


    def moving_anim(self):#running animation script
        self.key = pygame.key.get_pressed()
        global walkcount
        self.moving_list=[pygame.image.load('png files/Walking animations/Walking right1.png').convert_alpha(),
                          pygame.image.load('png files/Walking animations/Walking right2.png').convert_alpha(),
                          pygame.image.load('png files/Walking animations/Walking right3.png').convert_alpha(),
                          pygame.image.load('png files/Walking animations/Walking right4.png').convert_alpha()]
        if self.moving==True:
            # self.char_out=self.screen.blit(self.moving_list[walkcount],(char_x,char_y))
            # walkcount+=1
            pass

    def char_movement(self):#movement script
        global char_x
        global char_y
        global walkcount
        global jump
        self.key = pygame.key.get_pressed()
        if self.moving == False:
            if walkcount >= 2:
                walkcount = 0

        # right movement
        if (self.key[pygame.K_d] or self.key[pygame.K_RIGHT]) and char_x < 930:
            self.moving = True
            char_x += char_velocity

        # Left movement
        if (self.key[pygame.K_a] or self.key[pygame.K_LEFT]) and char_x > -25:
            self.moving=True
            char_x -= char_velocity
        # Jump
        if jump==True:
            char_y-=20
            jump=False
        if self.key[pygame.K_w] or self.key[pygame.K_UP]:
            jump=True


# gameloop
run = True
while run:
    game_instance = game(window_size[0],window_size[1])


    game_instance.sky()  # sky background
    game_instance.clouds()  # clouds
    game_instance.map()
    # All character Functions are here
    game_instance.character()
    game_instance.character_anim()
    game_instance.moving_anim()
    game_instance.char_movement()




    game_instance.heart(200, 460)
    game_instance.heart(500, 460)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or game_instance.key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    pygame.display.flip()
    clock.tick(120)