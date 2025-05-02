import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Movement Triangle")

# Set the initial player position
player_pos = [200, 200]  # Start in the center of the screen
speed = 200
angle = 340 # Angle in degrees

# Calculate the movement (dx, dy)
dy = math.cos(math.radians(angle)) * speed  # Vertical movement
dx = math.sin(math.radians(angle)) * speed  # Horizontal movement

# Calculate the new position for the player
new_x = player_pos[0] + dx
new_y = player_pos[1] + dy

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    # Draw the player as a small circle
    pygame.draw.circle(screen, (0, 255, 0), (int(player_pos[0]), int(player_pos[1])), 10)

    # Draw the new position (destination) of the player as a blue circle
    pygame.draw.circle(screen, (0, 0, 255), (int(new_x), int(new_y)), 10)

    # Draw the triangle representing the movement
    # Draw the lines of the triangle
    pygame.draw.line(screen, (255, 0, 0), (player_pos[0], player_pos[1]), (new_x, player_pos[1]), 2)  # Horizontal movement (dx)
    pygame.draw.line(screen, (0, 255, 0), (new_x, player_pos[1]), (new_x, new_y), 2)  # Vertical movement (dy)
    pygame.draw.line(screen, (255, 255, 0), (player_pos[0], player_pos[1]), (new_x, new_y), 2)  # Hypotenuse (speed)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()