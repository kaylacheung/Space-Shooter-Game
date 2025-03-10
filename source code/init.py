import pygame
import sys
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


def initialize_pygame():
    """Initialize pygame and set up the screen."""
    try:
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Shooting Game")
        return screen
    except pygame.error as e:
        print(f"Failed to initialize pygame: {e}")
        sys.exit(1)  # Exit the program with an error code.

def load_assets():
    """Load all game assets (e.g., images, sounds)."""
    assets = {}

    # Load background image.
    try:
        assets["background"] = pygame.image.load('Space Shooter Game Project/assets/images/background.jpg').convert()
    except pygame.error as e:
        print(f"Failed to load background.jpg: {e}. Using fallback.")
        assets["background"] = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        assets["background"].fill((0, 0, 0))  # Black background.

    # Load heart image.
    try:
        heart_image = pygame.image.load('Space Shooter Game Project/assets/images/heart.png').convert_alpha()
        assets["heart"] = pygame.transform.scale(heart_image, (40, 40))  # Resize to 20x20 pixels.
    except pygame.error as e:
        print(f"Failed to load heart.png: {e}. Using fallback.")
        assets["heart"] = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(assets["heart"], (255, 0, 0), (15, 15), 15)  # Red circle.

    # Load spaceship image.
    try:
        assets["spaceship"] = pygame.image.load('Space Shooter Game Project/assets/images/spaceship.png').convert_alpha()
    except pygame.error as e:
        print(f"Failed to load spaceship.png: {e}. Using fallback.")
        assets["spaceship"] = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.rect(assets["spaceship"], (0, 255, 0), (0, 0, 50, 50))  # Green square.

    # Load alien image.
    try:
        assets["alien"] = pygame.image.load('Space Shooter Game Project/assets/images/alien.png').convert_alpha()
    except pygame.error as e:
        print(f"Failed to load alien.png: {e}. Using fallback.")
        assets["alien"] = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.rect(assets["alien"], (255, 0, 0), (0, 0, 50, 50))  # Red square.

    # Load asteroid image.
    try:
        assets["asteroid"] = pygame.image.load('Space Shooter Game Project/assets/images/asteroid.png').convert_alpha()
    except pygame.error as e:
        print(f"Failed to load asteroid.png: {e}. Using fallback.")
        assets["asteroid"] = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(assets["asteroid"], (128, 128, 128), (25, 25), 25)  # Gray circle.

    # Load boss image.
    try:
        assets["boss"] = pygame.image.load('Space Shooter Game Project/assets/images/boss.png').convert_alpha()
    except pygame.error as e:
        print(f"Failed to load boss.png: {e}. Using fallback.")
        assets["boss"] = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.rect(assets["boss"], (255, 0, 255), (0, 0, 100, 100))  # Purple square.

    # Load blood image.
    try:
        assets["blood"] = pygame.image.load('Space Shooter Game Project/assets/images/blood.png').convert_alpha()
    except pygame.error as e:
        print(f"Failed to load blood.png: {e}. Using fallback.")
        assets["blood"] = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(assets["blood"], (139, 0, 0), (5, 5), 5)  # Dark red circle.

    # Load projectile image.
    try:
        assets["projectile"] = pygame.image.load('Space Shooter Game Project/assets/images/projectile.png').convert_alpha()
    except pygame.error as e:
        print(f"Failed to load projectile.png: {e}. Using fallback.")
        assets["projectile"] = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.rect(assets["projectile"], (255, 255, 0), (0, 0, 10, 10))  # Yellow square.

    return assets


def create_sprite_groups():
    """Create and return all sprite groups."""
    return {
        "all_sprites": pygame.sprite.Group(),
        "enemies": pygame.sprite.Group(),
        "projectiles": pygame.sprite.Group(),
        "boss_bloods": pygame.sprite.Group(),
    }