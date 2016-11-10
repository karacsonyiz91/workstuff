import pygame
from pygame.locals import *
import time
from rooms import*
from player import*


def player_contol(player2):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            player2.changespeed(5, 0)
        if event.key == pygame.K_a:
            player2.changespeed(-5, 0)
        if event.key == pygame.K_s:
            player2.changespeed(0, 5)
        if event.key == pygame.K_w:
            player2.changespeed(0, -5)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            player2.changespeed(-5, 0)
        if event.key == pygame.K_a:
            player2.changespeed(5, 0)
        if event.key == pygame.K_s:
            player2.changespeed(0, -5)
        if event.key == pygame.K_w:
            player2.changespeed(0, 5) 
 
class Wall(pygame.sprite.Sprite):
 
    def __init__(self, x, y, width, height, color):
         
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 


        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x



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

#def life_zero():  
 #   pygame.quit()


def main():
    pygame.init()
    screen = pygame.display.set_mode([750, 750])
    myfont = pygame.font.SysFont("monospace", 15)
    pygame.display.set_caption('Zodia')
    player = Player(35, 35)
    player2 = Player2(35, 35)
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
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player2.changespeed(3, 0)
                if event.key == pygame.K_a:
                    player2.changespeed(-3, 0)
                if event.key == pygame.K_s:
                    player2.changespeed(0, 3)
                if event.key == pygame.K_w:
                    player2.changespeed(0, -3)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player2.changespeed(-3, 0)
                if event.key == pygame.K_a:
                    player2.changespeed(3, 0)
                if event.key == pygame.K_s:
                    player2.changespeed(0, -3)
                if event.key == pygame.K_w:
                    player2.changespeed(0, 3)       
 
            
 # itt kezdödik a player 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-7, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(7, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -7)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 7)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(7, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-7, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 7)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -7)


        player2.move(current_room.wall_list)
        player.move(current_room.wall_list)
        
        if player.rect.x < -15 or player2.rect.x < -15:
            if current_room_no == 0 and player.rect.x <-15:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 35
                player2.rect.x =35
                player.rect.y = 35
                player2.rect.y =35
                player2_life -= 1

            elif current_room_no == 0 and player2.rect.x < -15:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 35
                player2.rect.x =35
                player.rect.y = 35
                player2.rect.y =35
                player_life -= 1

            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 35
                player2.rect.x =35
                player.rect.y = 35
                player2.rect.y =35
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 35
                player2.rect.x =35
                player.rect.y = 35
                player2.rect.y =35
 
        if player.rect.x > 751 or player2.rect.x > 751:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 35
                player2.rect.x =35
                player.rect.y = 35
                player2.rect.y =35

            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 35
                player2.rect.x =35
                player.rect.y = 35
                player2.rect.y =35
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 35
                player2.rect.x =35
                player.rect.y = 35
                player2.rect.y =35
        if player.rect.x > 740:
           if current_room_no == 2:
                current_room_no = 3
                message_display('Nyertél!')
                current_room = rooms[current_room_no]
                player.rect.x = 35
                player2.rect.x =35
                player.rect.y = 35
                player2.rect.y =35
        background_position = [0, 0]
        background_image = pygame.image.load("background2.jpg").convert()
        screen.blit(background_image, background_position)
 
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()