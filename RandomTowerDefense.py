
import Enemy
import Tower
import Grid
import random
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
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Random Tower Defense')
    pygame.mouse.set_visible(0)
    clock = pygame.time.Clock()
    pygame.time.set_timer(USEREVENT + 1, 500)
    
    #Prepare Game Objects
    start = False
    lose = False
    win = False
    level_break = False
    build_mode = False
    enemy_order = 0
    wave = 0
    money = 200
    countdown = 15.0
    life = 10
    enemy_hp = 100.0
    hp_mult = 1
    tower_damage = 75
    damage_mult = 1
    tower_cost = 100
    cost_mult = 1
    enemy_bounty = 50
    enemy_speed = 1
    speed_mult = 1
    lanes = [0,80,160,240,320,400,480]
    wave_length = [30,45,60]
    spawn_chance = [13, 13, 20]
    
    overlay = pygame.sprite.Sprite()
    start_image, rect = load_image('start_overlay.png', -1)
    quit_image, rect = load_image('quit_overlay.png', -1)
    lose_image, rect = load_image('lose_overlay.png', -1)
    win_image, rect = load_image('win_overlay.png', -1)
    overlay_group = pygame.sprite.Group()
    overlay_group.add(overlay)
    
    grid_x = 20
    grid_y = 16
    grid = Grid.Grid(grid_x, grid_y, 40, 40)
    
    towers = []
    for i in range(grid_x):
        towers.append([])
        for j in range(grid_y):  
            towers[i].append(None)
    hp_group = pygame.sprite.Group()
    enemies = []
    enemy_group = pygame.sprite.Group()
    
    new_tower = None
    tower_group = pygame.sprite.Group()
    new_tower_group = pygame.sprite.Group()
    
    pygame.mouse.set_visible(True)
    
    menu_rect = pygame.Rect((0, 640), (800, 700))
    menu_image, rect = load_image('menu.png', -1)
    menu_cancel_image, rect = load_image('menu_cancel.png', -1)
    menu = pygame.sprite.Sprite()
    menu.image = menu_image
    menu.rect = (0, 600)
    menu_group = pygame.sprite.Group()
    menu_group.add(menu)
    
    build_rect = pygame.Rect((47, 670), (70, 23))
    cancel_rect = pygame.Rect((45, 720),(100, 30))
    
    exit_rect = pygame.Rect((155, 665),(60, 35))
    
    new_range_color = (255,0,0)
    range_color = (0,0,255)
