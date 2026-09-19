import pygame, sys, random, os
import space_invaders_shop

"""
-----------------------------------------------------
 SPACE INVADERS - TWEE SPELERS
-----------------------------------------------------
Dit spel is een eenvoudige 2-player versie van Space Invaders.
Beide spelers besturen een ruimteschip, kunnen schieten en
krijgen punten door vijanden te vernietigen.

Er zijn meerdere soorten vijanden (hart, gb, pou),
en nieuwe waves worden moeilijker.

Ideeën in de toekomst:
- Punten gebruiken in een shop - gedaan
- Nieuwe vijandsoorten toevoegen - gedaan
- Power-ups implementeren - gedaan
- Meer Power-ups implementeren - nog doen
-----------------------------------------------------
"""

pygame.init()
pygame.key.set_repeat(0)

font = pygame.font.Font(None, 36)
font_big = pygame.font.Font(None, 100)
screen = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Space invaders")

screen.fill((200, 200, 200))
pygame.display.flip()

klok = pygame.time.Clock()

spel = True
status = "menu" # daarna "game"
score = 0

"""
Kleuren die vaak worden gebruikt in het spel
(makkelijker te herkennen en aan te passen)
"""
rood = (255, 0, 0)
groen = (0, 255, 0)
blauw = (0, 0, 255)
zwart = (0, 0, 0)
grijs = (200, 200, 200)
wit = (255, 255, 255)

"""
Speler 1 eigenschappen
(x, y, snelheid, status, score)
"""
speler1_x = 275
speler1_y = 650
player1_alive = True
score1 = 0
score1_verdubbel = 1
player1_lifes = 3
speler1_x_snelheid = 0
speler1_y_snelheid = 0

"""
Speler 2 eigenschappen
(werkt hetzelfde als speler 1)
"""
speler2_x = 175
speler2_y = 650
player2_alive = True
score2 = 0
score2_verdubbel = 1
player2_lifes = 3
speler2_x_snelheid = 0
speler2_y_snelheid = 0

"""
Afbeeldingen van spelerschepen
(opgesneden uit spritesheets)
"""
speler1_ruimteschip = 0
speler2_ruimteschip = 0

ship_sheet1 = pygame.image.load("C:/Users/Computer/Downloads/shipmain.png").convert_alpha()
speler1_afbeelding = ship_sheet1.subsurface(pygame.Rect(speler1_ruimteschip, 0, 1024, 1024))
speler1_afbeelding = pygame.transform.scale(speler1_afbeelding, (50, 50))

ship_sheet2 = pygame.image.load("C:/Users/Computer/Downloads/shipmain.png").convert_alpha()
speler2_afbeelding = ship_sheet2.subsurface(pygame.Rect(speler2_ruimteschip, 0, 1024, 1024))
speler2_afbeelding = pygame.transform.scale(speler2_afbeelding, (50, 50))

"""Afbeelding van de speler_hartjes"""
levens_sheet = pygame.image.load("C:/Users/Computer/Downloads/hart-spaceinv.png").convert_alpha()
speler_levens_afbeelding = levens_sheet.subsurface(pygame.Rect(0, 0, 1024, 1024))
speler_levens_afbeelding = pygame.transform.scale(speler_levens_afbeelding, (50, 50))

"""
Kogels van spelers
Elke speler heeft zijn eigen lijst met actieve kogels
"""
speler2_kogel_x = speler2_x + 22.5
kogel_breedte = 5
kogel_hoogte = 10
speler1_schieten = False
speler2_schieten = False
player1_firerate = 30
player2_firerate = 30
kogel_timer = 0
player1_kogels = []
player2_kogels = []
player1_laser = []
player2_laser = []
speler1_laser_gekocht = 0
speler2_laser_gekocht = 0
hart_alien_kogels = []

"""
Enemy instellingen en timers
(hart-, gb-, en pou-aliens worden later geactiveerd)
"""
enemy_drop_speed = 1
enemy_move_speed = 1
spawn_snelheid_hart = 100
spawn_snelheid_gb = 300
spawn_snelheid_pou = 500
enemy_timer_hart = 0
enemy_timer_pg = 0
enemy_timer_pou = 0
Hart_aliens = []
gb_aliens = []
pou_aliens = []
gb_aliens_active = False
pou_aliens_active = False

