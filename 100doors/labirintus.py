import pygame
import os
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


def koordinat(var, num, name, w, h, x, y,):
    for var in range(num):
        name = Block(RED,w, h)
 
        name.rect.x = x
        name.rect.y = y
 
        block_list.add(name)
        all_sprites_list.add(name)

 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# Ezek a falak. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 300)
wall_list.add(wall)
all_sprites_list.add(wall)

 
wall = Wall(10, 0, 300, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(10, 290, 290, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(290, 10, 10, 290)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(25, 25, 10, 250)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(25, 25, 300, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(50, 50, 225, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(50, 50, 10, 300)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(75, 75, 300, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(50, 100, 220, 10)
wall_list.add(wall)
all_sprites_list.add(wall)


wall = Wall(75, 125, 225, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(50, 150, 220, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(265, 150, 10, 50)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(245, 210, 50, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(245, 170, 10, 40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(225, 160, 10, 70)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(225, 230, 50, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(150, 250, 150, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(200, 170, 10, 90)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(175, 160, 10, 80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(150, 170, 10, 90)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(80, 170, 70, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(50, 190, 90, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(80, 210, 70, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(50, 230, 90, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(80, 250, 70, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(70, 250, 10, 30)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(90, 270, 10, 30)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(110, 250, 10, 30)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(130, 270, 10, 30)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(150, 250, 10, 30)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(170, 270, 10, 30)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(190, 250, 10, 30)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(210, 270, 10, 30)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(230, 250, 10, 30)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(250, 270, 10, 30)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(270, 250, 10, 30)
wall_list.add(wall)
all_sprites_list.add(wall)




koordinat('h', 1, 'Jancsi', 100, 20, 200, 40)

for x in range(10):
    block = Block(BLACK,20, 20)
 
    block.rect.x = 0 + x 
    block.rect.y = 140
 
    block_list.add(block)
    all_sprites_list.add(block)

for y in range(1):
    block = Block(RED,20, 200)
 
    block.rect.x = 100
    block.rect.y = 140 + y
 
    block_list.add(block)
    all_sprites_list.add(block)
  
# Create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)

finish = Block(RED, 20, 15)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
life = 3
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos(20, 20)
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        life-=1
        #score+=1
        print(life)
        if life is 0:
            pygame.quit()
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

#pygame.quit()