import sys
import pygame
from init import initialize_pygame, load_assets, create_sprite_groups, SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from screens.game_over_screen import GameOverScreen, draw_text
from screens.main_menu_screen import main_menu_screen
from screens.game_screen import GameScreen
from screens.scrolling_background import ScrollingBackground
from spaceship import Spaceship
from alien import Alien
from asteroid import Asteroid
from boss import Boss
from projectile import Projectile
from blood import Blood     

# Hi my name is Kayla 

class Game:
    def __init__(self):
        # Initialise pygame and load assets.
        self.screen = initialize_pygame()
        self.assets = load_assets()
        self.sprite_groups = create_sprite_groups()  # Create sprite groups.
        self.all_sprites = self.sprite_groups["all_sprites"]  # Access the all_sprites group.
        self.enemies = self.sprite_groups["enemies"]
        self.projectiles = self.sprite_groups["projectiles"]
        self.boss_bloods = self.sprite_groups["boss_bloods"]

        # Initialize game objects.
        self.background = ScrollingBackground(self.assets["background"], speed=3)
        self.player = Spaceship(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, speed=5, image=self.assets["spaceship"])
        self.all_sprites.add(self.player)  # Add player to the all_sprites group.

        # Initialize screen classes.
        self.game_screen = GameScreen(self.screen, self.assets)
        self.game_over_screen = None

        # Game variables.
        self.lives = 5
        self.score = 0
        self.boss_level = 1
        self.bosses = []
        self.enemy_wave_count = 1

        # Set up timers.
        self.setup_timers()

    def setup_timers(self):
        """Set up timers for enemy wave spawn and boss blood attacks."""
        self.SPAWN_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWN_EVENT, 5000)  # Spawn waves every 5 seconds.
        self.BOSS_BLOOD_EVENT = pygame.USEREVENT + 2
        pygame.time.set_timer(self.BOSS_BLOOD_EVENT, 3000)  # Boss blood attack every 3 seconds.

    def run(self):
        """Main game loop."""
        clock = pygame.time.Clock()
        while True:
            if not main_menu_screen(self.screen):
                break  # Exit if the player quits from the main menu.

            self.reset_game()
            while True:
                self.handle_events()
                self.update_game_state()
                self.draw()
                pygame.display.flip()
                clock.tick(FPS)

                if self.lives <= 0:
                    self.game_over_screen = GameOverScreen(self.screen, self.score)
                    if not self.game_over_screen.show():
                        break  # Exit if the player quits from the game over screen.
                    self.reset_game()

    def handle_events(self):
        """Handle all game events (e.g., quitting, key presses)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == self.SPAWN_EVENT:
                self.spawn_enemy_wave()
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event)
            elif event.type == self.BOSS_BLOOD_EVENT:
                self.handle_boss_blood()

    def handle_keydown(self, event):
        """Handle key presses (e.g., shooting, retrying)."""
        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
            self.player.shoot(self.all_sprites, self.projectiles, self.assets["projectile"])

    def handle_boss_blood(self):
        """Handle boss blood attacks."""
        if self.bosses:
            for boss in self.bosses:
                blood = boss.shoot_blood()
                self.all_sprites.add(blood)
                self.boss_bloods.add(blood)

    def spawn_enemy_wave(self):
        """Spawn a wave of enemies (aliens and asteroids)."""
        if not self.bosses:  # Only spawn waves if no boss is active.
            Alien.spawn_wave(self.enemies, self.all_sprites, self.assets["alien"])
            if self.enemy_wave_count == 1:  # Only spawn asteroids in the first wave.
                Asteroid.spawn_wave(self.enemies, self.all_sprites, self.assets["asteroid"])
            self.enemy_wave_count += 1
            if self.enemy_wave_count >= 4:
                self.spawn_bosses()

    def spawn_bosses(self):
        """Spawn bosses based on the current boss level."""
        self.bosses = Boss.spawn_bosses(self.boss_level, self.enemies, self.all_sprites, self.assets["boss"], self.assets)
        self.enemy_wave_count = 0  # Reset wave count.

    def update_game_state(self):
        """Update all game objects and check for collisions."""
        self.all_sprites.update(pygame.key.get_pressed())  # Update all sprites.
        self.background.update()
        self.check_collisions()
        self.check_game_over()


    def draw(self):
        """Draw all game objects and UI elements."""
        self.background.draw(self.screen)  # Draw the scrolling background.
        self.game_screen.draw(self.all_sprites, self.bosses, self.score, self.lives)  # Use GameScreen to draw everything.
        pygame.display.flip()

    def check_collisions(self):
        """Check for collisions between projectiles, enemies, and the player."""
        for projectile in self.projectiles:
            enemies_hit = pygame.sprite.spritecollide(projectile, self.enemies, False)
            for enemy in enemies_hit:
                projectile.kill()  # Remove the projectile.
                enemy.health -= 30  # Reduce enemy health.
                if enemy.health <= 0:
                    enemy.kill()  # Remove the enemy if health reaches zero.
                    if enemy in self.bosses:  # Check if the enemy is a boss.
                        self.bosses.remove(enemy)  # Remove the boss from the bosses list.
                        pygame.time.set_timer(self.BOSS_BLOOD_EVENT, 0)  # Stop blood attacks.
                    self.score += 100  # Increase score when an enemy is killed.

        # Check if boss blood hits the player.
        if pygame.sprite.spritecollide(self.player, self.boss_bloods, True):
            self.lives -= 1

        # Check if player touches enemies.
        if pygame.sprite.spritecollide(self.player, self.enemies, True):
            self.lives -= 1

    def check_game_over(self):
        """Check if the game is over (lives <= 0)."""
        if self.lives <= 0:
            return True
        return False

    def reset_game(self):
        """Reset the game state."""
        self.lives = 5
        self.score = 0
        self.boss_level = 1
        self.bosses = []
        self.enemy_wave_count = 0
        self.all_sprites.empty()
        self.enemies.empty()
        self.projectiles.empty()
        self.boss_bloods.empty()
        self.player = Spaceship(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, speed=5, image=self.assets["spaceship"])
        self.all_sprites.add(self.player)
        self.spawn_enemy_wave()

    def quit_game(self):
        """Quit the game."""
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()