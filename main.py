import pygame as pg

import settings as s
import tilemap as t
import collisions as c

pg.init()

screen = pg.display.set_mode((s.width, s.height))
pg.display.set_caption(s.title)


clock = pg.time.Clock()
# Load images ():
bg = pg.image.load('png files/background/sky.png').convert_alpha()
bg = pg.transform.scale(bg, (1000, 600))

player_img = pg.image.load('png files/Still Animation/Still Character Animation1.png').convert_alpha()
player_rect = pg.Rect(50, 400, player_img.get_width()-47, player_img.get_height()-33)

cloud1_img = pg.image.load('png files/background/clouds.png').convert_alpha()
cloud1_img = pg.transform.scale(cloud1_img, (600, 600))

# Surface to display images on to
display = pg.Surface((300, 200))

pg.display.set_icon(player_img)
moving_right = False
moving_left = False

air_timer = 0



running = True
while running:
    display.blit(bg, (0, 0)) # Background
    # display.fill((0,0,0))

    # Cloud Rendering
    display.blit(cloud1_img, s.cloud1_pos)
    s.cloud1_pos[0] += s.cloud_vel
    display.blit(cloud1_img, s.cloud2_pos)
    s.cloud2_pos[0] -= s.cloud_vel

    tile_rects = []
    y = 0
    for row in t.tilemap:
        x = 0
        for tile in row:
            if tile == 1:
                display.blit(t.soil_img.convert_alpha(), (x * 30, y * 30))
            if tile == 2:
                display.blit(t.grass_img.convert_alpha(), (x * 30, y * 30))
            if tile != 0:
                tile_rects.append(pg.Rect(x * 30, y * 30, 30, 30))

                # Uncomment the below line to see tile rects
                # pg.draw.rect(display, (255, 0, 0), pg.Rect(x * 30, y * 30, 30, 30), 2)
            x += 1
        y += 1


    player_movement = [0, 0]
    player_movement[1] += s.gravity
    s.gravity += 0.4
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2

    player_movement[1] += s.gravity

    if s.gravity > 3:
        s.gravity = 3

    player_rect, collisions = c.move(player_rect, player_movement, tile_rects)

    if collisions['bottom']:
        s.gravity = 0
        air_timer = 0
    else:
        air_timer += 1

    display.blit(player_img, (player_rect.x - 25, player_rect.y - 16))
    # Uncomment the below line to see the player rect
    # pg.draw.rect(display, (255, 0, 0), player_rect,2)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                moving_right = True
            if event.key == pg.K_a:
                moving_left = True
            if event.key ==pg.K_w:
                if air_timer < 6:
                    s.gravity -= 8

        if event.type == pg.KEYUP:
            if event.key == pg.K_d:
                moving_right = False
            if event.key == pg.K_a:
                moving_left = False


    display = pg.transform.scale(display, (1000,600))
    screen.blit (display, (0, 0))
    pg.display.update()
    clock.tick(60)
pg.quit()