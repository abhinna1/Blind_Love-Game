import pygame as pg
pg.init()

def button(screen, position, text, base_font=pg.font.SysFont("Arial", 50)):
    text_render = base_font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pg.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pg.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pg.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pg.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pg.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def Entry(screen, text, x, y, base_font=pg.font.Font(None, 30)):
    rect = pg.Rect((x, y, 400, 32))

    color = (255, 0, 0)
    pg.draw.rect(screen, color, rect, 2)
    text_surface = base_font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (rect.x + 5, rect.y + 5))


def Label(screen, text, x, y, base_font=pg.font.Font(None, 30)):
    text_surface = base_font.render(text, True, (255, 0, 0))
    screen.blit(text_surface, (x, y))
