import pygame
import Tile
class Grid():
    """container for board tiles"""
    def __init__(self, x, y):
        self.group = pygame.sprite.Group()
        self.tiles = []
        self.width = x
        self.height = y
        for i in range(x):
            self.tiles.append([])
            for j in range(y):
                self.tiles[i].append(Tile.Tile(40 * i + i, 40 * j + j));
                self.group.add(self.tiles[i][j])
        
    def draw(self, screen):
        self.group.draw(screen)
