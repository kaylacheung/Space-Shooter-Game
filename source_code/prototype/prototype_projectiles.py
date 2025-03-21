import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 255))  # Blue square for projectile
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self, *args, **kwargs):
        """Move the projectile upward."""
        self.rect.y -= self.speed
        if self.rect.bottom < 0:  # Off-screen
            self.kill()