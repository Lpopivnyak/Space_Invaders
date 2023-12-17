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

Rocket = rocket.Character(660, 598, 50, 100, 10, "rocket.png")

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

    pygame.display.flip()
    fps.tick(60)