import pygame
from init import SCREEN_WIDTH, SCREEN_HEIGHT

def draw_text(surface, text, size, color, x, y):
    """Draw text on the screen."""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def main_menu_screen(screen):
    """Display the main menu screen and handle input."""
    screen.fill((0, 0, 0))
    draw_text(screen, "MAIN MENU", 74, (255, 0, 0), SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 3)
    draw_text(screen, "Press SPACE to Start", 36, (255, 255, 255), SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Quit the game.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True  # Start the game.