import pygame as pg
import sys
import database

import settings as s
import tilemap as t
import collisions as c
import animations as a
from tkinter import *

pg.init()



def main_Game():
    def animation():
        animation_list = [pg.image.load('png files/Still Animation/Still Character Animation1.png'),
                          pg.image.load('png files/Still Animation/Still Character Animation2.png')]
        if moving_right:
            display.blit(a.char_still[1].convert_alpha(), (player_rect.x - 17 - s.scroll[0], player_rect.y - 16 - s.scroll[1]))
        if moving_left:
            display.blit(a.char_still[2].convert_alpha(), (player_rect.x - 17 - s.scroll[0], player_rect.y - 16 - s.scroll[1]))
        if (not moving_left) and (not moving_right):
            display.blit(a.char_still[0].convert_alpha(), (player_rect.x - 17 - s.scroll[0], player_rect.y - 16 - s.scroll[1]))

    def button(screen, position, text, size):
        font = pg.font.SysFont("Cambria", size)
        text_render = font.render(text, True, (255, 0, 0))
        x, y, w, h = text_render.get_rect()
        x, y = position
        pg.draw.rect(screen, (120, 120, 220), (x - 5, y - 5, w + 10, h + 10))
        pg.draw.rect(screen, (100, 100, 200), (x, y, w, h))
        return screen.blit(text_render, (x, y))


    def Label(screen, text, x, y, color, base_font=pg.font.Font(None, 30)):
        text_surface = base_font.render(text, True, color)
        screen.blit(text_surface, (x, y))

    def clouds():
        # Cloud Rendering
        display.blit(cloud1_img, (s.cloud1_pos[0] - s.scroll[0], s.cloud1_pos[1] - s.scroll[1]))
        s.cloud1_pos[0] += s.cloud_vel
        if s.cloud1_pos[0] >= 1200:
            s.cloud1_pos[0] = -600
        display.blit(cloud1_img, (s.cloud2_pos[0] - s.scroll[0], s.cloud2_pos[1] - s.scroll[1]))
        s.cloud2_pos[0] -= s.cloud_vel
        if s.cloud2_pos[0] <= -600:
            s.cloud2_pos[0] = 1200

    def tilemap():
        nonlocal air_timer, player_rect, score, collected
        # Tile Map Rendering
        tile_rects = []
        heart_lst = []
        enemy_lst = []
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
                    sushi_rect = pg.Rect(x * 30, y * 30, 30, 30)
                    heart_lst.append(sushi_rect)
                    # pg.draw.rect(display, (255,0,0), sushi_rect, 2)

                if (tile == 4) and collected == False:
                    # display.blit(display, ((x * 30 - s.scroll[0], y * 30 - s.scroll[1])))
                    sushi_img = (display.blit(t.sushi.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1])))
                    h1 = pg.Rect(x * 30 + 21, y * 30 + 30, 40, 40)
                    if player_rect.colliderect(h1):
                        collect_sound.play()
                        h1.x = 0
                        score += 1
                        collected = True
                if (tile == 8) and t.collected2 == False:
                    # display.blit(display, ((x * 30 - s.scroll[0], y * 30 - s.scroll[1])))
                    sushi_img = (display.blit(t.sushi.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1])))
                    h2 = pg.Rect(x * 30 + 21, y * 30 + 30, 40, 40)
                    if player_rect.colliderect(h2):
                        collect_sound.play()
                        h2.x = 0
                        score += 1
                        t.collected2 = True
                if (tile == 9) and t.collected9 == False:
                    sushi_img = (display.blit(t.sushi.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1])))
                    h9 = pg.Rect(x * 30 + 21, y * 30 + 30, 40, 40)
                    if player_rect.colliderect(h9):
                        collect_sound.play()
                        h9.x = 0
                        score += 1
                        t.collected9 = True

                if (tile == 10) and t.collected10 == False:
                    sushi_img = (display.blit(t.sushi.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1])))
                    h10 = pg.Rect(x * 30 + 21, y * 30 + 30, 40, 40)
                    if player_rect.colliderect(h10):
                        collect_sound.play()
                        h10.x = 0
                        score += 1
                        t.collected10 = True

                if (tile == 11) and t.collected11 == False:
                    sushi_img = (display.blit(t.sushi.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1])))
                    h11 = pg.Rect(x * 30 + 21, y * 30 + 30, 40, 40)
                    if player_rect.colliderect(h11):
                        collect_sound.play()
                        h11.x = 0
                        score += 1
                        t.collected11 = True

                if tile == 5:
                    display.blit(t.enemy.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    enemy_rect = pg.Rect(x * 30, y * 30 + 10, 35, 45)
                    enemy_lst.append(enemy_rect)
                    if player_rect.colliderect(enemy_rect):
                        fly_sound.play()
                        s.gravity -= 1

                    # pg.draw.rect(display, (255,255,0), enemy_rect, 2)
                    # Uncomment the below line to see tile rects
                    # pg.draw.rect(display, (255, 0, 0), pg.Rect(x * 30, y * 30, 30, 30), 2)
                if tile == 6:
                    display.blit(t.sand_img.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    tile_rects.append(pg.Rect(x * 30, y * 30, 30, 30))
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

    def widgets():
        global mute_rect, respawn_btn
        # audio buttons
        display.blit(sound_img, (930, 5))
        mute_rect = pg.Rect(930, 5, 50, 50)
        # pg.draw.rect(display, (255,0,0), mute_rect, 2)

        # Name Display:
        Label(display, f"{(database.show()[0])[0]}'s Score: {score}", 0, 0, (255, 0, 0))
        respawn_btn = button(display, (820, 15), 'Respawn', 20)

    def load_sounds():
        global jump_sound, fly_sound, sound_img, collect_sound
        # Loading Sounds
        jump_sound = pg.mixer.Sound('Sounds/Jump.mp3')
        fly_sound = pg.mixer.Sound('Sounds/Fly.wav')
        sound_img = pg.image.load('png files/Sound Img.png')
        sound_img = pg.transform.scale(sound_img, (50, 50))
        collect_sound = pg.mixer.Sound('Sounds/coin_collected.wav')

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

    air_timer = 0  # Jump Time
    score = 0  # Initializing score

    collected = False
    running = True
    load_sounds()
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
        clouds()

        tilemap()

        animation()

        widgets()

        # Uncomment the below line to see the player rect
        # pg.draw.rect(display, (255, 0, 0), player_rect,2)

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
            if event.type == pg.MOUSEBUTTONDOWN:
                if mute_rect.collidepoint(pg.mouse.get_pos()):
                    if pg.mixer.music.get_volume() <= 0.9921875:
                        pg.mixer.music.set_volume(1)
                    else:
                        pg.mixer.music.set_volume(0)

                if respawn_btn.collidepoint(pg.mouse.get_pos()):
                    player_rect.x, player_rect.y = 10, 420
                    s.scroll[0] = 0
                    score = 0
                    collected = False
                    t.collected2= False
                    t.collected9 = False
                    collected10 = False
                    collected11 = False

        display = pg.transform.scale(display, (1000, 600))
        screen.blit(display, (0, 0))
        pg.display.update()
        clock.tick(60)


def main_menu():
    def menumap(display):
        # Tile Map Rendering
        tile_rects = []
        heart_lst = []
        enemy_lst = []
        y = 0
        for row in t.menu_map:
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
                    sushi_rect = pg.Rect(x * 30, y * 30, 30, 30)
                    heart_lst.append(sushi_rect)
                    # pg.draw.rect(display, (255,0,0), sushi_rect, 2)

                if (tile == 4):
                    # display.blit(display, ((x * 30 - s.scroll[0], y * 30 - s.scroll[1])))
                    sushi_img = display.blit(t.sushi.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    heart_rect = pg.Rect(x * 30 + 21, y * 30 + 30, 40, 40)
                    heart_lst.append(heart_rect)

                if tile == 5:
                    display.blit(t.enemy.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    enemy_rect = pg.Rect(x * 30, y * 30 + 10, 35, 45)
                    enemy_lst.append(enemy_rect)

                    # pg.draw.rect(display, (255,255,0), enemy_rect, 2)
                    # Uncomment the below line to see tile rects
                    # pg.draw.rect(display, (255, 0, 0), pg.Rect(x * 30, y * 30, 30, 30), 2)
                if tile == 6:
                    display.blit(t.sand_img.convert_alpha(), (x * 30 - s.scroll[0], y * 30 - s.scroll[1]))
                    tile_rects.append(pg.Rect(x * 30, y * 30, 30, 30))
                x += 1
            y += 1

    def button(screen, position, text, size):
        font = pg.font.SysFont("Cambria", size)
        text_render = font.render(text, True, (255, 0, 0))
        x, y, w, h = text_render.get_rect()
        x, y = position
        pg.draw.rect(screen, (120, 120, 200), (x - 5, y - 5, w + 10, h + 10))
        pg.draw.rect(screen, (140, 140, 200), (x, y, w, h))
        return screen.blit(text_render, (x, y))

    def Entry(text, x, y, base_font=pg.font.Font(None, 30)):
        rect = pg.Rect((x, y, 400, 32))
        color = (255, 0, 0)
        pg.draw.rect(screen, color, rect, 2)
        text_surface = base_font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (rect.x + 5, rect.y + 5))

    def Label(text, x, y, base_font=pg.font.Font(None, 30)):
        text_surface = base_font.render(text, True, (255, 0, 0))
        screen.blit(text_surface, (x, y))


    screen = pg.display.set_mode((1000, 600))
    pg.display.set_caption(s.title)
    pg.display.set_icon(pg.image.load('png files/Still Animation/Still Character Animation1.png'))
    bg = pg.image.load('png files/background/sky.png')
    bg = pg.transform.scale(bg, (1000, 600))
    type_sound = pg.mixer.Sound('Sounds/type2.wav')
    click_sound = pg.mixer.Sound('Sounds/Type.wav')

    if len(database.show()) == 0:
        t1 = ''
    else:
        t1 = (database.show()[0])[0]
    run = True
    while run:
        screen.blit(bg, (0,0))
        menumap(screen)
        Entry(t1, 300, 250)
        Label('Enter Name', 420, 310)
        b1 = button(screen, (350, 350), 'Start Game', 50)
        clear_btn = button(screen, (710, 255), 'Clear Text', 20)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if b1.collidepoint(pg.mouse.get_pos()):
                    database.clear()
                    database.add(t1)
                    click_sound.play()
                    main_Game()

                if clear_btn.collidepoint(pg.mouse.get_pos()):
                    t1 = ''
                    type_sound.play()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    type_sound.play()
                    t1 = t1[0:-1]
                else:
                    type_sound.play()
                    t1 += event.unicode
        pg.display.update()
    pg.quit()


def main():

    pg.mixer.music.play(-1)
    main_menu()

music = pg.mixer.music.load('Sounds/Music.mp3')
main()