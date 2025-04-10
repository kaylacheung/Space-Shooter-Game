import pygame
import sys
from init import SCREEN_WIDTH, SCREEN_HEIGHT

class CongratulationsScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)  # Use a simple font.
        self.bg_color = (0, 0, 0)  # Black background for transition.

    def show_congratulations(self):
        """Display the congratulations screen when the player finishes all levels."""
        self.screen.fill(self.bg_color)
        congrats_text = "Congratulations! You've completed all levels!"
        
        congrats_surface = self.font.render(congrats_text, True, (255, 255, 255))  # White text.
        
        self.screen.blit(congrats_surface, (SCREEN_WIDTH // 2 - congrats_surface.get_width() // 2, SCREEN_HEIGHT // 2))
        
        pygame.display.flip()

        # Wait for the player to press Enter or close the game.
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                        return
