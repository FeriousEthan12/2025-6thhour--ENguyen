import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Epic Sword Fighting")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

player_width, player_height = 50, 60
player_x, player_y = 100, HEIGHT - player_height - 50
player_speed = 5
player_health = 100
player_attack_power = 20

enemy_width, enemy_height = 50, 60
enemy_x, enemy_y = WIDTH - 150, HEIGHT - enemy_height - 50
enemy_speed = 3
enemy_health = 200  # Increased HP for tougher enemy
enemy_attack_power = 10

knockback_distance = 20

font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()

running = True


def display_text(text, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


def player_block(keys):
    return keys[pygame.K_b]


def player_special_ability(keys):
    global player_special, special_cooldown
    if special_cooldown == 0 and keys[pygame.K_s]:
        player_special = True
        special_cooldown = 300


def enemy_attack(keys):
    global player_health, player_x
    melee_range = 60

    dx = abs(player_x - enemy_x)
    dy = abs(player_y - enemy_y)

    if dx < melee_range and dy < melee_range:
        if random.random() < 0.05:
            if not player_block(keys):
                player_health -= enemy_attack_power
                # Knockback player
                if player_x < enemy_x:
                    player_x -= knockback_distance
                    if player_x < 0:
                        player_x = 0
                else:
                    player_x += knockback_distance
                    if player_x > WIDTH - player_width:
                        player_x = WIDTH - player_width


def ai_behavior(player_attacking):
    global enemy_x, enemy_y

    # Distance from player
    dx = enemy_x - player_x
    dy = enemy_y - player_y

    # If player is attacking and close, move away from player
    if player_attacking and abs(dx) < 150 and abs(dy) < 100:
        # Move enemy away from player
        if dx < 0 and enemy_x > 0:
            enemy_x -= enemy_speed
        elif dx > 0 and enemy_x < WIDTH - enemy_width:
            enemy_x += enemy_speed

        if dy < 0 and enemy_y > 0:
            enemy_y -= enemy_speed
        elif dy > 0 and enemy_y < HEIGHT - enemy_height:
            enemy_y += enemy_speed
    else:
        # Otherwise, move towards player
        if enemy_x > player_x:
            enemy_x -= enemy_speed
        elif enemy_x < player_x:
            enemy_x += enemy_speed
        if enemy_y > player_y:
            enemy_y -= enemy_speed
        elif enemy_y < player_y:
            enemy_y += enemy_speed


def enemy_should_block():
    # AI randomly decides to block (30% chance)
    return random.random() < 0.3


def game_loop():
    global player_x, player_y, player_health, enemy_x, enemy_y, enemy_health, running
    global special_cooldown, player_special, sword_attack_rect, attacking, facing_left

    player_x, player_y = 100, HEIGHT - player_height - 50
    enemy_x, enemy_y = WIDTH - 150, HEIGHT - enemy_height - 50
    special_cooldown = 0
    player_special = False
    attacking = False
    sword_attack_rect = pygame.Rect(0, 0, 0, 0)
    facing_left = False
    enemy_blocking = False  # Track if AI is currently blocking

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Player movement & facing
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
            facing_left = True
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed
            facing_left = False
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
            player_y += player_speed

        # Detect if player is attacking this frame
        player_attacking = keys[pygame.K_SPACE]

        # Player attack logic
        global enemy_health
        if player_attacking and not attacking:
            attacking = True
            if facing_left:
                sword_attack_rect = pygame.Rect(player_x - 30, player_y + player_height // 2 - 5, 30, 10)
            else:
                sword_attack_rect = pygame.Rect(player_x + player_width, player_y + player_height // 2 - 5, 30, 10)

            enemy_hitbox = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
            if sword_attack_rect.colliderect(enemy_hitbox):
                enemy_health -= player_attack_power
                # Knockback enemy
                if facing_left:
                    enemy_x -= knockback_distance
                    if enemy_x < 0:
                        enemy_x = 0
                else:
                    enemy_x += knockback_distance
                    if enemy_x > WIDTH - enemy_width:
                        enemy_x = WIDTH - enemy_width
        else:
            attacking = False

        # Player block
        blocking = player_block(keys)

        # Player special ability
        player_special_ability(keys)

        # AI decides if it should block this frame
        enemy_blocking = enemy_should_block()

        # AI behavior: move away if player attacking and close, else move toward player
        ai_behavior(player_attacking)

        # Enemy attack logic
        melee_range = 60
        dx = abs(player_x - enemy_x)
        dy = abs(player_y - enemy_y)

        if dx < melee_range and dy < melee_range:
            if random.random() < 0.05:
                if not blocking and not enemy_blocking:
                    player_health -= enemy_attack_power
                    # Knockback player
                    if player_x < enemy_x:
                        player_x -= knockback_distance
                        if player_x < 0:
                            player_x = 0
                    else:
                        player_x += knockback_distance
                        if player_x > WIDTH - player_width:
                            player_x = WIDTH - player_width
                else:
                    # If enemy blocking, reduce damage by half or negate it
                    # (For simplicity, let's reduce by half)
                    player_health -= enemy_attack_power // 2

        # Handle special ability (power slash)
        if player_special:
            enemy_health -= 50
            player_special = False

        # Draw everything
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

        if attacking:
            pygame.draw.rect(screen, YELLOW, sword_attack_rect)

        # Draw block visual for enemy (a simple blue overlay when blocking)
        if enemy_blocking:
            block_overlay = pygame.Surface((enemy_width, enemy_height), pygame.SRCALPHA)
            block_overlay.fill((0, 0, 255, 100))  # semi-transparent blue
            screen.blit(block_overlay, (enemy_x, enemy_y))

        if player_special:
            pygame.draw.circle(screen, YELLOW, (player_x + player_width // 2, player_y), 40, 2)

        display_text(f"Player Health: {player_health}", BLACK, 20, 20)
        display_text(f"Enemy Health: {enemy_health}", BLACK, WIDTH - 200, 20)
        display_text(f"Special Ability Cooldown: {special_cooldown // 60}s", BLACK, WIDTH - 300, HEIGHT - 30)

        if special_cooldown > 0:
            special_cooldown -= 1

        if player_health <= 0:
            display_text("GAME OVER!", RED, WIDTH // 2 - 100, HEIGHT // 2)
            pygame.display.update()
            pygame.time.wait(2000)
            break

        if enemy_health <= 0:
            display_text("YOU WIN!", BLUE, WIDTH // 2 - 100, HEIGHT // 2)
            pygame.display.update()
            pygame.time.wait(2000)
            break

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
