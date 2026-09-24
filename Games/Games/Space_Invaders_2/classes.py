import pygame
import functions as f
import random

WIDTH = 500
HEIGHT = 750

class Transform:
    def __init__(self, vector):
        self.x = vector[0]
        self.y = vector[1]
        self.width = vector[2]
        self.height = vector[3]
        
    def vector(self):
        return (self.x, self.y, self.width, self.height)

class Player:
    def __init__(self, screen, vector, path, id, playerCount, speed):
        self.id = id
        self.screen = screen
        self.transform = Transform(vector)
        self.image = f.CreatImageElement(path, self.transform.width, self.transform.height)
        self.gun = Gun(screen, 1, 5, self.transform, "up")
        self.hp = 3
        self.maxHP = 5
        self.alive = True
        self.speed = speed
        
        self.color = (255, 0, 0) if id == 1 else (0, 255, 0) # ! CHANGE LATER WHEN SPRITES ADDED - HARDCODED
        
        if playerCount == 1:
            self.keys = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_SPACE]
        elif id == 1:
            self.keys = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_q]
        else:
            self.keys = [pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_RSHIFT]
            
    def handlePlayer(self, deltaTime, waveManager, players):
        for enemy in waveManager.wave.enemies[:]:
            for bullet in self.gun.bullets[:]:
                if f.IsColliding(bullet.transform, enemy.transform): 
                    enemy.takeDamage(1, waveManager.wave.enemies); self.gun.bullets.remove(bullet); break
                    
            if f.IsColliding(self.transform, enemy.transform):
                self.takeDamage(1, players); enemy.takeDamage(10, waveManager.wave.enemies); break # DAMAGE - HARDCODED
                    
        self.update(deltaTime, WIDTH, HEIGHT)
        self.gun.update(deltaTime)
        self.displayHP()
        
    def update(self, deltaTime, width, height):
        keys = pygame.key.get_pressed()
        if keys[self.keys[0]]:
            self.transform.y -= self.speed * deltaTime
        if keys[self.keys[1]]:
            self.transform.x -= self.speed * deltaTime
        if keys[self.keys[2]]:
            self.transform.y += self.speed * deltaTime
        if keys[self.keys[3]]:
            self.transform.x += self.speed * deltaTime
        f.Borders(self.transform, width, height)
        if keys[self.keys[4]]:
            self.gun.shoot()
        self.screen.blit(self.image, (self.transform.x, self.transform.y))
          
    def takeDamage(self, amount, list):
        self.hp -= amount
        if self.hp <= 0: 
            self.alive = False
            list.remove(self)
        
    def heal(self, amount):
        self.hp += amount
        if self.hp > self.maxHP: self.hp = self.maxHP
        
    def displayHP(self):
        imgW = imgH = 50
        direction = imgW if self.id == 1 else -imgW
        startPos = 10 if self.id == 1 else WIDTH - (imgW - 10) * 3 - 10
        for i in range(self.hp):
            self.screen.blit(f.CreatImageElement("IMG/hart.png", imgW, imgH), (startPos + direction * i, 10))
        
class Enemy:
    def __init__(self, screen, vector, hp, speed):
        self.screen = screen
        self.transform = Transform(vector)
        self.gun = Gun(screen, 1, 0.2, self.transform, "down")
        self.hp = hp
        self.alive = True
        self.speed = speed
        
    def clone(self):
        return Enemy(self.screen, self.transform.vector(), self.hp, self.speed)
        
    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.transform.vector())
        
    def move(self, deltaTime):
        self.transform.y += self.speed * deltaTime
        return -200 <= self.transform.y <= 1000 # ! CHANGE LATER - HARDCODED
        
    def takeDamage(self, amount, list):
        self.hp -= amount
        if self.hp <= 0: 
            self.alive = False
            list.remove(self)
        
class Gun:
    def __init__(self, screen, damage, fireRate, playerTransform, direction):
        self.screen = screen
        self.damage = damage
        self.fireRate = fireRate
        self.coolDown = 0
        self.playerTransform = playerTransform
        self.transform = playerTransform
        self.bulletSpeed = -150 if direction == "up" else 150
        self.bullets = []
        
    def shoot(self):
        if self.coolDown <= 0:
            (x, y) = f.GetCenterOfObject(5, 10, self.transform.width, self.transform.height)
            self.bullets.append(Bullet((self.transform.x + x, self.transform.y + y, 5, 10), self.bulletSpeed))
            self.coolDown = 1 / self.fireRate
            
    def update(self, deltaTime):
        self.coolDown -= deltaTime
        for bullet in self.bullets[:]:
            if not bullet.move(deltaTime):
                self.bullets.remove(bullet)
            else: bullet.draw(self.screen)
    
class Bullet:
    def __init__(self, vector, speed):
        self.transform = Transform(vector)
        self.speed = speed
        
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.transform.vector())
    
    def move(self, deltaTime):
        self.transform.y += self.speed * deltaTime
        return -200 <= self.transform.y <= 1000 # ! CHANGE LATER - HARDCODED

class WaveManager:
    def __init__(self, screen):
        self.screen = screen
        self.wave = Wave([], "Shop")
        self.waveIndex = 0
        
    def generateWave(self):
        if self.waveIndex % 6 == 0: self.wave = Wave([], "Shop"); return
        
        points = int(3 + self.waveIndex * 1.2)
        ENEMIES = [
            {"cost": 3, "enemy": Enemy(self.screen, (0, -100, 50, 50), 3, 75)},
            {"cost": 5, "enemy": Enemy(self.screen, (0, -100, 25, 25), 1, 150)},
            {"cost": 10, "enemy": Enemy(self.screen, (0, -100, 75, 75), 10, 25)}
            ]
        
        enemies = []
        
        for object in ENEMIES:
            toSpend = points
            points -= points / 2
            while object["cost"] <= toSpend:
                enemies.append(object["enemy"].clone())
                toSpend -= object["cost"]
                
        self.wave = Wave(enemies, "Wave")
        
    def startWave(self):
        self.waveIndex += 1
        self.generateWave()
        self.loadEnemies()
        
    def loadEnemies(self):
        for enemy in self.wave.enemies:
            enemy.transform.x = random.randint(0, WIDTH - enemy.transform.width)
            
    def reset(self):
        self.waveIndex = 0
        self.wave = Wave([], "Shop")
        
    def handleWave(self, deltaTime, PLAYERS):
        if len(self.wave.enemies) == 0 and self.wave.type == "Wave":
            self.startWave()
            
        for enemy in self.wave.enemies[:]:
            enemy.gun.shoot()
            for bullet in enemy.gun.bullets[:]:
                for player in PLAYERS:
                    if f.IsColliding(bullet.transform, player.transform): 
                        player.takeDamage(1, PLAYERS); enemy.gun.bullets.remove(bullet); break
            
            if not enemy.move(deltaTime):
                self.wave.enemies.remove(enemy); continue
            enemy.draw()
            enemy.gun.update(deltaTime)
    
class Wave:
    def __init__(self, enemies: list[Enemy], type):
        self.enemies = enemies
        self.type = type