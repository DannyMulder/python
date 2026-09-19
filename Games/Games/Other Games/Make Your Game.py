import pygame
import All_FUNCTIONS as All_FUNCTIONS, os
os.environ['SDL_VIDEO_WINDOW_POS'] = "450,175"
pygame.init()

WIDTH, HEIGHT = 1000, 600
FONT = pygame.font.Font(None, 50)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

playerImage = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.rect(playerImage, (0, 255, 0), playerImage.get_rect())

player_rect = pygame.Rect(0, 550, 50, 50)
spawnPos = pygame.Vector2(0, 550)

lijst = []

dy = 0
snelheid = 250
gravity = 500
onGround = False
cubeHold = False

finish = False
player_stop_moving_NOW = False
status = "builder" # anders "game"
scaler = "width" # anders "height"

running = True
while running:
    dt = CLOCK.tick(60) / 1000
    mouse_X, mouse_Y = pygame.mouse.get_pos()
    mouseHold = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         
        if event.type == pygame.KEYDOWN and status == "builder":   
            if event.key == pygame.K_e:
                lijst.append({
                    "rect": pygame.Rect(mouse_X-25, mouse_Y-25, 50, 50),
                    "color": (0, 0, 255),
                    "collider": False,
                    "type": "blok"
                    })
            elif event.key == pygame.K_r:
                lijst.append({
                    "rect": pygame.Rect(mouse_X-25, mouse_Y-25, 50, 50),
                    "color": (255, 0, 0),
                    "collider": True,
                    "type": "trap"
                    })
            elif event.key == pygame.K_f:
                lijst.append({
                    "rect": pygame.Rect(mouse_X-25, mouse_Y-25, 50, 50),
                    "color": (200, 0, 200),
                    "collider": True,
                    "finish": False,
                    "type": "finish"
                    })
            elif event.key == pygame.K_c:
                if event.key == pygame.K_c:
                    lijst.append({
                        "rect": pygame.Rect(mouse_X - 25, mouse_Y - 25, 50, 50),
                        "color": (255, 255 , 0),
                        "radius": 25,
                        "collider": True,
                        "collected": False,
                        "type": "muntjes"
                    })
            elif event.key == pygame.K_t:
                lijst.append({
                    "rect": pygame.Rect(mouse_X-25, mouse_Y-25, 50, 50),
                    "color": (255, 165, 0),
                    "collider": True,
                    "type": "spawn"
                    })
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                if status == "game":
                    status = "builder"
                else: status = "game"
                
        for rect in lijst:
            rects = rect["rect"]
            if event.type == pygame.KEYDOWN and status == "builder":
                if event.key == pygame.K_1:
                    scaler = "width"
                elif event.key == pygame.K_2:
                    scaler = "height"
                elif rects.x <= mouse_X <= rects.x+rects.width and rects.y <= mouse_Y <= rects.y+rects.height:
                    if event.key == pygame.K_q:
                        lijst.remove(rect)
            elif event.type == pygame.MOUSEBUTTONDOWN and status == "builder":
                if rects.x <= mouse_X <= rects.x+rects.width and rects.y <= mouse_Y <= rects.y+rects.height:
                    if scaler == "width":
                        if event.button == 4:
                            rects.width -= 5
                        elif event.button == 5:
                            rects.width += 5
                    if scaler == "height":
                        if event.button == 4:
                            rects.height -= 5
                        elif event.button == 5:
                            rects.height += 5
                    
            if rects.width <= 0 or rects.height <= 0:
                lijst.remove(rect)
            
    for rect in lijst:                    
        rects = rect["rect"]

        if not cubeHold and mouseHold[0] and rects.x <= mouse_X <= rects.x+rects.width and rects.y <= mouse_Y <= rects.y+rects.height:
            rects.x = mouse_X - rects.width // 2
            rects.y = mouse_Y - rects.height // 2
            cubeHold = True
        else:
            cubeHold = False

        if rects.x <= mouse_X <= rects.x+rects.width and rects.y <= mouse_Y <= rects.y+rects.height:
            print(f"X: {rects.x}, Y: {rects.y}, WIDTH: {rects.width}, HEIGHT: {rects.height}")
            
    finish = all(rect["collected"] for rect in lijst if rect["type"] == "muntjes")
    
    for rect in lijst[:]:
        rects = rect["rect"]
        if rect["collider"] == True:
            if player_rect.colliderect(rect["rect"]) and rect["type"] == "trap":
                player_rect.x, player_rect.y = spawnPos
                dx = 0
                dy = 0
                
            if player_rect.colliderect(rect["rect"]) and rect["type"] == "muntjes":
                rect["collected"] = True
                rects.width = 0
                rects.height = 0
                
            if player_rect.colliderect(rect["rect"]) and rect["type"] == "finish":
                if finish:
                    player_stop_moving_NOW = True
                    
            if player_rect.colliderect(rect["rect"]) and rect["type"] == "spawn":
                spawnPos = rects.x, rects.y
                
            if rects.width <= 0 or rects.height <= 0:
                lijst.remove(rect)
            
    dx = 0
    keys = pygame.key.get_pressed()
    if not player_stop_moving_NOW:
        if keys[pygame.K_a]:
            dx = -snelheid
        elif keys[pygame.K_d]:
            dx = snelheid
        if keys[pygame.K_SPACE] and onGround:
            dy = -300
            onGround = False
        
        if player_rect.bottom == HEIGHT:
            onGround = True 
        if not onGround:
            dy += gravity * dt
    else: dy, dx = 0, 0

    # Update X
    player_rect.x += round(dx * dt)
    onGround = All_FUNCTIONS.Player_Hitboxes(onGround, player_rect, lijst, dx, 0)

    # Update Y
    player_rect.y += round(dy * dt)
    onGround = All_FUNCTIONS.Player_Hitboxes(onGround, player_rect, lijst, 0, dy)

    # Player borders
    All_FUNCTIONS.Player_Borders(player_rect, WIDTH, HEIGHT)

    SCREEN.fill((0, 0, 0))
    SCREEN.blit(playerImage, player_rect)
    for rect in lijst:
        if rect["type"] != "muntjes":
            pygame.draw.rect(SCREEN, rect["color"], rect["rect"])
        if rect["type"] == "muntjes":
            center = rect["rect"].center
            pygame.draw.circle(SCREEN, rect["color"], center, rect["radius"])
        if player_stop_moving_NOW:
            text = FONT.render("Level voltooid", True, (255, 255, 255))
            SCREEN.blit(text, (375, 280))
    pygame.display.flip()
pygame.quit()