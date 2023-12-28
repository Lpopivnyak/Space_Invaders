import pygame

import rocket
import ufo

pygame.init()
window = pygame.display.set_mode((1370, 705))
fps = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play(-1)

backgroundImage = pygame.image.load("galaxy.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (1370, 705))

Rocket = rocket.Character(660, 598, 70, 100, 10, "rocket.png")
Ufo = []
Ufo.append(ufo.Enemy(30, 20, 100, 80, 10, "ufo.png"))
Ufo.append(ufo.Enemy(150, 20, 100, 80, 10, "ufo.png"))

game = True
while game:
    #обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    #оновлення
    Rocket.movement()

    #рендер
    window.fill((0, 0, 0))
    window.blit(backgroundImage, (0, 0))

    Rocket.Render((window))
    for ufo in Ufo:

        ufo.Render(window)

    pygame.display.flip()
    fps.tick(60)