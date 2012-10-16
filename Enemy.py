import pygame
import GridGame
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = GridGame.load_image('battlecruiser2.png', -1)
        self.rect.topleft = (x,y)
        self.velocity = [0,0]
        
    def accellerate(self, x, y):
        self.velocity[0] += x
        self.velocity[1] += y
        
    def update(self):
        self.rect.topleft = (self.rect.topleft[0] + self.velocity[0], self.rect.topleft[1] + self.velocity[1])