import pygame
import sys
from init import SCREEN_WIDTH, SCREEN_HEIGHT


class LevelTransitionScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)  # Use a simple font.
        self.bg_color = (0, 0, 0)  # Black background for transition.

    def show_level_transition(self, level):
        """Display the level transition screen for a given level."""
        self.screen.fill(self.bg_color)
        level_text = f"Level {level} Transition"
        instruction_text = "Press Enter to continue"
        
        level_surface = self.font.render(level_text, True, (255, 255, 255))  # White text for level.
        instruction_surface = self.font.render(instruction_text, True, (255, 255, 255))  # White text for instruction.
        
        self.screen.blit(level_surface, (SCREEN_WIDTH // 2 - level_surface.get_width() // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(instruction_surface, (SCREEN_WIDTH // 2 - instruction_surface.get_width() // 2, SCREEN_HEIGHT // 2))
        
        pygame.display.flip()

        # Wait for the player to press Enter.
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
