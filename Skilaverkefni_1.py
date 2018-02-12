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

y1_position = 30
y2_position = 30
y3_position = 210
x3_position = 310

window.fill(BLACK)

running = True

'''
def event_handling_function(events):
    pass



while running:

    event_handling_function(pygame.event.get())
    
    
    def movement(y_position, down, up):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN and event.key == up:
            if y_position != 420:
                y_position += .5
        if event.type == pygame.KEYDOWN and event.key == down:
            if y_position != 0:
                y_position -= .5
'''
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
        if y1_position != 420:
            y1_position += .5
    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        if y2_position != 420:
            y2_position += .5
    if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
        if y1_position != 0:
            y1_position -= .5
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        if y2_position != 0:
            y2_position -= .5

    pygame.draw.rect(window, WHITE, pygame.Rect(30, y1_position, 20, 60))
    pygame.draw.rect(window, WHITE, pygame.Rect(590, y2_position, 20, 60))
    pygame.draw.rect(window, WHITE, pygame.Rect(x3_position, y3_position, 20, 20))

    pygame.display.update()
    window.fill(BLACK)

pygame.quit()