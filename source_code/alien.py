from enemy import Enemy
from init import SCREEN_WIDTH, SCREEN_HEIGHT

class Alien(Enemy):
    def __init__(self, x, y, health, speed, image):
        """
        Initialize the Alien class.

        Args:
            x (int): The x-coordinate of the alien.
            y (int): The y-coordinate of the alien.
            health (int): The health of the alien.
            speed (int): The speed of the alien.
            image (pygame.Surface): The image of the alien.
        """
        super().__init__(x, y, health, speed, image)
        self.hor_direction = 1  # 1 for right, -1 for left

    def update(self, *args, **kwargs):
        """
        Update the alien's position and behavior.
        The alien moves horizontally and vertically, bouncing off screen edges.
        """
        self.rect.x += self.speed * self.hor_direction
        self.rect.y += self.speed / 4
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.hor_direction *= -1
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

    @staticmethod
    def spawn_wave(enemies, all_sprites, image, level):
        """
        Spawn a wave of aliens.

        Args:
            enemies (pygame.sprite.Group): The group to add the aliens to.
            all_sprites (pygame.sprite.Group): The group to add the aliens to for rendering.
            image (pygame.Surface): The image of the alien.
        """
        num_enemies = 8
        spacing = SCREEN_WIDTH // (num_enemies + 1)
        for i in range(1, num_enemies + 1):
            x = spacing * i
            alien = Alien(x, 50, health=100, speed=2, image=image)
            enemies.add(alien)
            all_sprites.add(alien)