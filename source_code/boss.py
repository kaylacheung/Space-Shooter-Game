import pygame
from enemy import Enemy
from blood import Blood
from init import SCREEN_WIDTH, SCREEN_HEIGHT

class Boss(Enemy):
    def __init__(self, x, y, boss_level, image, assets):
        """
        Initialize the Boss.

        Args:
            x (int): The x-coordinate of the boss.
            y (int): The y-coordinate of the boss.
            boss_level (int): The level of the boss, which affects its health and speed.
            image (pygame.Surface): The image of the boss.
            assets (dict): A dictionary containing all game assets.
        """
        # Call the parent class (Enemy) constructor.
        super().__init__(x, y, health=500 + (boss_level - 1) * 200, speed=2 + (boss_level - 1) * 1, image=image)
        self.boss_level = boss_level
        self.max_health = self.health  # Store the maximum health for the health bar.
        self.assets = assets  # Store the assets for accessing the blood image.

    def update(self, *args, **kwargs):
        """
        Update the boss's position and behavior.
        The boss moves horizontally and bounces off screen edges.
        """
        self.rect.x += self.speed
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.speed = -self.speed

    def shoot_blood(self):
        """
        Create a blood projectile.

        Returns:
            Blood: A Blood object representing the projectile.
        """
        return Blood(self.rect.centerx, self.rect.bottom, speed=5 + (self.boss_level - 1) * 1, image=self.assets["blood"])

    def draw_health_bar(self, surface):
        """
        Draw a health bar above the boss.

        Args:
            surface (pygame.Surface): The surface to draw the health bar on.
        """
        bar_width = self.rect.width
        bar_height = 5
        health_ratio = self.health / self.max_health
        fill_width = int(bar_width * health_ratio)
        outline_rect = pygame.Rect(self.rect.x, self.rect.y - bar_height - 2, bar_width, bar_height)
        fill_rect = pygame.Rect(self.rect.x, self.rect.y - bar_height - 2, fill_width, bar_height)
        pygame.draw.rect(surface, (255, 0, 0), fill_rect)  # Red fill for health.
        pygame.draw.rect(surface, (255, 255, 255), outline_rect, 1)  # White outline.

    @staticmethod
    def spawn_bosses(boss_level, enemies, all_sprites, image, assets):
        """
        Spawn a wave of bosses.

        Args:
            boss_level (int): The level of the bosses to spawn.
            enemies (pygame.sprite.Group): The group to add the bosses to.
            all_sprites (pygame.sprite.Group): The group to add the bosses to for rendering.
            image (pygame.Surface): The image of the boss.
            assets (dict): A dictionary containing all game assets.

        Returns:
            list: A list of Boss objects that were spawned.
        """
        bosses = []
        spacing = SCREEN_WIDTH // (boss_level + 1)
        for i in range(1, boss_level + 1):
            x = spacing * i
            boss = Boss(x, 100, boss_level, image, assets)
            bosses.append(boss)
            enemies.add(boss)
            all_sprites.add(boss)
        return bosses