import pygame
import RandomTowerDefense
import HealthBar
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, order, speed, hp, bounty):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = RandomTowerDefense.load_image('battlecruiser2.png', -1)
        self.rect.topleft = (x,y)
        self.velocity = [0.0,0.0]
        self.order = order
        self.x_speed = speed
        self.accellerate(self.x_speed, 0)
        self.health = hp
        self.hp_bar = HealthBar.HealthBar(hp, x, y)
        self.bounty = bounty
        
    def accellerate(self, x, y):
        self.velocity[0] += x
        self.velocity[1] += y
        
    def update(self):
        self.rect.topleft = (self.rect.topleft[0] + self.velocity[0], self.rect.topleft[1] + self.velocity[1])
        self.hp_bar.rect.topleft = (self.hp_bar.rect.topleft[0] + self.velocity[0] , self.hp_bar.rect.topleft[1] + self.velocity[1])
        
    def damage(self, hp):
        self.hp_bar.damage(hp)
    