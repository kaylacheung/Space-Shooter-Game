import unittest
import pygame
from prototype_spaceship import Spaceship
from prototype_enemy import Alien
from prototype_projectiles import Projectile

# InitialiSe Pygame (required for rendering and rect calculations)
pygame.init()

# Screen dimensions for testing
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class TestBoundaries(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        # Create a dummy image for testing
        self.dummy_image = pygame.Surface((50, 50))

        # Initialize player, alien, and projectile objects
        # Mock the Spaceship class to match its current implementation
        self.player = Spaceship()
        self.player.image = self.dummy_image
        self.player.rect = self.player.image.get_rect()
        self.player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.player.speed = 5  # Add speed attribute for testing

        # Mock the Alien class to match its current implementation
        self.alien = Alien(SCREEN_WIDTH // 2, 0)
        self.alien.image = self.dummy_image
        self.alien.rect = self.alien.image.get_rect()
        self.alien.rect.center = (SCREEN_WIDTH // 2, 0)
        self.alien.speed = 2  # Add speed attribute for testing

        # Mock the Projectile class to match its current implementation
        self.projectile = Projectile(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.projectile.image = self.dummy_image
        self.projectile.rect = self.projectile.image.get_rect()
        self.projectile.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.projectile.speed = 5  # Add speed attribute for testing

    def test_player_left_boundary(self):
        """Test that the player cannot move outside the left edge of the screen."""
        # Move player to the left edge
        self.player.rect.left = 0
        # Simulate the left arrow key being pressed
        keys = {pygame.K_LEFT: True, pygame.K_RIGHT: False}
        # Try to move further left
        self.player.update(keys)
        # Check that the player's position hasn't changed
        self.assertEqual(self.player.rect.left, 0)

    def test_player_right_boundary(self):
        """Test that the player cannot move outside the right edge of the screen."""
        # Move player to the right edge
        self.player.rect.right = SCREEN_WIDTH
        # Simulate the right arrow key being pressed
        keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True}
        # Try to move further right
        self.player.update(keys)
        # Check that the player's position hasn't changed
        self.assertEqual(self.player.rect.right, SCREEN_WIDTH)

    def test_enemy_wrap_around(self):
        """Test that enemies wrap around the screen when they move off the bottom edge."""
        # Move alien off the bottom edge
        self.alien.rect.top = SCREEN_HEIGHT + 10
        # Update the alien's position
        self.alien.update()
        # Check that the alien has wrapped around to the top
        self.assertEqual(self.alien.rect.bottom, 0)

    def test_projectile_off_screen(self):
        """Test that projectiles are removed when they move off the top edge of the screen."""
        # Move projectile off the top edge
        self.projectile.rect.bottom = -10
        # Update the projectile's position
        self.projectile.update()
        # Check that the projectile is no longer alive
        self.assertFalse(self.projectile.alive())

if __name__ == "__main__":
    unittest.main()