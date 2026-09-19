import pygame
pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("De oer game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill((0, 0, 0))
    pygame.display.flip()
    CLOCK.tick(60)
pygame.quit()