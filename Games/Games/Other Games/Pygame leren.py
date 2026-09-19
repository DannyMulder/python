import pygame, sys, random

pygame.init()

spel = True

"""kleur"""
rood = (255, 0, 0)
groen = (0, 255, 0)
blauw = (0, 0, 255)

"""eigenschappen van een rect"""
x = 275
y = 350
breedte = 50
hoogte = 50

x_snelheid = 0
y_snelheid = 0
sprong_hoogte = 10
zwaartekracht = 1
op_grond = True

"""kogels"""
kogel_x = x + 22.5
kogel_y = y - 5
kogel_breedte = 5
kogel_hoogte = 10

kogels = []

"""enemies"""
enemy_move_speed = 1
enemy_drop_speed = 0.5

enemies = []
score = 0



font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Mijn eerste pygame")

screen.fill((100, 150, 250))
pygame.display.flip()

klok = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("\nDoei!")
            pygame.quit()
            sys.exit()
            
        if spel and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and op_grond:
                op_grond = False
                y_snelheid = -sprong_hoogte
            elif event.key == pygame.K_LEFT:
                x_snelheid = -5
            elif event.key == pygame.K_RIGHT:
                x_snelheid = 5
            elif event.key == pygame.K_SPACE:
                if len(kogels) < 3 :
                    kogels.append([x + 22.5, y - 5])
        
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                x_snelheid = 0
                
    x += x_snelheid        
    y += y_snelheid
    y_snelheid += zwaartekracht
        
    if y >= 350:
        y = 350
        y_snelheid = 0
        op_grond = True
        
    if x <= 0:
        x = 0
    elif x >= 550:
        x = 550
        
    for k in kogels[:]:
        k[1] -= 10
        if k[1] < 0:
            kogels.remove(k)
            
    if len(enemies) < 1:
        enemy_x = random.randrange(0, 550)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y, 1])
        
    for e in enemies[:]:
        if spel:
            e[1] += enemy_drop_speed
            e[0] += e[2] * enemy_move_speed
            if e[0] <= 0 or e[0] >= 550:
                e[2] *= -1

    verwijder_enemies = []
    verwijder_kogels = []
          
    for e in enemies:
        enemie_rect = pygame.Rect(e[0], e[1], breedte, hoogte)
        for k in kogels:
            kogel_rect = pygame.Rect(k[0], k[1], 5, 10)
            if enemie_rect.colliderect(kogel_rect):
                verwijder_enemies.append(e)
                verwijder_kogels.append(k)
                score += 1
                enemy_move_speed += 1
                enemy_drop_speed += 0.05
                
    for e in verwijder_enemies:
        if e in enemies:
            enemies.remove(e)

    for k in verwijder_kogels:
        if k in kogels:
            kogels.remove(k)
            
    for e in enemies:
        enemie_rect = pygame.Rect(e[0], e[1], breedte, hoogte)
        player_rect = pygame.Rect(x, y, breedte, hoogte)
        if enemie_rect.colliderect(player_rect):
            spel = False
        elif e[1] >= 350:
            spel = False
        
    screen.fill((100, 150, 250))

    pygame.draw.rect(screen, groen, (x, y, breedte, hoogte), 0)
    
    for e in enemies:
        pygame.draw.rect(screen, rood, (e[0], e[1], breedte, hoogte))
    
    for k in kogels:
        pygame.draw.rect(screen, blauw, (k[0], k[1], 5, 10))
        
    aantal_kogels = font.render(f"kogels: {3 - len(kogels)}", True, (0, 0, 0))
    screen.blit(aantal_kogels, (10, 370))
    totale_score = font.render(f"score: {score}", True, (0, 0, 0))
    screen.blit(totale_score, (490, 370))
    
    if not spel:
        death = font.render("Je hebt verloren!", True, (0, 0, 0))
        screen.blit(death, (200, 200))
        
    klok.tick(30)
    pygame.display.flip()