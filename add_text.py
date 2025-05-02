import pygame

#   --- any text be added
def draw_text(screen, text, text_col, x, y):
    font = pygame.font.SysFont("Stencil", 30)
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# calcutes how far back it need to go to make it look centered
def middle(text,screen_width):
        text_width, text_height = pygame.font.SysFont("Stencil", 30).size(text) 
        center = (screen_width - text_width) // 2
        return center