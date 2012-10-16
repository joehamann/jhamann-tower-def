import pygame
import GridGame
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = GridGame.load_image(image, -1)
        self.rect.topleft = (x,y)
        
