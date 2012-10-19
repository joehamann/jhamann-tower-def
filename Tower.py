import pygame
import math
import RandomTowerDefense
class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, damage,  building=True):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = RandomTowerDefense.load_image('tower.png', -1)
        self.rect.topleft = (x,y)
        self.building = building
        self.range = 4
        self.speed = 40
        self.frequency = 1.0
        self.damage = damage
        self.shooting = False
        
    def update(self):
        pos = self.rect.center
        if (self.building):
            pos = pygame.mouse.get_pos()
        self.rect.center = pos
        if (self.shooting):
            self.done_shooting()
        
    def build(self):
        building = False
        pos = pygame.mouse.get_pos()
        
    def shoot_enemy(self, enemies):
        if (self.shooting):
            return
        for enemy in enemies:
            x1 = self.rect.center[0]
            y1 = self.rect.center[1]
            x2 = enemy.rect.center[0]
            y2 = enemy.rect.center[1]
            if (math.hypot(x1-x2, y1-y2) <= (self.range * 40 + 20)):
                enemy.damage(self.damage)
                self.shooting = True
                self.shot_time = pygame.time.get_ticks()
                return
         
    def done_shooting(self):
        if (self.shot_time + self.frequency * 1000 < pygame.time.get_ticks()):
            self.shooting = False