import pygame
import random
from prototype_spaceship import Spaceship
from prototype_enemy import Alien
from prototype_projectiles import Projectile

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialise screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter Prototype")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

# Create player
player = Spaceship()
all_sprites.add(player)

# Spawn initial enemies
for _ in range(5):
    alien = Alien(random.randint(0, SCREEN_WIDTH), random.randint(-100, -40))
    all_sprites.add(alien)
    enemies.add(alien)

# Game variables
score = 0
lives = 3

# Timer for spawning enemy waves
SPAWN_WAVE_EVENT = pygame.USEREVENT + 1  # Custom event for spawning waves
pygame.time.set_timer(SPAWN_WAVE_EVENT, 5000)  # Spawn a wave every 5 seconds

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(projectiles)
                all_sprites.add(projectiles)
        elif event.type == SPAWN_WAVE_EVENT:  # Spawn a new wave
            for _ in range(5):  # Spawn 5 new aliens
                alien = Alien(random.randint(0, SCREEN_WIDTH), random.randint(-100, -40))
                all_sprites.add(alien)
                enemies.add(alien)

    # Update game state
    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    # Check for collisions
    for projectile in projectiles:
        enemies_hit = pygame.sprite.spritecollide(projectile, enemies, True)
        for enemy in enemies_hit:
            projectile.kill()
            score += 10

    if pygame.sprite.spritecollide(player, enemies, True):
        lives -= 1
        if lives <= 0:
            running = False

    # Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Draw score and lives
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()