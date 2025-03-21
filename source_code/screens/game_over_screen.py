import pygame
from init import SCREEN_WIDTH, SCREEN_HEIGHT

def draw_text(surface, text, size, color, x, y):
    """Draw text on the screen."""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

class GameOverScreen:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score

    def show(self):
        """Display the game over screen and handle retries."""
        self.screen.fill((0, 0, 0))
        draw_text(self.screen, "GAME OVER", 74, (255, 0, 0), SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 3)
        draw_text(self.screen, f"Score: {self.score}", 36, (255, 255, 255), SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2)
        draw_text(self.screen, "Press R to Retry", 36, (255, 255, 255), SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False  # Quit the game.
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return True  # Retry the game.