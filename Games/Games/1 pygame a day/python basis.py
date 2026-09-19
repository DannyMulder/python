import pygame
pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
CLOCK = pygame.time.Clock()

running = True
while running:
    CLOCK.tick(60) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    SCREEN.fill((30, 20, 50))
    pygame.display.flip()
pygame.quit()