from maze import*
from player import*

class Room(object): 
    wall_list = None
    enemy_sprites = None
 
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
 
 
class Room1(Room):
    def __init__(self):
        super().__init__()
        walls = [[0, 0, 10, 135, BLACK],
                 [0, 131.25, 10, 160, BLACK],
                 [292.5, 0, 10, 93.75, BLACK],
                 [292.5, 131.25, 10, 160, BLACK],
                 [10, 0, 285, 10, BLACK],
                 [0, 290, 300, 10, BLACK],
                 [146.25, 30, 10, 260, WHITE],
                 [116.25, 10, 10, 260, WHITE],
                 [86.25, 30, 10, 260, WHITE],
                 [56.25, 10, 10, 260, WHITE],
                 [26.25, 30, 10, 260, WHITE],
                 [206.25, 30, 10, 260, WHITE],
                 [266.25, 30, 10, 260, WHITE],
                 [176.25, 10, 10, 260, WHITE],
                 [236.25, 10, 10, 260, WHITE],                  
                ]
 
        for item in walls:
            wall = Wall(item[0]*2.5, item[1]*2.5, item[2]*2.5, item[3]*2.5, item[4])
            self.wall_list.add(wall)
 
 
class Room2(Room):
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 10, 93.75, BLACK],
                 [0, 131.25, 10, 160, BLACK],
                 [292.5, 0, 10, 93.75, BLACK],
                 [292.5, 131.25, 10, 160, BLACK],
                 [10, 0, 285, 10, BLACK],
                 [0, 290, 300, 10, BLACK],
                 [146.25, 10, 10, 250, GREEN]
                ]
 
        for item in walls:
            wall = Wall(item[0]*2.5, item[1]*2.5, item[2]*2.5, item[3]*2.5, item[4])
            self.wall_list.add(wall)
 
 
class Room3(Room):
    def __init__(self):
        super().__init__()
 
        walls = [[10, 0, 300, 10,BLACK],[10, 0, 300, 10, BLACK],[10, 290, 290, 10, BLACK],
        [290, 10, 10, 250, BLACK],[25, 25, 10, 250, BLACK],[25, 25, 300, 10, BLACK],
        [50, 50, 225, 10, BLACK],[50, 50, 10, 300, BLACK],[75, 75, 300, 10,BLACK],
        [50, 100, 220, 10, BLACK],[75, 125, 225, 10, BLACK],[50, 150, 220, 10, BLACK],
        [265, 150, 10, 50, BLACK],[245, 210, 50, 10,BLACK],[245, 170, 10, 40,BLACK],[225, 160, 10, 70,BLACK],
        [225, 230, 50, 10, BLACK],[150, 250, 150, 10, BLACK],[200, 170, 10, 90,BLACK],[175, 160, 10, 80, BLACK],
        [150, 170, 10, 90, BLACK],[80, 170, 70, 10, BLACK],[50, 190, 90, 10, BLACK],
        [80, 210, 70, 10, BLACK],[50, 230, 90, 10, BLACK],[80, 250, 70, 10,BLACK],[70, 250, 10, 30, BLACK],
        [90, 270, 10, 30, BLACK],[110, 250, 10, 30, BLACK],[130, 270, 10, 30, BLACK],
        [150, 250, 10, 30, BLACK],[170, 270, 10, 30, BLACK],[190, 250, 10, 30, BLACK],
        [210, 270, 10, 30, BLACK],[230, 250, 10, 30,BLACK],[250, 270, 10, 30, BLACK],
        [270, 250, 10, 30, BLACK],[0, 0, 10, 93.75, BLACK],[0, 131.25, 10, 170, BLACK]]
 
        for item in walls:
            wall = Wall(item[0]*2.5, item[1]*2.5, item[2]*2.5, item[3]*2.5, item[4])
            self.wall_list.add(wall)
class Room4(Room):
    wall_list = None
    enemy_sprites = None
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()