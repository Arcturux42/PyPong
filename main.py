import pygame
from player import Player
from ball import Ball

# Define the screen colors and size
colors = {"blue": (26, 58, 110), "white": (255, 255, 255)}
size = (1280, 720)

# Initialiser Pygame
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
running = True

# Initialize Pygame
player1 = Player(colors["white"], 25, 140, 3.5, 30, (size[1]//2)-70, size)
player2 = Player(colors["white"], 25, 140, 3.5, size[0]-(30+25), (size[1]//2)-70, size)
ball = Ball(colors["white"], 20, 20, 3, (size[0]//2)-10, (size[1]//2)-10, size)

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Fill the screen with the background color
    screen.fill(colors["blue"])

    # Draw and update player 1
    player1.draw(screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        player1.move_player(-1)
    elif keys[pygame.K_x]:
        player1.move_player(1)
    player1.update_score(screen, 1, colors["white"])

    # Draw and update player 2
    player2.draw(screen)
    if keys[pygame.K_UP]:
        player2.move_player(-1)
    elif keys[pygame.K_DOWN]:
        player2.move_player(1)
    player2.update_score(screen, -1, colors["white"])

    # Update scores based on ball position
    player1.score, player2.score = ball.check_out(player1.score, player2.score)

    # Move and draw the ball
    ball.move(player1, player2)
    ball.draw(screen)

    # Update display
    pygame.display.update()

    # Control the speed of the main loop
    clock.tick(120)

# Quit Pygame
pygame.quit()