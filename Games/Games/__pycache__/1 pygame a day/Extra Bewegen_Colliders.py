import pygame
import All_FUNCTIONS
pygame.init()

WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

playerImage = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.rect(playerImage, (0, 255, 0), playerImage.get_rect())

playerPos = pygame.Vector2(0, 500)
player_rect = pygame.Rect(playerPos.x, playerPos.y, 50, 50)

level = 1

dy = 0
snelheid = 250
gravity = 350
onGround = False
isSprinting = False

running = True
while running:
    dt = CLOCK.tick(60) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dx = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        dx = -snelheid * sprint
    elif keys[pygame.K_d]:
        dx = snelheid * sprint
    if keys[pygame.K_LSHIFT]:
        isSprinting = True
    else: isSprinting = False
    if keys[pygame.K_SPACE] and onGround:
        dy = -300
        onGround = False
        
    if player_rect.bottom >= HEIGHT-1:
        player_rect.x = 0
        playerPos.y = 500
    if isSprinting:
        sprint = 1.5
    else: sprint = 1
    
    if not onGround:
        dy += gravity * dt
        
    if level == 1:
        levels = [pygame.Rect(0, 550, 50, 50), pygame.Rect(300, 500, 50, 100), pygame.Rect(750, 400, 50, 200)]
    elif level == 2:
        levels = [pygame.Rect(0, 500, 50, 100), pygame.Rect(350, 500, 50, 100), pygame.Rect(750, 400, 50, 200)]
    elif level == 3:
        levels = [pygame.Rect(0, 550, 50, 50), pygame.Rect(350, 500, 50, 100), pygame.Rect(750, 400, 50, 200)]
         
    if player_rect.colliderect(pygame.Rect(750, 350, 50, 50)):
        level += 1
        player_rect = pygame.Rect(0, 500, 50, 50)

    # Update X
    player_rect.x += round(dx * dt)
    onGround = All_FUNCTIONS.Player_Hitboxes(onGround, player_rect, levels, dx, 0)
    playerPos.x = player_rect.x

    # Update Y
    player_rect.y += round(dy * dt)
    onGround = All_FUNCTIONS.Player_Hitboxes(onGround, player_rect, levels, 0, dy)
    playerPos.y = player_rect.y

    # Player borders
    All_FUNCTIONS.Player_Borders(player_rect, WIDTH, HEIGHT)

    # Synchroniseer pos
    playerPos.x = player_rect.x
    playerPos.y = player_rect.y
            
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(playerImage, playerPos)
    for c in levels:
        pygame.draw.rect(SCREEN, (0, 0, 255), (c.x, c.y, c.width, c.height))
    pygame.display.flip()
pygame.quit()