"""
Wave-systeem:
Elke wave verhoogt het aantal vijanden
en verlaagt de spawn-tijden, zodat het moeilijker wordt
"""
wave = 0
aantal_enemies = 5
wave_requirements = 10

"""
Shop-variabele
(Wordt later gebruikt om upgrades te kopen)
"""
shop = False
shop_requirements = 4
selected1 = 0
selected2 = 0
gekocht1 = False
gekocht2 = False

"""
Vijand-afbeeldingen (worden geschaald)
"""
hart_sheet = pygame.image.load("C:/Users/Computer/Downloads/hart-alien.png").convert_alpha()
hart_alien_afbeelding = hart_sheet.subsurface(pygame.Rect(0, 0, 1024, 1024))
hart_alien_afbeelding = pygame.transform.scale(hart_alien_afbeelding, (50, 50))

gb_sheet = pygame.image.load("C:/Users/Computer/Downloads/gb-alien.png").convert_alpha()
gb_alien_afbeelding = gb_sheet.subsurface(pygame.Rect(0, 0, 1024, 1024))
gb_alien_afbeelding = pygame.transform.scale(gb_alien_afbeelding, (50, 50))

pou_sheet = pygame.image.load("C:/Users/Computer/Downloads/pou-alien.png").convert_alpha()
pou_alien_afbeelding = pou_sheet.subsurface(pygame.Rect(0, 0, 1024, 1024))
pou_alien_afbeelding = pygame.transform.scale(pou_alien_afbeelding, (50, 50))

"""
-----------------------------------------------------
 FUNCTIES
-----------------------------------------------------
Hieronder staan de functies voor besturing, schieten,
botsingen, beweging van vijanden, enzovoort.
-----------------------------------------------------
"""

def Keybinds():
    """
    Controleert welke toetsen worden ingedrukt
    en past de snelheid van de spelers aan.
    Beide spelers kunnen onafhankelijk bewegen.
    """
    global speler1_x_snelheid, speler1_y_snelheid, speler2_x_snelheid, speler2_y_snelheid, speler1_schieten, speler2_schieten
    if status == "game" and spel and not shop:
        keys = pygame.key.get_pressed()
        
        # speler 1
        if player1_alive:
            speler1_x_snelheid = 0
            speler1_y_snelheid = 0
            if keys[pygame.K_LEFT]:
                speler1_x_snelheid = -2.5 if speler1_laser_gekocht == 2 else -5
            elif keys[pygame.K_RIGHT]:
                speler1_x_snelheid = 2.5 if speler1_laser_gekocht == 2 else 5
            if keys[pygame.K_UP]:
                speler1_y_snelheid = -5
            elif keys[pygame.K_DOWN]:
                speler1_y_snelheid = 5
            speler1_schieten = keys[pygame.K_RSHIFT]
        else: speler1_schieten = False

        # speler 2
        if player2_alive:
            speler2_x_snelheid = 0
            speler2_y_snelheid = 0  
            if keys[pygame.K_a]:
                speler2_x_snelheid = -2.5 if speler2_laser_gekocht == 2 else -5
            elif keys[pygame.K_d]:
                speler2_x_snelheid = 2.5 if speler2_laser_gekocht == 2 else 5
            if keys[pygame.K_w]:
                speler2_y_snelheid = -5
            elif keys[pygame.K_s]:
                speler2_y_snelheid = 5
            speler2_schieten = keys[pygame.K_q]
        else: speler2_schieten = False

def Speler_schieten(ruimteschip, schieten, firerate, recoil, lijst, lijst_laser, x, y):
    """
    Laat spelers schieten met een kleine cooldown via kogel_timer.
    Wisselt tussen linker en rechter kanon voor een mooi effect.
    """
    global kogel_timer
    if schieten and spel and not shop:
        if ruimteschip == 0 and kogel_timer % (firerate * 2) == 0:
            lijst.append([x + 23.75, y + 20])
        elif ruimteschip == 1024 and kogel_timer % firerate == 0:
            if kogel_timer // (firerate + 5) % 2 == 0:
                lijst.append([x + 17.5, y + 20])
            else:
                lijst.append([x + 30, y + 20])
        elif ruimteschip == 2048 and kogel_timer % 10:
            lijst_laser.clear()
            lijst_laser.append([x + 22.5, y - 80])
            recoil += 0.5
    else: lijst_laser.clear()
    return recoil
            

