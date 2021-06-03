import pygame as pg
import tilemap as t
import database
import settings as s
import sys

pg.init()
def finish(score = 0):
    def button(screen, position, text, size):
        font = pg.font.SysFont("Cambria", size)
        text_render = font.render(text, True, (255, 0, 0))
        x, y, w, h = text_render.get_rect()
        x, y = position
        pg.draw.rect(screen, (120, 120, 200), (x - 5, y - 5, w + 10, h + 10))
        pg.draw.rect(screen, (140, 140, 200), (x, y, w, h))
        return screen.blit(text_render, (x, y))

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
    run = True
    msg = ''
    index = (database.show()[0])[0]
    s.cloud1_pos = [-100, -120]
    s.cloud2_pos = [400, -80]
    s.cloud3_pos = [1000, -130]
    s.cloud4_pos = [4000, -90]
    s.cloud_vel = 3
    print(f'The name stored in database is {index}')
    while run:
        screen.blit(bg, (0,0))

        msg = f'Congratulations, {index}!'
        Label(msg, 300, 80)
        Label(f'Your score is {score}', 380, 120)
        restart_btn = button(screen, (320, 150), 'Restart', 32)
        menu_btn = button(screen, (450, 150), 'Return To Menu', 30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if restart_btn.collidepoint(pg.mouse.get_pos()):
                    click_sound.play()
                    s.scroll[1] = 0
                    print('restart clicked')
                if menu_btn.collidepoint(pg.mouse.get_pos()):
                    click_sound.play()
                    print('Will return to Main Menu')
        pg.display.update()
    pg.quit()

finish(5)