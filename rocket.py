import pygame

from bullet import Bullet


class Character:
    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.bullets = []

    def Render(self, window):
        window.blit(self.texture, (self.hitbox.x, self.hitbox.y))
        for bullet in self.bullets:
            bullet.movement()
            bullet.Render(window)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.hitbox.x += self.speed
        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(self.hitbox.x, self.hitbox.y, 20, 20, 5, "bullet.png"))