def Boundries(x, y):       
    """
    Zorgt dat spelers niet buiten het scherm vliegen.
    """
    if x <= 0:
        x = 0
    elif x >= 450:
        x = 450
        
    if y <= 0:
        y = 0   
    elif y >= 700:
        y = 700
    
    return x, y

def Hitboxes(enemie_lijst):
    global player1_kogels, player2_kogels, hart_alien_kogels
    global speler1_x, speler1_y
    global speler2_x, speler2_y
    global score, score1, score2
    global player1_alive, player2_alive, player1_lifes, player2_lifes
    global spel

    player1 = pygame.Rect(speler1_x, speler1_y, 50, 50)
    player2 = pygame.Rect(speler2_x, speler2_y, 50, 50)

    to_remove = []  # vijanden die verwijderd moeten worden

    for e in enemie_lijst:
        enemie_rect = pygame.Rect(e[0], e[1], 50, 50)

        # Kogels van speler 1
        for k in player1_kogels[:]:
            if enemie_rect.colliderect(pygame.Rect(k[0], k[1], 5, 10)):
                player1_kogels.remove(k)
                e[2] -= 1
                score += 1
                score1 += 1

        # Kogels van speler 2
        for k in player2_kogels[:]:
            if enemie_rect.colliderect(pygame.Rect(k[0], k[1], 5, 10)):
                player2_kogels.remove(k)
                e[2] -= 1
                score += 1
                score2 += 1

        # Lasers
        for l in player1_laser[:]:
            if enemie_rect.colliderect(pygame.Rect(l[0], l[1], 20, 250)):
                player1_laser.clear()
                e[2] -= 1
                score += 1
                score1 += 1

        for l in player2_laser[:]:
            if enemie_rect.colliderect(pygame.Rect(l[0], l[1], 20, 250)):
                player2_laser.clear()
                e[2] -= 1
                score += 1
                score2 += 1
                
        # Vijandkogels raken speler
        for k in hart_alien_kogels[:]:
            hart_alien_kogel_rect = pygame.Rect(k[0], k[1], 5, 10)
            if player1.colliderect(hart_alien_kogel_rect) and player1_alive:
                player1_lifes -= 1
                hart_alien_kogels.remove(k)
            elif player2.colliderect(hart_alien_kogel_rect) and player2_alive:
                player2_lifes -= 1
                hart_alien_kogels.remove(k)
                
        # Vijand raakt speler
        if enemie_rect.colliderect(player1) and player1_alive:
            player1_lifes -= 1
            to_remove.append(e)
        elif enemie_rect.colliderect(player2) and player2_alive:
            player2_lifes -= 1
            to_remove.append(e)
        for k in hart_alien_kogels[:]:
            hart_alien_kogel_rect = pygame.Rect(k[0], k[1], 5, 10)
            for l in player1_laser:
                if hart_alien_kogel_rect.colliderect(pygame.Rect(l[0], l[1], 20, 100)):
                    hart_alien_kogels.remove(k)
            for l in player2_laser:
                if hart_alien_kogel_rect.colliderect(pygame.Rect(l[0], l[1], 20, 100)):
                    hart_alien_kogels.remove(k)
            
        if e[1] >= 750 or e[2] <= 0:
            to_remove.append(e)

    # Verwijder alle vijanden pas na de loop
    for e in to_remove:
        if e in enemie_lijst:
            enemie_lijst.remove(e)
            
    if shop:
        for e in enemie_lijst:
            enemie_lijst.remove(e)

    player1_alive = player1_lifes > 0
    player2_alive = player2_lifes > 0
    if not player1_alive and not player2_alive:
        spel = False

def Enemy_kogels(enemy_lijst, lijst):
    """
    Laat vijanden af en toe schieten.
    Kans per frame: 1 op 400.
    """
    if spel and not shop:
        for e in enemy_lijst:
            if random.randint(1, 750) == 1:
                lijst.append([e[0]+23, e[1]+35])
        for k in lijst[:]:
            k[1] += 2
            if k[1] > 750:
                lijst.remove(k)
    elif shop and lijst:
        lijst.pop()    
                
