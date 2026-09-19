import pygame
pygame.init()

screen = pygame.display.set_mode((500, 750))
font = pygame.font.Font(None, 36)
wit = (255, 255, 255)

def Shop_items(laser_gekocht, selected, afbeelding_hartjes, lifes, afbeedling_spelers, ruimteschip, player, start_x, start_y):
    afbeelding_hartjes = pygame.transform.scale(afbeelding_hartjes, (150, 150))

    ruimteschip += 1024
    if ruimteschip >= 2048:
        ruimteschip = 2048
    
    ship_sheet1 = pygame.image.load("C:/Users/Computer/Downloads/shipmain.png").convert_alpha()
    afbeedling_spelers = ship_sheet1.subsurface(pygame.Rect(ruimteschip, 0, 1024, 1024))
    afbeedling_spelers = pygame.transform.scale(afbeedling_spelers, (150, 150))
    
    fire_rate_ = pygame.image.load("C:/Users/Computer/Downloads/firerate.png").convert_alpha()
    fire_rate = fire_rate_.subsurface(pygame.Rect(0, 0, 10, 15))
    fire_rate = pygame.transform.scale(fire_rate, (150, 150))
    
    revive_ = pygame.image.load("C:/Users/Computer/Downloads/revive.png").convert_alpha()
    revive = revive_.subsurface(pygame.Rect(0, 0, 10, 10))
    revive = pygame.transform.scale(revive, (150, 150))
    
    current_life = f"Current lifes: {lifes}" if lifes > 0 else f"Player is dead"
    current_spaceship = f"Buy next spaceship" if lifes > 0 else f"Player is dead"
    current_firerate = f"Buy next upgrade" if lifes > 0 else "Player is dead"
    current_revive = f"Revive" if lifes > 0 else "Player is dead"
    cost = f"Cost: 75" if ruimteschip == 1024 else "Cost: 150"
    
    if ruimteschip == 1024:
        cost = "Cost: 75"
    elif laser_gekocht == 2:
        cost = "Max level"
    else: cost = "Cost: 150"
    
    if player == 2:
        start_y += 225
        
    if selected == 0:
        screen.blit(afbeelding_hartjes, (start_x, start_y))
        
        lifes_ = font.render("Get a life back", True, wit)
        screen.blit(lifes_, (start_x + 200, start_y))
        
        momentele_levens_ = font.render(current_life, True, wit)
        screen.blit(momentele_levens_, (start_x + 200, start_y + 85))
        
        player_ = font.render(f"Player {player}", True, wit)
        screen.blit(player_, (start_x + 25, start_y))
        
        cost_ = font.render(f"Cost: 20", True, wit)
        screen.blit(cost_, (start_x + 200, start_y + 115))
        
    elif selected == 1:
        screen.blit(revive, (start_x, start_y + 20))
        
        friend_ = font.render("Revive your friend", True, wit)
        screen.blit(friend_, (start_x + 150, start_y))
        
        momentele_revive = font.render(current_revive, True, wit)
        screen.blit(momentele_revive, (start_x + 200, start_y + 85))
        
        player_ = font.render(f"Player {player}", True, wit)
        screen.blit(player_, (start_x + 25, start_y))
        
        cost_ = font.render(f"Cost: 50", True, wit)
        screen.blit(cost_, (start_x + 200, start_y + 115))
        
    elif selected == 2:
        screen.blit(fire_rate, (start_x, start_y + 20))
        
        fire_ = font.render("Upgrade your fire rate", True, wit)
        screen.blit(fire_, (start_x + 150, start_y))
        
        momentele_firerate_ = font.render(current_firerate, True, wit)
        screen.blit(momentele_firerate_, (start_x + 200, start_y + 85))
        
        player_ = font.render(f"Player {player}", True, wit)
        screen.blit(player_, (start_x + 25, start_y))
        
        cost_ = font.render(f"Cost: 10", True, wit)
        screen.blit(cost_, (start_x + 200, start_y + 115))
    
    elif selected == 3:
        screen.blit(afbeedling_spelers, (start_x, start_y + 20))
        
        ship_ = font.render("Upgrade your spaceship", True, wit)
        screen.blit(ship_, (start_x + 150, start_y))
        
        momentele_ruimteschip_ = font.render(current_spaceship, True, wit)
        screen.blit(momentele_ruimteschip_, (start_x + 200, start_y + 85))
        
        player_ = font.render(f"Player {player}", True, wit)
        screen.blit(player_, (start_x + 25, start_y))
        
        cost_ = font.render(cost, True, wit)
        screen.blit(cost_, (start_x + 200, start_y + 115))