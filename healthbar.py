from constants import *


class HealthBar:
    def __init__(self, x, y):
        self.hearts = 3
        self.x = x
        self.y = y
        self.image = heart3
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        # Sets the right image to the healthbar
        if self.hearts == 3:
            self.image = heart3
        elif self.hearts == 2:
            self.image = heart2
        elif self.hearts == 1:
            self.image = heart1

        # Updates the rect position
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        # If player has no more hearts, display nothing
        if self.hearts > 0:
            screen.blit(self.image, self.rect)
