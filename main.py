import pygame,sys
pygame.init()

screen=pygame.display.set_mode((500,500))
char_img=pygame.image.load('png files/Still Animation/Still Character Animation1.png')
player= pygame.Rect((100,60,40,60))
tiles=[pygame.Rect(100,200,100,100),pygame.Rect(200,300,100,100)]
ground=pygame.image.load('Tile Maps/Groud Tile.png')
soil=pygame.image.load('Tile Maps/soil.png')
def collision_test(rect,tiles):
    collisions=[]
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    return collisions

def move(rect,movement,tiles):
    rect.x+=movement[0]
    collisions=collision_test(rect,tiles)
    for tile in collisions:
        if movement[0]>0:
            rect.right=tile.left
        if movement[0]<0:
            rect.left=tile.right

    rect.y+=movement[1]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
        if movement[1] < 0:
            rect.top = tile.bottom
    return rect


up=False
down=False
left=False
right=False
#gameloop
run=True

tilemap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1]]
while run==True:
    screen.fill((255, 255, 255))
    tile_y = 0
    tile_rects=[]
    for row in tilemap:
        tile_x = 0
        for tile in row:
            if tile == 1:
                screen.blit(soil, (tile_x * 30, tile_y * 30))
            if tile == 2:
                screen.blit(ground, (tile_x * 30, tile_y * 30))
            if tile != 0:
                tile_rects.append(pygame.Rect(tile_x * 30, tile_y * 30, 50, 50))

                '''remove the "#" to see the tile rects'''
                # pygame.draw.rect(self.screen,(255,0,0),self.tile_rects[self.tile_x])

            tile_x += 1
        tile_y += 1


    movement=[0,0]


    if right == True:
        movement[0]+=1
    if left == True:
        movement[0]-=1
    if up == True:
        movement[1]-=3
    if down==True:
        movement[1]+=1

    movement[1]+=1


    player=move(player,movement,tiles)
    #pygame.draw.rect(screen,(255,255,255),player)
    screen.blit(char_img,(player.x-25,player.y-15))

    for tile in tiles:
        pygame.draw.rect(screen,(255,0,0),tile)

    for event in pygame.event.get():
        #exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #player movement
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_UP:
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
    pygame.display.update()
    (pygame.time.Clock()).tick(120)
