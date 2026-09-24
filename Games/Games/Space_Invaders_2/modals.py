import pygame
import functions as f
import classes as c
import root as r

def MainMenu(screen, player1, player2):
    text = "Player 1 and 2 have connected - Press Enter to play" if player1 and player2 else "Player 1 has connected - Press Enter to play" if player1 else "Player 2 has connected - Press Enter to play" if player2 else "Atleast 1 player must be connected to start"
    
    screen.fill((0, 0, 0))
    screen.blit(f.CreatImageElement("IMG/mainMenu.png", r.WIDTH, r.HEIGHT), (0, 0))
    f.PlaceSurfaceObject(screen, None, 100, f.CreateTextElement(pygame.font.SysFont(None, 50), "SPACE INVADERS 2", True, r.WHITE), (0, 0, r.WIDTH, r.HEIGHT), True)
    f.PlaceSurfaceObject(screen, None, r.HEIGHT / 100 * 80, f.CreateTextElement(pygame.font.SysFont(None, 25), "Press SHIFT to join", True, r.WHITE), (0, 0, r.WIDTH, r.HEIGHT), True)
    f.PlaceSurfaceObject(screen, None, r.HEIGHT / 4 * 3, f.CreateTextElement(pygame.font.SysFont(None, 25), text, True, r.WHITE), (0, 0, r.WIDTH, r.HEIGHT), True)
    pygame.display.flip()
    
def DeathScreen(screen):
    screen.fill((0, 0, 0))
    title = f.CreateTextElement(pygame.font.SysFont(None, 75), "GAME OVER", True, r.WHITE)
    (x, _) = f.GetCenterOfObject(title.get_width(), title.get_height(), r.WIDTH, r.HEIGHT)
    screen.blit(title, (x, 100))
    title = f.CreateTextElement(pygame.font.SysFont(None, 25), "Press ENTER to restart the game", True, r.WHITE)
    (x, y) = f.GetCenterOfObject(title.get_width(), title.get_height(), r.WIDTH, r.HEIGHT)
    screen.blit(title, (x, y))
    pygame.display.flip()
    pass

def Shop(screen, players: list[c.Player]):
    screen.fill((0, 0, 0))
    
    # line (2 players)
    if len(players) == 2:
        (x, _) = f.GetCenterOfObject(r.WIDTH / 100, r.HEIGHT, r.WIDTH, r.HEIGHT)
        pygame.draw.rect(screen, r.WHITE, (x, 0, r.WIDTH / 100, r.HEIGHT))
        
    for i in range(len(players)):
        player = players[i]
        startWidth = r.WIDTH / len(players) * i
        objectWidth = r.WIDTH / len(players)
        padding = r.WIDTH / len(players) / 20
        border = int(r.WIDTH / 100)
        
        # SHOP
        shopRect = pygame.draw.rect(screen, r.WHITE, (startWidth + padding, padding, objectWidth - padding * 2, objectWidth / 2 - padding), border, border)
        f.PlaceSurfaceObject(screen, padding / 2, padding / 2, f.CreatImageElement("IMG/player.png", shopRect.width / 2 - padding, shopRect.width / 2 - padding), (shopRect.x, shopRect.y, shopRect.width, shopRect.height), True)
        
        # Stats
        for j in range(2):
            startWidth = r.WIDTH / len(players) * j
            # shopRect = pygame.draw.rect(screen, r.WHITE, (startWidth + padding, padding, r.DEFAULT_WIDTH - padding * 2, r.HEIGHT / 2 - padding * 2), border, border)
        
    pygame.display.flip()