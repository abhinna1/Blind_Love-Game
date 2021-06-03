import pygame as pg
import tilemap as t
import database
import settings as s
import sys

pg.init()
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
        return rect

    def Label(text, x, y, base_font=pg.font.Font(None, 30)):
        text_surface = base_font.render(text, True, (255, 0, 0))
        screen.blit(text_surface, (x, y))


    screen = pg.display.set_mode((1000, 600))
    pg.display.set_caption(s.title)
    bg = pg.image.load('png files/Menu bg.png')
    bg = pg.transform.scale(bg, (1000, 600))
    type_sound = pg.mixer.Sound('Sounds/type2.wav')
    click_sound = pg.mixer.Sound('Sounds/Type.wav')
    icon = pg.image.load('png files/Still Animation/Still Character Animation1.png')
    pg.display.set_icon(icon)


    def test_db():
        try:
            database.clear()
            print('Table Cleared')
            database.add(t1)
            print(f'{t1} has been added to the UserInfo Table')
            click_sound.play()
        except:
            print('Error Found')

            # m.main_Game()
    if len(database.show()) == 0:
        t1 = ''
    else:
        t1 = (database.show()[0])[0]
    run = True
    while run:
        screen.blit(bg, (0,0))
        menumap(screen)
        text_entry = Entry(t1, 300, 50)
        Label('Enter Name', 420, 100)
        b1 = button(screen, (350, 125), 'Start Game', 50)
        clear_btn = button(screen, (710, 55), 'Clear Text', 20)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if b1.collidepoint(pg.mouse.get_pos()):
                    test_db()

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
main_menu()

