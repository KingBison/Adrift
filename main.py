import pygame as pg
import gameObjects

pg.init()
# init pg data
WIDTH, HEIGHT = 1000, 800
pg.display.set_caption("Adrift")
fpsClock = pg.time.Clock()
# init objects
bg_img = pg.image.load("imgs/bg_img.jpeg")
# init window
window = pg.display.set_mode((WIDTH,HEIGHT))

# init game objects
ship = gameObjects.Ship(500,700,50,100)
asteroidField = gameObjects.AsteroidField()


def handleEvents():
    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            return False 
        ship.handleEvent(event)
    
    return True

def handleUpdates():
    ship.update(asteroidField)
    asteroidField.update()

    if ship.destroyed:
        return False
    else:
        return True

def handleRender():
    window.blit(bg_img, (0,0))
    asteroidField.render(window)
    ship.render(window)
    pg.display.flip()

def main():
    running = True
    while running:
        running = handleEvents()
        if not running:
            break
        running = handleUpdates()
        handleRender()
        fpsClock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main()