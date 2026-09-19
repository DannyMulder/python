import pygame
import classes
pygame.init()

SCREEN = pygame.display.set_mode((500, 750))
CLOCK = pygame.time.Clock()
GREEN = (0, 255, 0)

PLAYER1 = classes.Player((50, 650, 50, 50), SCREEN)
PLAYER2 = classes.Player((400, 650, 50, 50), SCREEN)

running = True
while running:
    deltaTime = CLOCK.tick(60) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            print("W")
        elif keys[pygame.K_a]:
            print("A")
        elif keys[pygame.K_s]:
            print("S")
        elif keys[pygame.K_d]:
            print("D")
            
            
    SCREEN.fill((0, 0, 0))
    PLAYER1.drawPlayer()
    PLAYER2.drawPlayer()
    pygame.display.flip()
    CLOCK.tick(60)
pygame.quit()