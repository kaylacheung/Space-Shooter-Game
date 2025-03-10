import pygame
from init import SCREEN_HEIGHT

class Blood(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, image):
        """
        Initialize the Blood projectile.

        Args:
            x (int): The x-coordinate of the blood projectile.
            y (int): The y-coordinate of the blood projectile.
            speed (int): The speed of the blood projectile.
            image (pygame.Surface, optional): The image of the blood.
        """
        super().__init__()
        if image:
            self.image = image
        else:
            # Fallback: Create a red circle if the image is not available.
            self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (139, 0, 0), (5, 5), 5)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def update(self, *args, **kwargs):
        """
        Update the blood projectile's position.
        If it moves off the screen, it is removed.
        """
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()