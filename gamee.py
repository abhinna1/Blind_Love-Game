import pygame,sys
pygame.init()

char_position = [0, 0]  # x and y axis
left=False
right=False
up=False
down=False
char_rect=pygame.Rect(0,0,40,60)
class game:
    def __init__(self,screen_x,screen_y):
        self.screen_x=screen_x
        self.screen_y=screen_y
        self.screen=pygame.display.set_mode((self.screen_x,self.screen_y))
        self.screen.fill((135,206,235))

    def images(self):
        self.char=pygame.image.load('png files/Still Animation/Still Character Animation1.png')
        self.char_rect=pygame.Rect(20,20,20,20)

        self.ground=pygame.image.load('Tile Maps/Groud Tile.png')
        self.soil=pygame.image.load('Tile Maps/soil.png')

    def tile_map(self):
        self.tile_y=0
        self.tile_rects=[]
        self.tilemap=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
        for self.row in self.tilemap:
            self.tile_x=0
            for self.tile in self.row:
                if self.tile==1:
                    self.screen.blit(self.soil,(self.tile_x*30,self.tile_y*30))
                if self.tile == 2:
                    self.screen.blit(self.ground, (self.tile_x * 30, self.tile_y * 30))
                if self.tile!=0:
                    self.tile_rects.append(pygame.Rect(self.tile_x *30, self.tile_y *30, 50, 50))

                    '''remove the "#" to see the tile rects'''
                    pygame.draw.rect(self.screen,(255,0,0),self.tile_rects[self.tile_x])


                self.tile_x+=1
            self.tile_y+=1

    def check_collision(self,rect,tiles):
        collisions = []
        for tile in tiles:
            if rect.colliderect(tile):
                collisions.append(tile)
        return collisions

    def move_char(self,rect,movement_value,tiles):
        rect.x+=movement_value[0]
        collisions = game_instance.check_collision(rect,tiles)
        for tile in collisions:
            if movement_value[0]>0:
                rect.right = tile.left
            if movement_value[0]<0:
                rect.left = tile.right

        rect.y=movement_value[1]
        collisions = game_instance.check_collision(rect, tiles)
        for tile in collisions:
            if movement_value[1] > 0:
                rect.bottom = tile.top
            if movement_value[1] < 0:
                rect.top = tile.bottom
        return rect
    def load_char(self):
        global up
        global down
        global left
        global right
        global char_position
        global char_rect

        self.char_velocity=2

        if right == True:
            char_position[0] += self.char_velocity
        if left == True:
            char_position[0] -= self.char_velocity
        if up == True:
            char_position[1] -= self.char_velocity
        if down == True:
            char_position[1] += self.char_velocity
        char_position[1]+=1

        char_rect= pygame.Rect((100,60,40,60))

        char_rect=game_instance.move_char(self.char_rect,char_position,self.tile_rects)
        pygame.draw.rect(self.screen,(255,0,0),self.char_rect)
        self.screen.blit(self.char,(self.char_rect.x,self.char_rect.y))



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key ==pygame.K_UP:
                up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_UP:
                up = False



run=True
while run == True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_instance = game(1000, 600)

    game_instance.images()
    game_instance.tile_map()
    game_instance.load_char()
    pygame.display.update()


