import pygame
import RandomTowerDefense
class HealthBar(pygame.sprite.Sprite):
    def __init__(self, hp, x, y):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.hp100, self.rect100 = RandomTowerDefense.load_image('health100.png', -1)
        self.hp90, self.rect90 = RandomTowerDefense.load_image('health90.png', -1)
        self.hp80, self.rect80 = RandomTowerDefense.load_image('health80.png', -1)
        self.hp70, self.rect70 = RandomTowerDefense.load_image('health70.png', -1)
        self.hp60, self.rect60 = RandomTowerDefense.load_image('health60.png', -1)
        self.hp50, self.rect50 = RandomTowerDefense.load_image('health50.png', -1)
        self.hp40, self.rect40 = RandomTowerDefense.load_image('health40.png', -1)
        self.hp30, self.rect30 = RandomTowerDefense.load_image('health30.png', -1)
        self.hp20, self.rect20 = RandomTowerDefense.load_image('health20.png', -1)
        self.hp10, self.rect10 = RandomTowerDefense.load_image('health10.png', -1)
        self.hp00, self.rect00 = RandomTowerDefense.load_image('health00.png', -1)
        
        self.hp = hp
        self.max_hp = hp
        self.image = self.hp100
        self.rect = self.rect100
        self.rect.topleft = (x + 30 ,y  + 10)
            
    def damage(self, hp):
        self.hp -= hp
        self.update()
    
    def update(self):
        if (self.hp / self.max_hp < 1 and self.hp / self.max_hp > .9):
            self.image = self.hp100
        elif (self.hp / self.max_hp < .9 and self.hp / self.max_hp > .8):
            self.image = self.hp90
        elif (self.hp / self.max_hp < .8 and self.hp / self.max_hp > .7):
            self.image = self.hp80
        elif (self.hp / self.max_hp < .7 and self.hp / self.max_hp > .6):
            self.image = self.hp70
        elif (self.hp / self.max_hp < .6 and self.hp / self.max_hp > .5):
            self.image = self.hp60
        elif (self.hp / self.max_hp < .5 and self.hp / self.max_hp > .4):
            self.image = self.hp50
        elif (self.hp / self.max_hp < .4 and self.hp / self.max_hp > .3):
            self.image = self.hp40
        elif (self.hp / self.max_hp < .3 and self.hp / self.max_hp > .2):
            self.image = self.hp30
        elif (self.hp / self.max_hp < .2 and self.hp / self.max_hp > .1):
            self.image = self.hp20
        elif (self.hp / self.max_hp < .1 and self.hp / self.max_hp > .0):
            self.image = self.hp10
        else :
            self.image = self.hp00