import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
os.environ['SDL_VIDEO_CENTERED'] = '1'
import pygame
import classes as c
import functions as f
import modals as m
import root as r
pygame.init()
pygame.key.set_repeat(0)

SCREEN = pygame.display.set_mode((r.DEFAULT_WIDTH, r.DEFAULT_HEIGHT))
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 40)

PLAYER1 = None
PLAYER2 = None
PLAYERS = []

WAVEMANAGER = c.WaveManager(SCREEN)

mainMenu = True
shop = False
isReady = [False, False]
running = True
if __name__ == "__main__":
    while running:
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(f.CreatImageElement("IMG/mainMenu.png", r.WIDTH, r.HEIGHT), (0, 0))
        deltaTime = CLOCK.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if mainMenu:
                    if event.key == pygame.K_RETURN and (PLAYER1 or PLAYER2):
                        PLAYERS = [p for p in [PLAYER1, PLAYER2] if p]; mainMenu = False
                    else:
                        if event.key == pygame.K_LSHIFT:
                            PLAYER1 = c.Player(SCREEN, (50, 650, 50, 50), "IMG/player.png", 1, 2, 100) if PLAYER1 == None else None
                        if event.key == pygame.K_RSHIFT:
                            PLAYER2 = c.Player(SCREEN, (400, 650, 50, 50), "IMG/player.png", 2, 2, 100) if PLAYER2 == None else None
                elif len(PLAYERS) == 0:
                    if event.key == pygame.K_RETURN:
                        PLAYERS = []; PLAYER1 = PLAYER2 = None; mainMenu = True; WAVEMANAGER.reset()
                elif WAVEMANAGER.wave.type == "Shop":
                    if len(PLAYERS) == 1 and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
                        isReady = []
                    elif len(PLAYERS) == 2:
                        if event.key == pygame.K_LSHIFT:
                            isReady[0] = True if isReady[0] == False else False
                        if event.key == pygame.K_RSHIFT:
                            isReady[1] = True if isReady[1] == False else False
                    if all(isReady):
                        shop = False; isReady = [False, False]; SCREEN, r.WIDTH, r.HEIGHT = f.ChangeScreen(r.DEFAULT_WIDTH, r.DEFAULT_HEIGHT); WAVEMANAGER.startWave()
        
        if mainMenu:
            m.MainMenu(SCREEN, PLAYER1, PLAYER2)
            continue
        elif len(PLAYERS) == 0:
            m.DeathScreen(SCREEN)
            continue
        elif WAVEMANAGER.wave.type == "Shop":
            if not shop:
                SCREEN, r.WIDTH, r.HEIGHT = f.ChangeScreen(r.DEFAULT_WIDTH * len(PLAYERS), r.DEFAULT_HEIGHT)
                shop = True
            m.Shop(SCREEN, PLAYERS)
            continue
        
        for player in PLAYERS[:]:
            player.handlePlayer(deltaTime, WAVEMANAGER, PLAYERS)
                
        WAVEMANAGER.handleWave(deltaTime, PLAYERS)

        pygame.display.flip()
    pygame.quit()