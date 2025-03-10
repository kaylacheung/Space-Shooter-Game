import pygame
from init import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, load_assets
from screens.scrolling_background import ScrollingBackground

def test_background():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    assets = load_assets()
    background = ScrollingBackground(assets["background"], speed=3)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        background.update()
        background.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

test_background()