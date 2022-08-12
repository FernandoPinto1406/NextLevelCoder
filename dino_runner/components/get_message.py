import pygame
FONT_STYLE = 'freesansbold.ttf'
def get_message(screen, screen_width, screen_height, what_message = str, size = int):
    font = pygame.font.Font(FONT_STYLE, size)
    text = font.render(what_message, True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = (screen_width, screen_height)
    screen.blit(text, text_rect)