#Main Loop
    range_surface = pygame.Surface((800, 800))   
    while 1:
        clock.tick(120)
        
         
            
    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return    
            elif event.type == MOUSEBUTTONUP and (not start or win or lose):
                if (exit_rect.collidepoint(event.pos)):
                    return
                elif (not start):
                    start = True
                    level_break = True
                else:
                    return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return            
            elif (not start):
                continue
            elif event.type == USEREVENT + 1:
                countdown -= 0.5
                if (level_break and countdown <= 0):
                    level_break = False
                    wave += 1
                    if (wave > 1):
                        enemy_hp += enemy_hp * random.randrange(10)
                        tower_damage += tower_damage * random.randrange(7)
                        tower_cost += tower_cost * random.randrange(3)
                        enemy_bounty += enemy_bounty * random.randrange(7)
                    if (wave > 2):
                        enemy_speed += 3
                    if (wave > 3):
                        win = True  
                        tower_group.empty()
                        enemy_group.empty()
                        hp_group.empty()
                    else:
                        countdown = wave_length[wave - 1]
                        if (wave > 1):
                            money += tower_cost * 5
                elif (countdown <= 0):
                    level_break = True
                    
                    countdown = 15
                elif (not level_break and not win and not lose):
                    money += 2
                    #more enemies at a time possible at higher waves
                    for i in range(wave):
                        roll_enemy = random.randrange(99)
                        if (roll_enemy <  spawn_chance[wave - 1]):
                            print 'enemy spawned'
                            bc = Enemy.Enemy(0, lanes[random.randrange(len(lanes))], enemy_order, enemy_speed, enemy_hp, enemy_bounty)
                            hp_group.add(bc.hp_bar)
                            enemy_order += 1
                            
                            enemies.append(bc)
                            enemy_group.add(bc)
                            bc = None                                                      
                                                  
                    
                    
            elif event.type == MOUSEMOTION and build_mode:
                tilex = event.pos[0] / grid.tileX
                tiley = event.pos[1] / grid.tileY 
                if (tilex >= grid_x or tiley >= grid_y or towers[tilex][tiley] or money < tower_cost):
                    new_range_color = (255,0,0)
                else:
                    new_range_color = (0,255,0)
            elif event.type == MOUSEBUTTONUP:
                if (exit_rect.collidepoint(event.pos)):
                    return                  
                if (build_rect.collidepoint(event.pos) and not build_mode):
                    build_mode = True
                    menu.image = menu_cancel_image
                    new_tower = Tower.Tower(event.pos[0], event.pos[1], tower_damage)
                    new_tower_group.add(new_tower)
                elif (build_mode and (cancel_rect.collidepoint(event.pos) or event.button == 3)):
                    new_tower_group.remove(new_tower)
                    new_tower = None
                    build_mode = False
                    menu.image = menu_image
                elif (build_mode and not menu_rect.collidepoint(event.pos) and new_range_color != (255,0,0)):
                    print 'tower '
                    new_tower_group.remove(new_tower)
                    tower_group.add(new_tower)
                    tilex = event.pos[0] / grid.tileX
                    tiley = event.pos[1] / grid.tileY
                    new_tower.building = False
                    new_tower.rect.center = ((tilex * grid.tileX) + grid.tileX / 2, (tiley * grid.tileY) + grid.tileY / 2)
                    towers[tilex][tiley] = new_tower
                    money -= tower_cost
                    new_tower = Tower.Tower(event.pos[0], event.pos[1], tower_damage)
                    new_tower_group.add(new_tower)                    
           
        #update Everything           
        remove_list = []
        for i in reversed(range(len(enemies))):
            if (enemies[i].rect.topleft[0] > 800):
                enemy_group.remove(enemies[i])
                hp_group.remove(enemies[i].hp_bar)
                life -= 1
                remove_list.append(i)
                continue
            if (enemies[i].hp_bar.hp <= 0 ):
                enemy_group.remove(enemies[i])
                hp_group.remove(enemies[i].hp_bar)
                money += enemies[i].bounty
                remove_list.append(i)
                
        for i in range(len(remove_list)):
            enemies.pop(remove_list[i])                                        
            tower_group.update()
        if (life <= 0):
            lose = True
            tower_group.empty()
            enemy_group.empty()
            hp_group.empty()
        for i in range(grid_x):
            for j in range(grid_y):  
                if (towers[i][j]):  
                    towers[i][j].shoot_enemy(reversed(enemies))        
        enemy_group.update()
        new_tower_group.update()
        tower_group.update()
        #Draw Everything
          
        #grid.draw(screen)
        
        menu_group.draw(screen)           
        #screen.blit(background, (0, 0))
        if (build_mode):
            grid.drawLines(screen)
        
        myfont = pygame.font.SysFont("monospace", 26)
        money_label = myfont.render("%d" % money, 1, (255,255,0))
        screen.blit(money_label, (550, 665))      
        wave_label = myfont.render("%d" % wave, 1, (255,255,0))
        screen.blit(wave_label, (550, 755))       
        life_label = myfont.render("%d" % life, 1, (255,255,0))
        screen.blit(life_label, (550, 710))          
        
        countdown_label = myfont.render("%.1f" % countdown, 1, (255,255,0))
        screen.blit(countdown_label, (100, 750))
        
        ready_label = myfont.render("Get Ready!" , 1, (255,0,0))
        if (level_break):
            screen.blit(ready_label, (150, 715))
            
        
        tower_group.draw(screen)
        enemy_group.draw(screen)
        hp_group.draw(screen)
        new_tower_group.draw(screen)
        pygame.display.flip()
               
               
        
        range_surface = range_surface.convert()
        range_surface.fill((100,100,100))
        if (build_mode):
            pygame.draw.circle(range_surface, new_range_color, new_tower.rect.center, new_tower.range * grid.tileX + grid.tileX / 2, 5)         
            for i in range(grid_x):
                    for j in range(grid_y):  
                        if (towers[i][j]):
                            pygame.draw.circle(range_surface, range_color, towers[i][j].rect.center, towers[i][j].range * grid.tileX + grid.tileX / 2 , 2)
    
            
        screen.blit(range_surface, (0, 0))
        over_surface = pygame.surface.Surface((800,800))
        over_surface.fill((100,100,100))
        if (not start):
            overlay.image = start_image
            overlay.rect = (0,0)
            overlay_group.draw(over_surface)
            screen.blit(over_surface, (200,100))
        if (lose):
            overlay.image = lose_image
            overlay.rect = (0,0)
            overlay_group.draw(over_surface)
            screen.blit(over_surface, (200,100))
        if (win):
            overlay.image = win_image
            overlay.rect = (0,0)
            overlay_group.draw(over_surface) 
            screen.blit(over_surface, (200,100))
                 
#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()