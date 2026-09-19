from pygame import draw

class Transform:
    def __init__(self, vector):
        self.x = vector[0]
        self.y = vector[1]
        self.width = vector[2]
        self.height = vector[3]
        
    def vector(self):
        return (self.x, self.y, self.width, self.height)

class Player:
    def __init__(self, vector, screen):
        self.hp = 3
        self.alive = True
        self.screen = screen
        self.transform = Transform(vector)
        
    def takeDamage(self, amount):
        self.hp -= amount
        
    def heal(self, amount):
        self.hp += amount
        
    def drawPlayer(self):
        draw.rect(self.screen, (0, 255, 0), self.transform.vector())
        
        
class Gun:
    def __init__(self, damage, fireRate):
        self.damage = damage
        self.fireRate = fireRate
        
    def shoot():
        pass