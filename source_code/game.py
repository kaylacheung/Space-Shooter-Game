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
from screens.level_transition_screen import LevelTransitionScreen  # Import Level Transition Screen
from screens.congratulations_screen import CongratulationsScreen  # Import Congratulations Screen

# Hello I am KAyla

class Game:
    def __init__(self):
        """Initialise the game and set up variables."""
        self.screen = initialize_pygame()
        self.assets = load_assets()
        self.sprite_groups = create_sprite_groups()  # Create sprite groups.
        self.all_sprites = self.sprite_groups["all_sprites"]  # Access the all_sprites group.
        self.enemies = self.sprite_groups["enemies"]
        self.projectiles = self.sprite_groups["projectiles"]
        self.boss_bloods = self.sprite_groups["boss_bloods"]
        self.can_spawn_next_wave = True

        # Initialise game objects
        self.background = ScrollingBackground(self.assets["background"], speed=3)
        self.player = Spaceship(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, speed=5, image=self.assets["spaceship"])
        self.all_sprites.add(self.player)  # Add player to the all_sprites group

        # Initialise screen classes
        self.game_screen = GameScreen(self.screen, self.assets)
        self.game_over_screen = None
        self.level_transition_screen = LevelTransitionScreen(self.screen)  # Initialise level transition screen
        self.congratulations_screen = CongratulationsScreen(self.screen)  # Initialise congratulations screen

        # Game variables/ constants
        self.lives = 5
        self.score = 0
        self.boss_level = 1
        self.bosses = []
        self.enemy_wave_count = 1
        self.current_level = 1 

        
        self.setup_timers()

    def setup_timers(self):
        """Set up timers for enemy wave spawn and boss blood attacks."""
        self.SPAWN_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWN_EVENT, 5000)  # Spawn waves every 5 seconds
        self.BOSS_BLOOD_EVENT = pygame.USEREVENT + 2
        pygame.time.set_timer(self.BOSS_BLOOD_EVENT, 2000)  # Boss blood attack every TWO SECONDs

    def run(self):
        """Main game loop."""

        clock = pygame.time.Clock()
        while True:
            if not main_menu_screen(self.screen):
                break  # Exit when player quits from main menu.

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
                        break  # Exit if the player quits from the game over screen
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
                if blood:  # Check if blood is returned by the boss
                    self.all_sprites.add(blood)
                    self.boss_bloods.add(blood)

    def spawn_enemy_wave(self):
        """Spawn a wave of enemies (aliens and asteroids)."""
        if not self.bosses:  # Only spawn waves if no boss is active.
            Alien.spawn_wave(self.enemies, self.all_sprites, self.assets["alien"], self.current_level)
            Asteroid.spawn_wave(self.enemies, self.all_sprites, self.assets["asteroid"], self.current_level)
            self.enemy_wave_count += 1
            if self.enemy_wave_count >= 4:
                self.spawn_bosses()

        # Check if the boss is defeated and transition to the next level
        if not self.bosses and self.enemy_wave_count >= 4:
            self.level_up()


    def spawn_bosses(self):
        """Spawn bosses based on the current boss level."""
        num_bosses = self.current_level  # The number of bosses should = current boss level eg level2 = 2 bosses; level 3 = 3 bosses
        
        # Spawn the bosses for the current level
        self.bosses = Boss.spawn_bosses(num_bosses, self.enemies, self.all_sprites, self.assets["boss"], self.assets)
        self.enemy_wave_count = 0  # Reset wave count
        
        # Make sure each boss has its own blood attack event
        pygame.time.set_timer(self.BOSS_BLOOD_EVENT, 2000)  # Ensure each boss spits out blood



    def update_game_state(self):
        """Update all game objects and check for collisions."""
        self.all_sprites.update(pygame.key.get_pressed())
        self.background.update()
        self.check_collisions()
        self.check_game_over()

        # Check if all bosses are defeated before transitioning to the next level
        if not self.bosses and self.enemy_wave_count >= 4:
            self.level_up()  # Call level_up only when all bosses are defeated

        # Check if current wave has cleared the screen
        if not self.can_spawn_next_wave:
            wave_cleared = True
            for enemy in self.enemies:
                if isinstance(enemy, (Alien, Asteroid)) and enemy.rect.top < SCREEN_HEIGHT:
                    wave_cleared = False
                    break
            if wave_cleared:
                self.can_spawn_next_wave = True
                    
        # Check for boss spawn conditions
        if (self.enemy_wave_count >= 8 and 
            len(self.enemies) == 0 and 
            not self.bosses):
            self.spawn_bosses()

    def draw(self):
        """Draw all game objects and UI elements."""
        self.background.draw(self.screen)  # Draw the scrolling background
        self.game_screen.draw(self.all_sprites, self.bosses, self.score, self.lives)  # Use GameScreen to draw everything.
        pygame.display.flip()

    def check_collisions(self):
        """Check for collisions between projectiles, enemies, and the player."""
        # Check projectile-enemy collisions
        for projectile in self.projectiles:
            # Get all enemies hit by this projectile
            enemies_hit = pygame.sprite.spritecollide(projectile, self.enemies, False)
            for enemy in enemies_hit:
                projectile.kill()  # Remove the projectile
                if isinstance(enemy, Boss):  # Boss takes damage but doesn't die immediately
                    enemy.health -= 30
                    if enemy.health <= 0:
                        enemy.kill()
                        self.bosses.remove(enemy)
                        pygame.time.set_timer(self.BOSS_BLOOD_EVENT, 0)
                        self.score += 100
                        # Immediately spawn new wave after boss dies
                        self.enemy_wave_count = 1
                        pygame.time.set_timer(self.SPAWN_EVENT, 3000)  # Reset to 3 seconds
                        self.spawn_enemy_wave()  # Spawn first wave immediately
                        
                                                # If all bosses are defeated, trigger level transition
                        if len(self.bosses) == 0:
                            pygame.time.set_timer(self.BOSS_BLOOD_EVENT, 0)
                            self.level_up()

                else:  # Regular enemies (Aliens, Asteroids) die immediately
                    enemy.kill()
                    self.score += 100

        # Check player-enemy collisions.
        enemies_collided = pygame.sprite.spritecollide(self.player, self.enemies, False)
        for enemy in enemies_collided:
            if isinstance(enemy, Boss):  # Boss collision
                self.lives -= 1
            else:  # Regular enemy collision
                enemy.kill()
                self.lives -= 1

        # Check boss blood collisions
        if pygame.sprite.spritecollide(self.player, self.boss_bloods, True):
            self.lives -= 1

        # Check if player touches enemies
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
        self.current_level = 1  # Reset to Level 1 at the start
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

    def level_up(self):
        """Handle level-up transition."""
        self.lives = 5  # Reset lives to 5 at the start of every new level

        if self.current_level == 1:
            self.level_transition_screen.show_level_transition(self.current_level)
            self.current_level = 2
            self.enemy_wave_count = 0
            self.spawn_enemy_wave()
        elif self.current_level == 2:
            self.level_transition_screen.show_level_transition(self.current_level)
            self.current_level = 3
            self.enemy_wave_count = 0
            self.spawn_enemy_wave()
        elif self.current_level == 3:
            self.level_transition_screen.show_level_transition(self.current_level)
            self.current_level = 4
            self.enemy_wave_count = 0
            self.spawn_enemy_wave()

        elif self.current_level == 4:
            self.congratulations_screen.show_congratulations()

if __name__ == "__main__":
    game = Game()
    game.run()