def totaal_enemies():
    """
    Telt het totaal aantal actieve vijanden van alle types.
    """
    return len(Hart_aliens) + len(gb_aliens) + len(pou_aliens)
                
def Enemy_append_movement(enemy_lijst, active, timer, spawn_snelheid):
    if status == "game" and spel and not shop:
        enemy_hp = 3 if enemy_lijst is pou_aliens else 1
        if timer >= spawn_snelheid and totaal_enemies() < aantal_enemies and active:
            timer = 0
            spawn = random.randrange(1, 10)
            enemy_x = 50 * spawn
            enemy_y = -50
            enemy_lijst.append([enemy_x, enemy_y, enemy_hp, 1])
        else:
            timer += 1

    if spel and not shop:
        for e in enemy_lijst:
            if enemy_lijst is gb_aliens:
                e[1] += 4
            elif enemy_lijst is pou_aliens:
                e[1] += 0.5
            else:
                e[1] += 1
                
        for e in enemy_lijst:
            if enemy_lijst is pou_aliens:
                e[0] += e[3] * enemy_move_speed
                
                if e[0] <= 0 or e[0] >= 450:
                    e[3] *= -1
    return timer

def Draw_enemy(enemy_lijts, afbeelding):
    """
    Tekent elke vijand uit een lijst op het scherm.
    """
    for e in enemy_lijts:
        pygame.draw.rect(screen, grijs, (e[0], e[1], 50, 50))
        screen.blit(afbeelding, (e[0], e[1]))
        
def Display():
    global spel
    """
    Tekent alle visuele elementen afhankelijk van de status.
    - Menu: Welkomsttekst
    - Game: Spelers, kogels, vijanden, scores, levens
    """
    def Draw_player_harts(lifes, start_x, start_y):
        """
        Tekent hartjes/levens van een speler op het scherm.
        lifes: int, aantal levens van de speler
        start_x/start_y: positie van het eerste hartje
        """
        for i in range(lifes):
            x_pos = start_x + i * 60
            y_pos = start_y
            screen.blit(speler_levens_afbeelding, (x_pos, y_pos))

    if status == "menu":
        start_scherm = font.render("Welcome to space invaders", True, (255, 255, 255))
        screen.blit(start_scherm, (90, 350))
        
        press_enter = font.render("Press enter to start!", True, (255, 255, 255))
        screen.blit(press_enter, (135, 430))
        
    elif status == "game":
        if player1_alive:
            screen.blit(speler1_afbeelding, (speler1_x, speler1_y))
        if player2_alive:
            screen.blit(speler2_afbeelding, (speler2_x, speler2_y))
            
        for k in player1_kogels:
            pygame.draw.rect(screen, blauw, (k[0], k[1], 5, 10))
        for k in player2_kogels:
            pygame.draw.rect(screen, blauw, (k[0], k[1], 5, 10))
            
        for l in player1_laser:
            pygame.draw.rect(screen, blauw, (l[0], l[1], 7.5, 100))
            
        for l in player2_laser:
            pygame.draw.rect(screen, blauw, (l[0], l[1], 7.5, 100))
            
        Draw_enemy(Hart_aliens, hart_alien_afbeelding)
        Draw_enemy(gb_aliens, gb_alien_afbeelding)
        Draw_enemy(pou_aliens, pou_alien_afbeelding)
            
        for k in hart_alien_kogels:
            pygame.draw.rect(screen, rood, (k[0], k[1], 5, 10))
        
        score1_ = font.render(f"Player1 score: {score1}", True, wit)
        screen.blit(score1_, (280, 720))
            
        score_ = font.render(f"Score: {score}", True, wit)
        screen.blit(score_, (175, 10))
        
        score2_ = font.render(f"Player2 score: {score2}", True, wit)
        screen.blit(score2_, (10, 720))
        
        wave_ = font.render(f"Wave: {wave + 1}", True, wit)
        screen.blit(wave_, (10, 10))
        
    if not spel:
        game_over = font.render("Game Over!", True, zwart)
        screen.blit(game_over, (180, 360))
        
        final_score = font.render(f"Final score: {score}", True, zwart)
        screen.blit(final_score, (170, 395))

    """
    teken de hartjes van de spelers
    """
    Draw_player_harts(player1_lifes, start_x=320, start_y=670)
    Draw_player_harts(player2_lifes, start_x=10, start_y=670)
 
