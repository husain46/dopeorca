import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Mario Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)  # Mario is red for simplicity
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT - 100
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.speed = 5
        self.jump_power = -15
        self.gravity = 1

    def update(self):
        # Handle input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel_x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.vel_x = self.speed
        else:
            self.vel_x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

        # Apply gravity
        self.vel_y += self.gravity

        # Update position
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Check boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0

        # Ground collision (simple)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0
            self.on_ground = True

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Enemy class (simple goomba)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = -2  # Move left

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

# Sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create platforms
ground = Platform(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
platform1 = Platform(300, 400, 200, 20)
platform2 = Platform(600, 300, 150, 20)

all_sprites.add(ground, platform1, platform2)
platforms.add(ground, platform1, platform2)

# Create enemies
enemy1 = Enemy(700, SCREEN_HEIGHT - 80)
enemy2 = Enemy(500, 370)

all_sprites.add(enemy1, enemy2)
enemies.add(enemy1, enemy2)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Collision with platforms
    player.on_ground = False
    hits = pygame.sprite.spritecollide(player, platforms, False)
    for hit in hits:
        if player.vel_y > 0 and player.rect.bottom > hit.rect.top:
            player.rect.bottom = hit.rect.top
            player.vel_y = 0
            player.on_ground = True

    # Collision with enemies
    if pygame.sprite.spritecollide(player, enemies, False):
        print("Game Over!")
        running = False

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()