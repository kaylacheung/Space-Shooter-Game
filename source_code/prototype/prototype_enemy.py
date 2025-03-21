import pygame
import random

# Base Enemy class (abstract)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 2

    def update(self, *args, **kwargs):
        """Update enemy position (must be overridden by subclasses)."""
        raise NotImplementedError("Subclasses must implement update()")

# Alien subclass (inherits from Enemy)
class Alien(Enemy):
    def __init__(self, x, y):
        image = pygame.Surface((40, 40))
        image.fill((255, 0, 0))  # Red square for alien
        super().__init__(x, y, image)

    def update(self, *args, **kwargs):
        """Move the alien down the screen and wrap around."""
        self.rect.y += self.speed
        if self.rect.top > 600:  # Screen height
            self.rect.bottom = 0
            self.rect.x = random.randint(0, 800)  # Random x position