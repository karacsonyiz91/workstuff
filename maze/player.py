from maze import*
from rooms import*

BLACK = (0, 0, 0)
WHITE = (51, 25, 0)
BLUE = (0, 0, 255)
GREEN = (0, 51, 25)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
ORANGE = (255,140,   0)

class Player2(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    global player2_life

    player2_life =3

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("bluecarjo4.png").convert()
        self.image.set_colorkey(BLACK)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x    
 
 
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
 
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            message_display('GAME OVER')
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            message_display('GAME OVER')        
 
class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    global player_life

    player_life=3

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("redcarjo2.png").convert()
        self.image.set_colorkey(BLACK)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x  
              
 
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
 
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            message_display('GAME OVER')
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            message_display('GAME OVER')
 