import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Player properties
player_size = 50
player_color = black
player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Fill the screen with white
    screen.fill(white)
    
    # Draw player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))
    
    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)
