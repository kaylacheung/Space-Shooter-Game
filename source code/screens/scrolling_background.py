import pygame
from init import SCREEN_WIDTH, SCREEN_HEIGHT

class ScrollingBackground:
    def __init__(self, image, speed):
        """
        Initialize the ScrollingBackground.

        Args:
            image (pygame.Surface): The background image.
            speed (int): The speed at which the background scrolls.
        """
        self.image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.speed = speed
        # Two rects for continuous vertical scrolling.
        self.rect1 = self.image.get_rect(topleft=(0, 0))
        self.rect2 = self.image.get_rect(topleft=(0, -SCREEN_HEIGHT))

    def update(self):
        """
        Update the position of the background for scrolling.
        """
        self.rect1.y += self.speed
        self.rect2.y += self.speed
        if self.rect1.top >= SCREEN_HEIGHT:
            self.rect1.y = self.rect2.top - SCREEN_HEIGHT
        if self.rect2.top >= SCREEN_HEIGHT:
            self.rect2.y = self.rect1.top - SCREEN_HEIGHT

    def draw(self, surface):
        """
        Draw the scrolling background on the screen.

        Args:
            surface (pygame.Surface): The surface to draw the background on.
        """
        surface.blit(self.image, self.rect1)
        surface.blit(self.image, self.rect2)