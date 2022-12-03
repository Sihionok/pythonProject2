import pygame
import random

SIZE = WIDH, HEIGHT = 800, 600
SPEED = 10
FPS = 60
pygame.init()
screen = pygame.display.set_mode(SIZE)
running = True
clock = pygame.time.Clock()
x = 20
center = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            center = event.pos
            radius = 0
    screen.fill("blue")
    if center:
        pygame.draw.circle(screen, "yellow", center, 20)
    x += 20 / FPS
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()