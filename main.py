import pygame

import rocket
import ufo
import asteroid

pygame.init()
window = pygame.display.set_mode((1370, 705))
fps = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play(-1)

backgroundImage = pygame.image.load("galaxy.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (1370, 705))

Rocket = rocket.Character(660, 598, 70, 100, 10, "rocket.png")
Enemies = []
Enemies.append(ufo.Enemy(30, 20, 100, 60, 10, "ufo.png"))
Enemies.append(asteroid.Enemy(150, 20, 80, 60, 10, "asteroid.png"))
Enemies.append(ufo.Enemy(250, 20, 100, 60, 10, "ufo.png"))
Enemies.append(asteroid.Enemy(370, 20, 80, 60, 10, "asteroid.png"))
Enemies.append(ufo.Enemy(470, 20, 100, 60, 10, "ufo.png"))
Enemies.append(asteroid.Enemy(590, 20, 80, 60, 10, "asteroid.png"))
Enemies.append(ufo.Enemy(690, 20, 100, 60, 10, "ufo.png"))
Enemies.append(asteroid.Enemy(810, 20, 80, 60, 10, "asteroid.png"))
Enemies.append(ufo.Enemy(910, 20, 100, 60, 10, "ufo.png"))
Enemies.append(asteroid.Enemy(1030, 20, 80, 60, 10, "asteroid.png"))
Enemies.append(ufo.Enemy(1130, 20, 100, 60, 10, "ufo.png"))
Enemies.append(asteroid.Enemy(1250, 20, 80, 60, 10, "asteroid.png"))


game = True
while game:
    #обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    #оновлення
    Rocket.movement()
    for ufo in Enemies:
        ufo.movement()

    #рендер
    window.fill((0, 0, 0))
    window.blit(backgroundImage, (0, 0))

    Rocket.Render((window))
    for ufo in Enemies:
        ufo.Render(window)


    pygame.display.flip()
    fps.tick(60)