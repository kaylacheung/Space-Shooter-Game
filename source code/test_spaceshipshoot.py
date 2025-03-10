import unittest
import pygame
from spaceship import Spaceship
from projectile import Projectile

class TestSpaceshipShoot(unittest.TestCase):
    def setUp(self):
        pygame.init()
        # Create a mock spaceship image 
        self.mock_spaceship_image = pygame.Surface((50, 50))  
        # Create a mock projectile image 
        self.mock_projectile_image = pygame.Surface((10, 10))  
        # Create a Spaceship instance
        self.spaceship = Spaceship(x=100, y=200, speed=5, image=self.mock_spaceship_image)
        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

    def test_shoot_creates_projectile(self):
        # Call the shoot method
        self.spaceship.shoot(self.all_sprites, self.projectiles, self.mock_projectile_image)
        
        # Check if a projectile was added to the all_sprites group
        self.assertEqual(len(self.all_sprites), 1)  # Spaceship + Projectile
        # Check if a projectile was added to the projectiles group
        self.assertEqual(len(self.projectiles), 1)
        
        # Verify the projectile is an instance of the Projectile class
        projectile = self.projectiles.sprites()[0]
        self.assertIsInstance(projectile, Projectile)
        
        # Verify the projectile's position matches the spaceship's position
        self.assertEqual(projectile.rect.centerx, self.spaceship.rect.centerx)
        # Account for the projectile's height when checking rect.top
        self.assertEqual(projectile.rect.top, self.spaceship.rect.top - (projectile.rect.height // 2))

    def tearDown(self):
        pygame.quit()

if __name__ == "__main__":
    unittest.main()