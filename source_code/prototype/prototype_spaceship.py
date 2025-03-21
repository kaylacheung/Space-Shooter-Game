import pygame
from prototype_projectiles import Projectile

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Green square for player
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)  # Start at the bottom center
        self.speed = 5

    def update(self, keys):
        """Update player position based on key presses."""
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

    def shoot(self, projectiles):
        """Create a projectile and add it to the projectiles group."""
        projectile = Projectile(self.rect.centerx, self.rect.top)
        projectiles.add(projectile)