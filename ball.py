import pygame
import random

class Ball:
    def __init__(self, color, size_x, size_y, speed_x, pos_x, pos_y, size_screen):
        # Initialize ball properties
        self.color = color
        self.size_x = size_x
        self.size_y = size_y
        self.speed_x = speed_x
        self.speed_y = random.randrange(-3, 3)  # Randomize initial vertical speed
        self.reset_speed = (self.speed_x, self.speed_y)  # Store initial speed for resetting
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_screen = size_screen
        self.Rect = pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y)  # Create a rectangle for collision detection

    def draw(self, screen):
        # Draw the ball on the screen
        pygame.draw.rect(screen, self.color, self.Rect)

    def check_border(self):
        # Check if the ball hits the top or bottom border and reverse its vertical speed
        if self.pos_y >= self.size_screen[1] - self.size_y or self.pos_y <= 0:
            self.speed_y *= -1

    def check_out(self, player1_score, player2_score):
        # Check if the ball goes out of bounds and update scores accordingly
        if self.pos_x < 0 - self.size_x:  # If ball goes past left side
            player1_score += 1  # Increment player 1's score
            self.reset_position_and_speed()  # Reset ball position and speed
        elif self.pos_x > self.size_screen[0]:  # If ball goes past right side
            player2_score += 1  # Increment player 2's score
            self.reset_position_and_speed()  # Reset ball position and speed

        return player1_score, player2_score

    def rebound(self, player):
        # Change ball direction when it collides with a player
        self.speed_x = -self.speed_x  # Reverse horizontal direction

        # Calculate vertical speed based on where the ball hits the player
        alignment = (player.Rect.top + (player.Rect.height / 2)) - (self.Rect.top + (self.Rect.height / 2))
        self.speed_y = int(alignment // 40) * -1  # Adjust vertical speed based on collision point

    def move(self, player1, player2):
        # Move the ball and handle collisions with players
        if self.Rect.colliderect(player1.Rect):  # If ball collides with player 1
            self.rebound(player1)  # Change ball direction based on collision
        if self.Rect.colliderect(player2.Rect):  # If ball collides with player 2
            self.rebound(player2)  # Change ball direction based on collision

        # Update ball position
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        # Check for collision with top or bottom borders
        self.check_border()

        # Update the rectangle position for collision detection
        self.Rect.topleft = (self.pos_x, self.pos_y)

    def reset_position_and_speed(self):
        # Reset ball position and speed to initial values
        self.pos_x = self.size_screen[0] // 2 - self.size_x // 2
        self.pos_y = self.size_screen[1] // 2 - self.size_y // 2
        self.speed_x, self.speed_y = self.reset_speed[:]  # Reset speed to initial values
