import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Animated Word")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 36)

# Define the word and its initial position
word_text = "คุณเป็นเกย์หรือเปล่า?"
word_surface = font.render(word_text, True, WHITE)
word_rect = word_surface.get_rect()
word_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

velocity = [1, 0]  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    word_rect.move_ip(velocity)

    if word_rect.right > SCREEN_WIDTH:
        word_rect.left = 0

    screen.fill(BLACK)

    screen.blit(word_surface, word_rect)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
