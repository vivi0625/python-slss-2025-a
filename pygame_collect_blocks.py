# Collect Blocks
# Author: Vivian Liang
# 7 January 2026

import pygame
import random
from pygame import mixer

# COLOURS
RED   = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 1280
HEIGHT = 800

pygame.mixer.init()

# background
background_image = pygame.image.load(
    "assests/cartoonish-super-mario-landscape-mushrooms-waves-vibrant-stylized-digital-illustration-super-mario-themed-404916342.webp"
)
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


#star block
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            "assests/New_Super_Mario_Bros._U_Deluxe_Super_Star.webp"
        ).convert_alpha()
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.point_value = 1

    def update(self):
        pass

    def level_up(self, val):
        self.point_value *= val


#mushroom block
class DeadlyMushroom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assests/SMP_Poison_Mushroom.webp")

        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)


#powerup block
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assests/QuestionBlock3DWorld.webp")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)

        self.type = random.choice(["health", "speed"])


#player mario block
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image_right = pygame.image.load("assests/mario-snes.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image = self.image_right
        self.rect = self.image.get_rect()

        self.previous_x = 0
        self.health = 100
        self.points = 0
        self.speed_multiplier = 1.0

    def calc_damage(self, amt):
        self.health -= amt

    def incr_score(self, amt):
        self.points += amt

    def get_damage_percentage(self):
        return self.health / 100

    def update(self):
        mx, my = pygame.mouse.get_pos()
        self.rect.centerx += (mx - self.rect.centerx) * 0.2 * self.speed_multiplier
        self.rect.centery += (my - self.rect.centery) * 0.2 * self.speed_multiplier

        if self.previous_x < self.rect.x:
            self.image = self.image_right
        elif self.previous_x > self.rect.x:
            self.image = self.image_left

        self.previous_x = self.rect.x


#enemy block
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assests/goomba-nes.png")
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.damage = 1

        self.image = pygame.transform.scale(self.image, (35, 35))


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def level_up(self):
        self.damage *= 4


#health bar
class HealthBar(pygame.Surface):
    def __init__(self, width, height):
        self._width = width
        self._height = height
        super().__init__((width, height))
        self.fill(RED)

    def update_info(self, percentage):
        self.fill(RED)
        pygame.draw.rect(self, GREEN, (0, 0, percentage * self._width, self._height))


#game
def game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mario Danger Blocks")

    clock = pygame.time.Clock()
    done = False

    level = 1
    num_blocks = 100
    num_enemies = 10

    health_bar = HealthBar(200, 10)

    all_sprites = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    powerup_group = pygame.sprite.Group()
    deadly_mushroom_group = pygame.sprite.Group()

    # Enemies
    for _ in range(num_enemies):
        enemy = Enemy()
        enemy.vel_x = random.choice([-5, -3, -1, 1, 3, 5])
        enemy.vel_y = random.choice([-5, -3, -1, 1, 3, 5])
        enemy.rect.center = (WIDTH // 2, HEIGHT // 2)
        all_sprites.add(enemy)
        enemy_group.add(enemy)

    # Blocks
    for _ in range(num_blocks):
        block = Block()
        all_sprites.add(block)
        block_group.add(block)

    # Player
    player = Mario()
    player.rect.center = (WIDTH // 2, HEIGHT // 2)
    all_sprites.add(player)

    # MAIN LOOP
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        all_sprites.update()

        # Enemy bounce
        for enemy in enemy_group:
            if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
                enemy.vel_x *= -1
            if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
                enemy.vel_y *= -1

        # Collect blocks
        for block in pygame.sprite.spritecollide(player, block_group, True):
            player.incr_score(block.point_value)

        # Power-ups
        for p in pygame.sprite.spritecollide(player, powerup_group, True):
            if p.type == "health":
                player.health = min(100, player.health + 25)
            else:
                player.speed_multiplier = min(2.0, player.speed_multiplier + 0.3)

        # DEADLY MUSHROOM COLLISION (GAME OVER)
        if pygame.sprite.spritecollide(player, deadly_mushroom_group, False):
            print("☠️ Mario touched a deadly mushroom!")
            done = True

        # Rare power-up spawn
        if random.randint(1, 600) == 1 and len(powerup_group) < 5:
            p = PowerUp()
            all_sprites.add(p)
            powerup_group.add(p)

        # VERY RARE deadly mushroom spawn
        if random.randint(1, 900) == 1 and len(deadly_mushroom_group) < 2:
            m = DeadlyMushroom()
            all_sprites.add(m)
            deadly_mushroom_group.add(m)

        # Level up
        if not block_group:
            level += 1
            for _ in range(num_blocks):
                block = Block()
                block.level_up(level)
                all_sprites.add(block)
                block_group.add(block)

            enemy = Enemy()
            enemy.vel_x = random.choice([-5, -3, -1, 1, 3, 5])
            enemy.vel_y = random.choice([-5, -3, -1, 1, 3, 5])
            enemy.rect.center = (WIDTH // 2, HEIGHT // 2)
            all_sprites.add(enemy)
            enemy_group.add(enemy)

            for enemy in enemy_group:
                enemy.level_up()

        # Enemy damage
        for enemy in pygame.sprite.spritecollide(player, enemy_group, False):
            player.calc_damage(enemy.damage)

        health_bar.update_info(player.get_damage_percentage())

        if player.health <= 0:
            done = True

        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        screen.blit(health_bar, (10, 10))
        pygame.display.flip()
        clock.tick(60)

    print("Game Over")
    print("Final score:", player.points)
    pygame.quit()


if __name__ == "__main__":
    game()
