import pygame

class Player:
    def __init__(self, color, size_x, size_y, speed, pos_x, pos_y, size_screen, score=0):
        self.color = color
        self.size_x = size_x
        self.size_y = size_y
        self.speed = speed
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_screen = size_screen
        self.Rect = pygame.Rect(pos_x, pos_y, size_x, size_y)
        self.score = score
        self.font = pygame.font.Font(None, 200)

    def draw(self, screen):
        """Draw the player on the screen."""
        pygame.draw.rect(screen, self.color, self.Rect)

    def check_border(self):
        """Ensure the player stays within the screen borders."""
        if self.pos_y < 0:
            self.pos_y = 0
        elif self.pos_y > self.size_screen[1] - self.size_y:
            self.pos_y = self.size_screen[1] - self.size_y

    def move_player(self, direction):
        """Move the player in the given direction."""
        self.pos_y += self.speed * direction
        self.check_border()
        self.Rect.topleft = (self.pos_x, self.pos_y)

    def update_score(self, screen, side, color_score):
        """Update and display the player's score on the screen."""
        score_text = self.font.render(str(self.score), True, color_score)
        text_width = score_text.get_width()
        screen.blit(score_text, (self.size_screen[0]//2 - (300 * side + text_width // 2), self.size_screen[1]//2 - text_width // 2))