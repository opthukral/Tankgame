from constants import *


class Bullet:
    BULLET_SPEED = 12

    def __init__(self, x, y, shoot_right):
        self.x = x
        self.y = y
        self.speed = self.BULLET_SPEED if shoot_right else -self.BULLET_SPEED
        self.image = bullet_1 if shoot_right else bullet_2
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.x += self.speed
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
