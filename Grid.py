import pygame
import Tile
class Grid():
    """container for board tiles"""
    def __init__(self, x, y, tileX, tileY,):
        self.group = pygame.sprite.Group()
        self.tiles = []
        self.width = x
        self.height = y
        self.tileX = tileX
        self.tileY = tileY
        for i in range(x):
            self.tiles.append([])
            for j in range(y):
                self.tiles[i].append(Tile.Tile(tileX * i, tileY * j, 'grass.gif'));
                self.group.add(self.tiles[i][j])
        
    def mouseOver(self):
        (x, y) = pygame.mouse.get_pos()
        print (x / self.tileX,y / self.tileY)
        
    
    def draw(self, screen):
        self.group.draw(screen)
    
    def drawLines(self, screen):
        for i in range(self.width - 1):
            pygame.draw.line(screen, (0,0,0), ((i + 1) * self.tileX, 0), ((i + 1) * self.tileX, self.get_height()))
            for i in range(self.height - 1):
                        pygame.draw.line(screen, (0,0,0), (0, (i + 1) * self.tileY), (self.get_width(), (i + 1) * self.tileY))     
                        
    def get_height(self):
        return self.height * self.tileY
    def get_width(self):
            return self.width * self.tileX    