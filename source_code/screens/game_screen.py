import pygame
from init import SCREEN_WIDTH, SCREEN_HEIGHT

def draw_text(surface, text, size, color, x, y):
    """Draw text on the screen."""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

class GameScreen:
    def __init__(self, screen, assets):
        self.screen = screen
        self.assets = assets

    def draw(self, all_sprites, bosses, score, lives):
        """Draw all game objects and UI elements."""
        all_sprites.draw(self.screen)
        if bosses:
            for boss in bosses:
                boss.draw_health_bar(self.screen)
        draw_text(self.screen, f"Score: {score}", 36, (255, 255, 255), 10, 10)
        self.draw_hearts(lives)  # Draw hearts.

    def draw_hearts(self, lives):
        """Draw the player's remaining lives as hearts."""
        heart_spacing = 5
        for i in range(lives):
            x = SCREEN_WIDTH - (i + 1) * (self.assets["heart"].get_width() + heart_spacing) - 10
            y = 10
            self.screen.blit(self.assets["heart"], (x, y))