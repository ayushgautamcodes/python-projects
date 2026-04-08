import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird - Python")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 00)
BLUE = (135, 206, 235)
RED = (255, 0, 0)

# Bird
bird_x = 50
bird_y = 200
bird_radius = 15
gravity = 0.5
bird_movement = 0
jump_strength = -8

# Pipes
pipe_width = 60
pipe_gap = 150
pipe_speed = 3
pipes = []

def create_pipe():
    height = random.randint(100, 400)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom_pipe = pygame.Rect(
        WIDTH, height + pipe_gap, pipe_width, HEIGHT
    )
    return top_pipe, bottom_pipe

pipes.extend(create_pipe())

# Score
score = 0
font = pygame.font.SysFont(None, 40)

def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def check_collision(pipes):
    for pipe in pipes:
        if pipe.collidepoint(bird_x, bird_y):
            return True
    if bird_y <= 0 or bird_y >= HEIGHT:
        return True
    return False

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = jump_strength

    # Bird physics
    bird_movement += gravity
    bird_y += bird_movement

    # Draw bird
    pygame.draw.circle(screen, RED, (bird_x, int(bird_y)), bird_radius)

    # Pipes movement
    for pipe in pipes:
        pipe.x -= pipe_speed
        pygame.draw.rect(screen, GREEN, pipe)

    # Add new pipes
    if pipes[0].x < -pipe_width:
        pipes.pop(0)
        pipes.pop(0)
        pipes.extend(create_pipe())
        score += 1

    # Collision
    if check_collision(pipes):
        running = False

    draw_score()
    pygame.display.update()

pygame.quit()
