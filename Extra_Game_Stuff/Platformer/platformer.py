import pygame
from pygame.locals import *
import os

pygame.init()

#screen_width = 1000
#screen_height = 1000
screen_width=800
screen_height=600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Platformer')

title_size = 200

#images
#sun_img = pygame.image.load('sun.png')
bg_img = pygame.image.load('bg_img.jpg')

class World():
    def __init__(self, data):
        
        self.title_list = []
        
        #images
        dirt_img = pygame.image.load('dirt.jpeg')
        
        row_count = 0
        for row in data:
            col_count = 0 
            for tile in row:
                if title == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, title_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * title_size
                    img_rect.x = row_count * title_size
                    tilte = (img, img_rect)
                    self.tile_list.append(title)
                col_count += 1
            row_count += 1


world_data = [
[1,1,1,1,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,1,1,1,1],

]


world = World(world_data)


run = True
while run:
    
    screen.blit(bg_img, (0,0))
    #screen.blit(sun_img, (100,100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
    
    pygame.display.update()



main_menu()
pygame.quit()
quit()