def Shop():     
    global shop, score1, score2, shop_requirements
    """
    Placeholder voor toekomstige winkel (nog niet actief).
    Wordt geactiveerd elke 5 waves.
    """
    keys = pygame.key.get_pressed()
    if wave == shop_requirements:
        shop = True
        pygame.draw.rect(screen, zwart, (0, 0, 500, 75)) # titel shop
        pygame.draw.rect(screen, zwart, (25, 100, 450, 200)) # item player 1
        pygame.draw.rect(screen, zwart, (25, 325, 450, 200)) # item player 2
        
        space_invaders_shop.Shop_items(speler1_laser_gekocht, selected1, speler_levens_afbeelding, player1_lifes, speler1_afbeelding, speler1_ruimteschip, 1, 35, 115)
        space_invaders_shop.Shop_items(speler2_laser_gekocht, selected2, speler_levens_afbeelding, player2_lifes, speler2_afbeelding, speler2_ruimteschip, 2, 35, 115)
                  
        shop_titel = font_big.render("shop", True, wit)
        screen.blit(shop_titel, (175, 2.5))
        
        if keys[pygame.K_RETURN]:
            shop = False
            shop_requirements += 5

def Items_kopen(verdubbel, firerate, speler_laser_gekocht, gekocht, geselecteerd, lifes, score, ruimteschip, speler_afbeelding):
    global player1_alive, player2_alive, player1_lifes, player2_lifes, score1, score2
    global speler1_x, speler2_x, speler1_y, speler2_y
    if gekocht and geselecteerd == 0 and lifes < 3 and score >= 20:
        score -= 20
        lifes += 1
    elif gekocht and gekocht is gekocht1 and geselecteerd == 1 and not player2_alive and score >= 50:
        score1 -= 50
        player2_alive = True
        player2_lifes = 3
        speler2_x = 225
        speler2_y = 650
    elif gekocht and gekocht is gekocht2 and geselecteerd == 1 and not player1_alive and score >= 50:
        score2 -= 50
        player1_alive = True
        player1_lifes = 3
        speler1_x = 225
        speler1_y = 650
    elif gekocht and geselecteerd == 2 and firerate > 15 and  score >= 10:
        score -= 10
        firerate -= 1
    elif gekocht and geselecteerd == 3 and ruimteschip <= 1024 and score >= 75 * verdubbel:
        score -= 75 * verdubbel
        ruimteschip += 1024
        verdubbel *= 2
        speler_laser_gekocht += 1
        
    gekocht = False
    speler_afbeelding = ship_sheet1.subsurface(pygame.Rect(ruimteschip, 0, 1024, 1024))
    speler_afbeelding = pygame.transform.scale(speler_afbeelding, (50, 50))
    return verdubbel, firerate, speler_laser_gekocht, gekocht, geselecteerd, lifes, score, ruimteschip, speler_afbeelding
        
"""
de shop bevat de items die je kan kopen: draw_rects voor betere gui
score1 en score2 zijn de punten die de spelers kunnen besteden
check voor toetsen voor betere navigatie

items voor in de shop:
player_gun upgrade
player_schieten_cooldown upgrade
healing upgrade
teammate_revive upgrade

vergeet de tekst niet onder te zetten: Press enter to continue!
"""

