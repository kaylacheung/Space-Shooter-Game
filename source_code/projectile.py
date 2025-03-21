import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, image):
        """
        Initialize the Projectile.

        Args:
            x (int): The x-coordinate of the projectile.
            y (int): The y-coordinate of the projectile.
            speed (int): The speed of the projectile.
            image (pygame.Surface): The image of the projectile.
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def update(self, *args, **kwargs):
        """
        Update the projectile's position.
        If it moves off the screen, it is removed.
        """
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()