import pygame

import json

import rocket
import ufo
import asteroid

def start_game():
    def read_data():
        global settings
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    read_data()

    def write_data():
        global settings
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)

    window = pygame.display.set_mode((1600, 845))
    fps = pygame.time.Clock()

    pygame.mixer.init()
    pygame.mixer.music.load("space.ogg")
    pygame.mixer.music.play(-1)

    backgroundImage = pygame.image.load("galaxy.jpg")
    backgroundImage = pygame.transform.scale(backgroundImage, (1600, 845))

    Rocket = rocket.Character(660, 650, 70, 100, 10, "rocket.png")
    Enemies = []
    Enemies.append(ufo.Enemy(30, 20, 100, 60, 5, "ufo.png"))
    Enemies.append(asteroid.Enemy(150, 20, 80, 60, 5, "asteroid.png"))
    Enemies.append(ufo.Enemy(250, 20, 100, 60, 5, "ufo.png"))
    Enemies.append(asteroid.Enemy(370, 20, 80, 60, 5, "asteroid.png"))
    Enemies.append(ufo.Enemy(470, 20, 100, 60, 5, "ufo.png"))
    Enemies.append(asteroid.Enemy(590, 20, 80, 60, 5, "asteroid.png"))
    Enemies.append(ufo.Enemy(690, 20, 100, 60, 5, "ufo.png"))
    Enemies.append(asteroid.Enemy(810, 20, 80, 60, 5, "asteroid.png"))
    Enemies.append(ufo.Enemy(910, 20, 100, 60, 5, "ufo.png"))
    Enemies.append(asteroid.Enemy(1030, 20, 80, 60, 5, "asteroid.png"))
    Enemies.append(ufo.Enemy(1130, 20, 100, 60, 5, "ufo.png"))
    Enemies.append(asteroid.Enemy(1250, 20, 80, 60, 5, "asteroid.png"))


    game = True
    while game:
        #обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                write_data()

        #оновлення
        Rocket.movement()
        for u in Enemies:
            u.movement()

        for enemy in Enemies:
            for bullet in Rocket.bullets:
                if enemy.hitbox.colliderect(bullet.hitbox):
                    Rocket.bullets.remove(bullet)
                    enemy.hitbox.y = 1000
                    settings["money balance"] += 1
                    break


        #рендер
        window.fill((0, 0, 0))
        window.blit(backgroundImage, (0, 0))

        Rocket.Render((window))
        for u in Enemies:
            u.Render(window)


        pygame.display.flip()
        fps.tick(60)