"""
-----------------------------------------------------
 HOOFDLOOP
-----------------------------------------------------
De game loopt hier continu:
- events (input)
- logica
- tekenen
-----------------------------------------------------
"""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("\nDoei!")
            pygame.quit()
            sys.exit()

        if status == "menu":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                status = "game"
                
        if shop:
            if event.type == pygame.KEYDOWN and shop:
                if player1_alive:  
                    if event.key == pygame.K_UP:
                        selected1 = min(3, selected1 + 1)
                    elif event.key == pygame.K_DOWN:
                        selected1 = max(0, selected1 - 1)
                    elif event.key == pygame.K_RSHIFT:
                        gekocht1 = True
                 
                if player2_alive: 
                    if event.key == pygame.K_w:
                        selected2 = min(3, selected2 + 1)
                    elif event.key == pygame.K_s:
                        selected2 = max(0, selected2 - 1)
                    elif event.key == pygame.K_LSHIFT:
                        gekocht2 = True
            
    score1_verdubbel, player1_firerate, speler1_laser_gekocht, gekocht1, selected1, player1_lifes, score1, speler1_ruimteschip, speler1_afbeelding = Items_kopen(score1_verdubbel, player1_firerate, speler1_laser_gekocht, gekocht1, selected1, player1_lifes, score1, speler1_ruimteschip, speler1_afbeelding)
    score2_verdubbel, player2_firerate, speler2_laser_gekocht, gekocht2, selected2, player2_lifes, score2, speler2_ruimteschip, speler2_afbeelding = Items_kopen(score2_verdubbel, player2_firerate, speler2_laser_gekocht, gekocht2, selected2, player2_lifes, score2, speler2_ruimteschip, speler2_afbeelding)

    """
    Activeer nieuwe vijandsoorten naarmate de wave stijgt.
    """
    if wave >= 4:
        gb_aliens_active = True
    if wave >= 9:
        pou_aliens_active = True
        
    """
    Timers voor het spawnen van vijanden
    """
    enemy_timer_hart += 1
    if gb_aliens_active:
        enemy_timer_pg += 1
    if pou_aliens_active:
        enemy_timer_pou += 1

    """
    Check of wave voorbij is, en verhoog moeilijkheid.
    """
    if score >= wave_requirements:
        wave += 1
        wave_requirements += 10
        if wave <= 10:
            aantal_enemies = 5 + wave
            
        spawn_snelheid_hart = max(50, spawn_snelheid_hart - 2)
        spawn_snelheid_gb = max(100, spawn_snelheid_gb - 3)
        spawn_snelheid_pou = max(150, spawn_snelheid_pou - 2)
        
    Keybinds()

    """
    Schietfuncties en spelersbeweging
    """
    kogel_timer += 1
    speler1_y_snelheid = Speler_schieten(speler1_ruimteschip, speler1_schieten, player1_firerate, speler1_y_snelheid, player1_kogels, player1_laser, speler1_x, speler1_y)
    speler2_y_snelheid = Speler_schieten(speler2_ruimteschip, speler2_schieten, player2_firerate, speler2_y_snelheid, player2_kogels, player2_laser, speler2_x, speler2_y)
    
    speler1_x, speler1_y = Boundries(speler1_x, speler1_y)
    speler2_x, speler2_y = Boundries(speler2_x, speler2_y)
    
    """
    Controleer botsingen met verschillende vijanden
    """
    Hitboxes(Hart_aliens)
    Hitboxes(gb_aliens)
    Hitboxes(pou_aliens)
    
    Enemy_kogels(Hart_aliens, hart_alien_kogels)
    
    """
    Werk spelersposities bij
    """
    if not shop:
        speler1_x += speler1_x_snelheid        
        speler1_y += speler1_y_snelheid
        
        speler2_x += speler2_x_snelheid        
        speler2_y += speler2_y_snelheid
    
    """
    Beweeg kogels omhoog en verwijder ze als ze van het scherm zijn
    """
    for k in player1_kogels[:]:
        k[1] -= 10
        if k[1] < 0:
            player1_kogels.remove(k)
    for k in player2_kogels[:]:
        k[1] -= 10
        if k[1] < -10:
            player2_kogels.remove(k) 

    enemy_timer_hart = Enemy_append_movement(Hart_aliens, True, enemy_timer_hart, spawn_snelheid_hart)
    enemy_timer_pg = Enemy_append_movement(gb_aliens, gb_aliens_active, enemy_timer_pg, spawn_snelheid_gb)
    enemy_timer_pou = Enemy_append_movement(pou_aliens, pou_aliens_active, enemy_timer_pou, spawn_snelheid_pou)
    
    screen.fill((200, 200, 200))
    Display()
    Shop()
    
    if not spel:
        base_path = os.path.dirname(os.path.abspath(__file__))
        bestand = os.path.join(base_path, "savegame.txt")

        if os.path.exists(bestand):
            with open(bestand, "r") as f:
                saved_score = int(f.read())

        highscore = font.render(f"Highscore: {saved_score}", True, zwart)
        screen.blit(highscore, (170, 430))

        if score > saved_score:
            with open(bestand, "w") as f:
                f.write(str(score))
    
    klok.tick(60)
    pygame.display.flip()