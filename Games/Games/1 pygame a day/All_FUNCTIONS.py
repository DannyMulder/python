import pygame
pygame.init()

def Player_Borders(player, width, height):
    if player.left < 0: player.left = 0
    if player.right > width: player.right = width
    if player.top < 0: player.top = 0
    if player.bottom > height: player.bottom = height
    
def Player_Hitboxes(onGround, player, lijst, dx, dy):
    for rect in lijst:
        if player.colliderect(rect):
            if dx > 0:
                player.right = rect.left
            elif dx < 0:
                player.left = rect.right
            if dy > 0:
                player.bottom = rect.top
                onGround = True
            elif dy < 0:
                player.top = rect.bottom
                dy = 0
    return onGround
                
def Player_Bullets(event, player, lijst, dx, dy, givenKey):
    if event.key == givenKey:
        if dx != 0 or dy != 0:
            lijst.append([pygame.Rect(player.x + player.width//2, player.y + player.height//2, 5, 5), dx, dy])
    return lijst

"""
    delta time prove
    
    dy += gravity * dt

    # Update X
    player_rect.x += round(dx * dt)
    onGround = All_FUNCTIONS.Player_Hitboxes(onGround, player_rect, cube, dx, 0)
    playerPos.x = player_rect.x

    # Update Y
    player_rect.y += round(dy * dt)
    onGround = All_FUNCTIONS.Player_Hitboxes(onGround, player_rect, cube, 0, dy)
    playerPos.y = player_rect.y

    # Player borders
    All_FUNCTIONS.Player_Borders(player_rect, WIDTH, HEIGHT)

    # Synchroniseer pos
    playerPos.x = player_rect.x
    playerPos.y = player_rect.y
"""