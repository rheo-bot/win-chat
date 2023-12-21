import pygame
import sys

pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Subtitle Example")

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Helper function to display text on the screen


def display_text(text):
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect(
        center=(screen_width // 2, screen_height - 50))
    screen.blit(text_surface, text_rect)


# Main loop
running = True
subtitle_text = "HELLO???"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    # Display your subtitles
    display_text(subtitle_text)

    pygame.display.flip()

    pygame.time.Clock().tick(30)  # Adjust the frame rate as needed

pygame.quit()
sys.exit()
