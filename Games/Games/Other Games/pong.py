import pygame, sys

pygame.init()

font = pygame.font.Font(None, 50)
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Pong")

screen.fill((0, 0, 0))
pygame.display.flip()

klok = pygame.time.Clock()

"""Kleur"""
wit = (255, 255, 255)

"""eigenschappen van de rect"""
x = 925
y = 175
breedte = 25
hoogte = 150

y_snelheid = 0
snelheid = 10

"""eigenschappen van de rect: speler 2"""
speler2_x = 75
speler2_y = 175
speler2_breedte = 25
speler2_hoogte = 150

"""de bal"""
bal_x = 475
bal_y = 250
straal = 25

bal_y_snelheid = 2.5
bal_x_snelheid = 10

timer = 0
bal_snelheid = 1

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    speler2_y_snelheid = 0
    y_snelheid = 0
    if keys[pygame.K_UP]:
        y_snelheid -= snelheid
    if keys[pygame.K_DOWN]:
        y_snelheid += snelheid
        
    if keys[pygame.K_w]:
        speler2_y_snelheid -= snelheid
    if keys[pygame.K_s]:
        speler2_y_snelheid += snelheid
        
    timer += 1
    if timer % 100 == 0:
        bal_snelheid += 0.0025
        bal_x_snelheid *= bal_snelheid
        bal_y_snelheid *= bal_snelheid
        hoogte -= 2.5
        speler2_hoogte -= 2.5
        straal -= 0.5
        snelheid += 0.1
    
    y += y_snelheid
    speler2_y += speler2_y_snelheid
    # speler2_y = bal_y - straal * 3
    
    y = max(0, min(y, 500 - hoogte))
    speler2_y = max(0, min(speler2_y, 500 - hoogte))
    
    bal_x += bal_x_snelheid
    bal_y += bal_y_snelheid
        
    player_rect = pygame.Rect(x, y, breedte, hoogte)
    player2_rect = pygame.Rect(speler2_x, speler2_y, speler2_breedte, speler2_hoogte)
    circle_rect = pygame.Rect(bal_x - straal, bal_y - straal, straal*2, straal*2)

    if circle_rect.colliderect(player_rect) or circle_rect.colliderect(player2_rect):
        bal_x_snelheid *= -1
        score += 1
        
    if bal_y - straal <= 0:
        bal_y = straal
        bal_y_snelheid *= -1
    elif bal_y + straal >= 500:
        bal_y = 500 - straal
        bal_y_snelheid *= -1
        
    screen.fill((0, 0, 0))
    
    if bal_x - straal >= 1000:
        speler1 = font.render("speler1 heeft gewonnen!", True, wit)
        screen.blit(speler1, (300, 250))
    elif bal_x - straal <= 0:
        speler2 = font.render("speler2 heeft gewonnen!", True, wit)
        screen.blit(speler2, (300, 250))   
    else:
        score_ = font.render(f"score: {score}", True, wit)
        screen.blit(score_, (10, 10))
    
    pygame.draw.rect(screen, wit, (x, y, breedte, hoogte), 0)
    pygame.draw.rect(screen, wit, (speler2_x, speler2_y, speler2_breedte, speler2_hoogte), 0)
    pygame.draw.circle(screen, wit, (bal_x, bal_y), straal, 0)

    klok.tick(30)
    pygame.display.flip()