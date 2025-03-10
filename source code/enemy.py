import pygame
from abc import ABC, abstractmethod

class Enemy(ABC, pygame.sprite.Sprite):
    def __init__(self, x, y, health, speed, image):
        """
        Initialize the base Enemy class.

        Args:
            x (int): The x-coordinate of the enemy.
            y (int): The y-coordinate of the enemy.
            health (int): The health of the enemy.
            speed (int): The speed of the enemy.
            image (pygame.Surface): The image of the enemy.
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = health
        self.speed = speed

    @abstractmethod
    def update(self, *args, **kwargs):
        """
        Update the enemy's position and behavior.
        This method must be implemented by subclasses.
        """
        pass

    @staticmethod
    def spawn_wave(enemies, all_sprites, image):
        """
        Spawn a wave of enemies.
        This method can be overridden by subclasses for custom behavior.
        """
        pass