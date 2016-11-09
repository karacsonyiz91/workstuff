import pygame
from pygame.locals import *
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
ORANGE = (255,140,   0)


 
class Wall(pygame.sprite.Sprite):
 
    def __init__(self, x, y, width, height, color):
         
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 


        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Player2(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([30, 30])
        self.image.fill(BLACK)
 
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
 
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
 
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
                 [146.25, 30, 10, 260, GREEN]
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
                 [146.25, 10, 10, 270, RED]
                ]
 
        for item in walls:
            wall = Wall(item[0]*2.5, item[1]*2.5, item[2]*2.5, item[3]*2.5, item[4])
            self.wall_list.add(wall)
 
 
class Room3(Room):
    def __init__(self):
        super().__init__()
 
        walls = [[10, 0, 300, 10,BLACK],[10, 0, 300, 10, BLACK],[10, 290, 290, 10, BLACK],
        [290, 10, 10, 270, BLACK],[25, 25, 10, 250, BLACK],[25, 25, 300, 10, BLACK],
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
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((450),(450))
    screen = pygame.display.set_mode([750, 750])
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
def main():
    pygame.init()
    screen = pygame.display.set_mode([750, 750])
    myfont = pygame.font.SysFont("monospace", 15)
    pygame.display.set_caption('Zodia')
    player = Player(50, 50)
    player2 = Player2(100, 100)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    movingsprites.add(player2)
 
    rooms = []
 
    room = Room1()
    rooms.append(room)
 
    room = Room2()
    rooms.append(room)
 
    room = Room3()
    rooms.append(room)
    room = Room4()
    rooms.append(room)
 
    current_room_no = 0
    current_room = rooms[current_room_no]
 
    clock = pygame.time.Clock()
 
    done = False
 
    while not done:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                #itt kezdődik a player2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player2.changespeed(-5, 0)
                if event.key == pygame.K_a:
                    player2.changespeed(5, 0)
                if event.key == pygame.K_s:
                    player2.changespeed(0, -5)
                if event.key == pygame.K_w:
                    player2.changespeed(0, 5)
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player2.changespeed(5, 0)
                if event.key == pygame.K_a:
                    player2.changespeed(-5, 0)
                if event.key == pygame.K_s:
                    player2.changespeed(0, 5)
                if event.key == pygame.K_w:
                    player2.changespeed(0, -5)
 
            player2.move(current_room.wall_list)
        
            if player2.rect.x < -15:
                if current_room_no == 0:
                    current_room_no = 2
                    current_room = rooms[current_room_no]
                    player2.rect.x = 740
                elif current_room_no == 2:
                    current_room_no = 1
                    current_room = rooms[current_room_no]
                    player2.rect.x = 740
                else:
                    current_room_no = 0
                    current_room = rooms[current_room_no]
                    player2.rect.x = 740
 
            if player2.rect.x > 751:
                if current_room_no == 0:
                    current_room_no = 1
                    current_room = rooms[current_room_no]
                    player2.rect.x = 0
                elif current_room_no == 1:
                    current_room_no = 2
                    current_room = rooms[current_room_no]
                    player2.rect.x = 0
                else:
                    current_room_no = 0
                    current_room = rooms[current_room_no]
                    player2.rect.x = 0
            if player2.rect.x > 740:
                if current_room_no == 2:
                    current_room_no = 3
                    message_display('Játékos 1 nyert!!')
                    current_room = rooms[current_room_no]
                    player2.rect.x = 0
 # itt kezdödik a player 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
 
        player.move(current_room.wall_list)
        
        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 740
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 740
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 740
 
        if player.rect.x > 751:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0
        if player.rect.x > 740:
           if current_room_no == 2:
                current_room_no = 3
                message_display('Nyertél!')
                current_room = rooms[current_room_no]
                player.rect.x = 0
        screen.fill(BLUE)
 
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()