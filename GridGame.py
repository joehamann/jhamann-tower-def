
import Enemy
import Tower
import Grid
#Import Modules
import os, pygame
from pygame.locals import *

#functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption('Grass Grid')
    pygame.mouse.set_visible(0)
    build_mode = False
    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
#Prepare Game Objects
    clock = pygame.time.Clock()
    grid = Grid.Grid(20, 16, 40, 40)
    bc = Enemy.Enemy(0, 140)
    bc.accellerate(1,0)
    enemyGroup = pygame.sprite.Group()
    towerGroup = pygame.sprite.Group()
    
    enemyGroup.add(bc)
    pygame.mouse.set_visible(True)
    build_rect = pygame.Rect((100, 660), (130, 680))
    pygame.draw.rect(screen, (255,255,255), build_rect,1)

#Main Loop
    while 1:
        clock.tick(120)
        if (build_mode):
            tower.rect.center = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] )
    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            
            elif event.type == MOUSEBUTTONUP:
                if (build_rect.collidepoint(event.pos)):
                    build_mode = True
                    tower = Tower.Tower(event.pos[0], event.pos[1])
                    towerGroup.add(tower)
            
            

    #Draw Everything
          
        grid.draw(screen)
        if (build_mode):
            grid.drawLines(screen)
        screen.blit(background, (0, 0))
        enemyGroup.update()
        enemyGroup.draw(screen)
        towerGroup.draw(screen)
        pygame.display.flip()
        myfont = pygame.font.SysFont("monospace", 20)
        label = myfont.render("Build", 1, (255,255,255))
        screen.blit(label, (100, 660))
#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()