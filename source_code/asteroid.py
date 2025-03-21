from enemy import Enemy
from init import SCREEN_HEIGHT, SCREEN_WIDTH

class Asteroid(Enemy):
    def __init__(self, x, y, health, speed, image):
        """
        Initialize the Asteroid class.

        Args:
            x (int): The x-coordinate of the asteroid.
            y (int): The y-coordinate of the asteroid.
            health (int): The health of the asteroid.
            speed (int): The speed of the asteroid.
            image (pygame.Surface): The image of the asteroid.
        """
        super().__init__(x, y, health, speed, image)

    def update(self, *args, **kwargs):
        """
        Update the asteroid's position and behavior.
        The asteroid moves vertically and wraps around the screen.
        """
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

    @staticmethod
    def spawn_wave(enemies, all_sprites, image):
        """
        Spawn a wave of asteroids.

        Args:
            enemies (pygame.sprite.Group): The group to add the asteroids to.
            all_sprites (pygame.sprite.Group): The group to add the asteroids to for rendering.
            image (pygame.Surface): The image of the asteroid.
        """
        num_enemies = 8
        spacing = SCREEN_WIDTH // (num_enemies + 1)
        for i in range(1, num_enemies + 1):
            x = spacing * i
            asteroid = Asteroid(x, 100, health=50, speed=2, image=image)
            enemies.add(asteroid)
            all_sprites.add(asteroid)