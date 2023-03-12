import pygame as pg

HEART = pg.image.load("imgs/heart.png")

pg.font.init()
FONT = pg.font.SysFont(None, 50)

def renderShipStats(ship, window):
    WIDTH = pg.display.get_surface().get_width()

    pg.draw.rect(window, "white", (WIDTH-150,0,150,50))
    pg.draw.rect(window, "white", (WIDTH-100,50,100,50))

    for i in range(ship.health):
        window.blit(HEART, (WIDTH-150 + 50*i, 0))

    img = FONT.render(str(ship.score), True, "black")
    window.blit(img, (WIDTH-90,60))
