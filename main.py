import pygame as pg
import sys

import settings as s
import tilemap as t
import collisions as c
import animations as a

pg.init()

# Loading Sounds
jump_sound = pg.mixer.Sound('Sounds/Jump.mp3')

def main_Game():
    screen = pg.display.set_mode((s.width, s.height))
    pg.display.set_caption(s.title)

    clock = pg.time.Clock()
    # Load images ():
    bg = pg.image.load('png files/background/sky.png').convert_alpha()
    bg = pg.transform.scale(bg, (1000, 600))

    player_img = pg.image.load('png files/Still Animation/Still Character Animation1.png').convert_alpha()
    player_rect = pg.Rect(50, 400, player_img.get_width() - 55, player_img.get_height() - 33)

    cloud1_img = pg.image.load('png files/background/clouds.png').convert_alpha()
    cloud1_img = pg.transform.scale(cloud1_img, (600, 600))

    # Surface to display images on to
    display = pg.Surface((300, 200))

    pg.display.set_icon(player_img)
    moving_right = False
    moving_left = False

    air_timer = 0
    score = 0

    def animation():
        animation_list = [pg.image.load('png files/Still Animation/Still Character Animation1.png'),
                          pg.image.load('png files/Still Animation/Still Character Animation2.png')]
        if moving_right:
            display.blit(a.char_still[1].convert_alpha(), (player_rect.x - 17 - s.scroll[0], player_rect.y - 16 - s.scroll[1]))
        if moving_left:
            display.blit(a.char_still[2].convert_alpha(), (player_rect.x - 17 - s.scroll[0], player_rect.y - 16 - s.scroll[1]))
        if (not moving_left) and (not moving_right):
            display.blit(a.char_still[0].convert_alpha(), (player_rect.x - 17 - s.scroll[0], player_rect.y - 16 - s.scroll[1]))

    # Score Bar
    running = True
    while running:
        display.blit(bg, (0, 0))  # Background
        # display.fill((0,0,0))

        if player_rect.x > ((t.tilemap[0])[0]) + 300:  # if player position is not near map edge move camera x position
            s.scroll[0] += (player_rect.x - s.scroll[0] - 340) / 10
        else:
            if (s.scroll >= [30, 0]) and (
                    player_rect.x <= (t.tilemap[0])[0]):  # if player position is near map edge move camera position
                s.scroll[0] = (s.scroll[0] + (350 / 10))
        s.scroll[1] += (player_rect.y - s.scroll[1] - 300) / 30  # Y- Camera movement - Always Enabled

        # Cloud Rendering
        display.blit(cloud1_img, (s.cloud1_pos[0] - s.scroll[0], s.cloud1_pos[1] - s.scroll[1]))
        s.cloud1_pos[0] += s.cloud_vel
        if s.cloud1_pos[0] >= 1200:
            s.cloud1_pos[0] = -600
        display.blit(cloud1_img, (s.cloud2_pos[0] - s.scroll[0], s.cloud2_pos[1] - s.scroll[1]))
        s.cloud2_pos[0] -= s.cloud_vel
        if s.cloud2_pos[0] <= -600:
            s.cloud2_pos[0] = 1200

        # Tile Map Rendering
        tile_rects = []
        heart_lst = []
        enemy_lst= []
        y = 0
        for row in t.tilemap:
            x = 0
            for tile in row:
                if tile == 1:
                    display.blit(t.dirt1_img.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    tile_rects.append(pg.Rect(x * 30, y * 30, 30, 30))
                if tile == 2:
                    display.blit(t.grass_img.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    tile_rects.append(pg.Rect(x * 30, y * 30, 30, 30))

                if tile == 3:
                    display.blit(t.dirt2_img.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    tile_rects.append(pg.Rect(x * 30, y * 30, 30, 30))
                if tile == 4:
                    display.blit(t.sushi.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    heart_rect = pg.Rect(x * 30 + 21, y * 30 + 30, 40, 40)
                    heart_lst.append(heart_rect)

                if tile == 5:

                    display.blit(t.enemy.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    enemy_rect = pg.Rect(x * 30, y * 30+10, 35, 45)
                    enemy_lst.append(enemy_rect)
                    # pg.draw.rect(display, (255,255,0), enemy_rect, 2)
                    # Uncomment the below line to see tile rects
                    # pg.draw.rect(display, (255, 0, 0), pg.Rect(x * 30, y * 30, 30, 30), 2)

                x += 1
            y += 1

        # Implementing Gravity
        player_movement = [0, 0]
        player_movement[1] += s.gravity * 2
        s.gravity += 0.4

        # Movement
        if moving_right:
            player_movement[0] += s.player_vel
        if moving_left and player_rect.x >= 5:
            player_movement[0] -= s.player_vel

        for lifes in heart_lst:
            if player_rect.colliderect(lifes):
                score += 1
                lifes.height = 0
                print(score)

        # Limiting gravity
        if s.gravity > 5:
            s.gravity = 5

        player_rect, collisions = c.move(player_rect, player_movement, tile_rects)

        if collisions['bottom']:
            s.gravity = 0
            air_timer = 0
        else:
            air_timer += 1
        # display.blit(player_img, (player_rect.x - 25 - s.scroll[0], player_rect.y - 16 - s.scroll[1]))

        animation()
        # Uncomment the below line to see the player rect
        # pg.draw.rect(display, (255, 0, 0), player_rect,2)

    # Enemy collision
        for enemy in enemy_lst:
            if player_rect.colliderect(enemy):
                if player_rect.bottom >= enemy.top:
                    print('kill')
                else:
                    print('ded')
        # Event Handling
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                sys.exit()

            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_d) or (event.key == pg.K_RIGHT):
                    moving_right = True
                if (event.key == pg.K_a) or (event.key == pg.K_LEFT):
                    moving_left = True
                if (event.key == pg.K_w) or (event.key == pg.K_UP):
                    if air_timer < 6:
                        jump_sound.play()
                        s.gravity -= 8

            if event.type == pg.KEYUP:
                if (event.key == pg.K_d) or (event.key == pg.K_RIGHT):
                    moving_right = False
                if (event.key == pg.K_a) or (event.key == pg.K_LEFT):
                    moving_left = False

        display = pg.transform.scale(display, (1000, 600))
        screen.blit(display, (0, 0))
        pg.display.update()
        clock.tick(60)

def menu():
    screen = pg.display.set_mode((1000, 600))
    running = True
    bg = pg.image.load('png files/background/sky.png')
    bg = pg.transform.scale(bg,(1000, 600))
    screen.blit(bg, (0,0))

    while running:
        # Tile Map Rendering
        tile_rects = []
        heart_lst = []
        enemy_lst = []
        y = 0
        for row in t.menu_map:
            x = 0
            for tile in row:
                if tile == 1:
                    screen.blit(t.dirt1_img.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    tile_rects.append(pg.Rect(x * 30, y * 30, 30, 30))
                if tile == 2:
                    screen.blit(t.grass_img.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    tile_rects.append(pg.Rect(x * 30, y * 30, 30, 30))

                if tile == 3:
                    screen.blit(t.dirt2_img.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    tile_rects.append(pg.Rect(x * 30, y * 30, 30, 30))
                if tile == 4:
                    screen.blit(t.sushi.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    heart_rect = pg.Rect(x * 30 + 21, y * 30 + 30, 40, 40)
                    heart_lst.append(heart_rect)

                if tile == 5:
                    screen.blit(t.enemy.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    enemy_rect = pg.Rect(x * 30, y * 30 + 10, 35, 45)
                    enemy_lst.append(enemy_rect)
                    # pg.draw.rect(display, (255,255,0), enemy_rect, 2)
                    # Uncomment the below line to see tile rects
                    # pg.draw.rect(display, (255, 0, 0), pg.Rect(x * 30, y * 30, 30, 30), 2)

                x += 1
            y += 1
        for i in range(0, 1):
            screen.blit(t.msg_lst[i], (250, 200))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                main_Game()
        pg.display.update()

def main():

    pg.mixer.music.play(-1)
    menu()

music = pg.mixer.music.load('Growtopia Update Song.mp3')
main()