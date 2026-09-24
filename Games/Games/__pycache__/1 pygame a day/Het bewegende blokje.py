import pygame
pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
CLOCK = pygame.time.Clock()

spelerImage = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.rect(spelerImage, (0, 255, 0), spelerImage.get_rect())
spelerPos = pygame.Vector2((300, 550))

velocity_Y = 15
gravity = 1
onGround = True

cubes = [[400, 500]]

def Border():
    if spelerPos.x <= 0:
        spelerPos.x = 0
    elif spelerPos.x >= 750:
        spelerPos.x = 750
    
    if spelerPos.y <= 0:
        spelerPos.y = 0
    elif spelerPos.y >= 550:
        spelerPos.y = 550
        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        spelerPos.x -= 5
    elif keys[pygame.K_d]:
        spelerPos.x += 5
    if keys[pygame.K_SPACE] and onGround:
        velocity_Y -= 15
        onGround = False
        
    spelerPos.y += velocity_Y
    velocity_Y += gravity
        
    if spelerPos.y >= 550:
        spelerPos.y = 550
        velocity_Y = 0
        onGround = True
        
    Border()
        
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(spelerImage, spelerPos)
    for c in cubes:
        pygame.draw.rect(SCREEN, (0, 0, 255), (c[0], c[1], 50, 100))
    pygame.display.flip()
    CLOCK.tick(60)
            
    print(velocity_Y)
pygame.quit()