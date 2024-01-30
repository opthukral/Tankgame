from healthbar import HealthBar
from bullet import Bullet
from constants import *


class Player:
    SPEED = 7
    SHOOT_COOLDOWN = 500

    def __init__(self, x, y, image, keys, border, shoots_right):
        # Player variables
        self.healthbar = HealthBar(border.centerx, border.h // 10)
        self.border = border
        self.keys = keys
        self.shoots_right = shoots_right
        self.opponent = None
        self.bullet_timer = 0
        self.bullets = []

        # Position related variables
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def shoot(self):
        self.bullet_timer = pygame.time.get_ticks()
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.shoots_right)
        self.bullets.append(bullet)

    def update_bullets(self):
        # Updates the bullets
        for bullet in self.bullets:
            bullet.update()

            # Checks if the bullet hits the opponent
            if bullet.rect.colliderect(self.opponent.rect):
                self.opponent.healthbar.hearts -= 1
                self.bullets.remove(bullet)

            # Removes the bullet if it's out of the map
            if bullet.rect.left > SCREEN_WIDTH or bullet.rect.right < 0 or bullet.rect.top > SCREEN_HEIGHT or bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def update(self, key_pressed):
        # Updates the players position if the keys are pressed | Also checks for border collision
        if key_pressed[self.keys["UP"]] and self.rect.top - self.SPEED >= self.border.top:
            self.y -= self.SPEED
        if key_pressed[self.keys["DOWN"]] and self.rect.bottom + self.SPEED <= self.border.bottom:
            self.y += self.SPEED
        if key_pressed[self.keys["RIGHT"]] and self.rect.right + self.SPEED <= self.border.right:
            self.x += self.SPEED
        if key_pressed[self.keys["LEFT"]] and self.rect.left - self.SPEED >= self.border.left:
            self.x -= self.SPEED
        if key_pressed[self.keys["SHOOT"]] and pygame.time.get_ticks() - self.SHOOT_COOLDOWN >= self.bullet_timer:
            self.shoot()

        # Updates the player's rectangle where we will blit the image
        self.rect = self.image.get_rect(center=(self.x, self.y))

        # Updates the healthbar
        self.healthbar.update()

        # Calls the method to update the bullets
        self.update_bullets()

    def draw(self, screen):
        # Draws every bullet
        for bullet in self.bullets:
            bullet.draw(screen)

        # Draws Health Bar
        self.healthbar.draw(screen)

        # Draws Player
        screen.blit(self.image, self.rect)
