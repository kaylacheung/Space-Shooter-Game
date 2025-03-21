import pygame
import math
from init import SCREEN_WIDTH
from projectile import Projectile

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, image):
        """
        Initialize the Spaceship.

        Args:
            x (int): The x-coordinate of the spaceship.
            y (int): The y-coordinate of the spaceship.
            speed (int): The speed of the spaceship.
            image (pygame.Surface): The image of the spaceship.
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        # Save base x position for oscillation.
        self.base_x = self.rect.x

    def update(self, keys, *args, **kwargs):
        """
        Update the spaceship's position based on key inputs.
        If no keys are pressed, the spaceship oscillates slightly.

        Args:
            keys (list): A list of keys currently pressed.
        """
        moved = False
        # If left/right keys pressed, update position and base_x.
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            moved = True
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
            moved = True

        if moved:
            self.base_x = self.rect.x
        else:
            # If no horizontal key is pressed, apply an oscillation.
            offset = int(5 * math.sin(pygame.time.get_ticks() * 0.01))
            self.rect.x = self.base_x + offset

    def shoot(self, all_sprites, projectiles, projectile_image):
        """
        Shoot a projectile from the spaceship.

        Args:
            all_sprites (pygame.sprite.Group): The group to add the projectile to for rendering.
            projectiles (pygame.sprite.Group): The group to add the projectile to for collision detection.
            projectile_image (pygame.Surface): The image of the projectile.
        """
        projectile = Projectile(self.rect.centerx, self.rect.top, speed=10, image=projectile_image)
        all_sprites.add(projectile)
        projectiles.add(projectile)