import pygame as pg
import random, math
import asteroidHelpers, miscHelpers, shipHelpers

class Ship:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.right_vel = 0
        self.left_vel = 0 
        self.spdFactor = 10
        self.w = w
        self.h = h
        self.texture = pg.image.load("imgs/ship.png")
        self.bullets = Bullets()
        self.health = 3
        self.destroyed = False
        self.score = 0

    def render(self, window):
        window.blit(self.texture, (self.x,self.y))
        self.bullets.render(window)
        shipHelpers.renderShipStats(self, window)

    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                self.left_vel-=self.spdFactor
            if event.key == pg.K_RIGHT:
                self.right_vel+=self.spdFactor
            if event.key == pg.K_SPACE:
                self.bullets.shoot(self.x, self.y)
        
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                self.left_vel=0
            if event.key == pg.K_RIGHT:
                self.right_vel=0


    def update(self, asteroidField):
        ttm = self.x + self.right_vel + self.left_vel

        if ttm < 0:
            self.x = 0
        elif ttm > 950:
            self.x = 950
        else :
            self.x+=self.right_vel + self.left_vel

        for asteroid in asteroidField.asteroids:
            if miscHelpers.collisionDetection(self.x, self.y, self.texture.get_width(), self.texture.get_height(),
                                    asteroid.x, asteroid.y, asteroid.texture.get_width(), asteroid.texture.get_height()):
                self.health -= 1
                asteroidField.asteroids.remove(asteroid)

        if self.health < 1:
            self.destroyed = True

        self.bullets.update(asteroidField, self)


class Bullets:
    def __init__(self):
        self.bullets = []

    def render(self, window):
        for bullet in self.bullets:
            bullet.render(window)

    def update(self, asteroidField, ship):

        outBullets = []
        for bullet in self.bullets:
            bullet.update()
            if bullet.y < 0:
                outBullets.append(bullet)
            else:
                hit = False
                outAsteroids = []
                for asteroid in asteroidField.asteroids:
                    if not miscHelpers.collisionDetection(asteroid.x, asteroid.y, asteroid.texture.get_width(), asteroid.texture.get_height(),bullet.x,bullet.y,3,5):
                        outAsteroids.append(asteroid)
                    else:
                        hit = True
                        ship.score += asteroid.points
                if not hit:
                    outBullets.append(bullet)

                asteroidField.asteroids = outAsteroids
            
        self.bullets = outBullets

    def shoot(self, x, y):
        self.bullets.append(Bullet(x+25, y+50))


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def render(self, window):
        pg.draw.rect(window, "red", (self.x,self.y,3,5))

    def update(self):
        self.y -= self.speed



class AsteroidField:
    def __init__(self):
        self.asteroidCap = 15
        self.asteroids = []
        setAsteroids(self.asteroids, self.asteroidCap)

    def render(self, window):
        for asteroid in self.asteroids:
            asteroid.render(window)

    def update(self):

        updatedAsteroids = []
        for asteroid in self.asteroids:
            if asteroid.y < 800:
                asteroid.y += asteroid.speed
                updatedAsteroids.append(asteroid)
        self.asteroids = updatedAsteroids



        if len(self.asteroids) != self.asteroidCap:
            setAsteroids(self.asteroids, self.asteroidCap)

def setAsteroids(asteroids, cap):
    while len(asteroids) < cap:
        newAsteroid = Asteroid(asteroidHelpers.getAsteroidColor())
        found = False
        for existingAsteroid in asteroids:
            if abs(existingAsteroid.x- newAsteroid.x) < 100 and abs(existingAsteroid.y- newAsteroid.y) < 100:
                found = True
        if not found:
            asteroids.append(newAsteroid)
    return asteroids        

class Asteroid:
    def __init__(self, color):
        self.x = random.randint(0,900)
        self.y = random.randint(-1000,-100)
        self.color = color
        if color == "ice":
            self.texture = pg.image.load("imgs/Asteroid_Ice.png")
            self.speed = 1
            self.points = 1
        if color == "red":
            self.texture = pg.image.load("imgs/Asteroid_Red.png")
            self.speed = 5
            self.points = 3
        if color == "gray":
            self.texture = pg.image.load("imgs/Asteroid_1.png")
            self.speed = 2
            self.points = 1

        rotate = random.randint(0,3)
        self.texture = pg.transform.rotate(self.texture, rotate*90)

    def render(self, window): 
        window.blit(self.texture, (self.x,self.y))

    def update(self):
        pass
        

