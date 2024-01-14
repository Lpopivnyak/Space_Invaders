import pygame

class Enemy:
    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def Render(self, window):
        window.blit(self.texture, (self.hitbox.x, self.hitbox.y))

    def movement(self):
        self.hitbox.y += self.speed