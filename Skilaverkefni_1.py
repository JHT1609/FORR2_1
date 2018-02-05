import pygame

pygame.init()

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

pygame.display.set_caption('FOR3G3U')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

y_position = 30

window.fill(BLACK)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
        if y_position != 420:
            y_position += .5
    if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
        if y_position != 0:
            y_position -= .5


    pygame.draw.rect(window, WHITE, pygame.Rect(30, y_position, 20, 60))

    pygame.display.update()
    window.fill(BLACK)

pygame.quit()