#!/usr/bin/python3
#Ella Adam
#1/29/2021

'''Following the Popfizz Computer Science code
https://youtu.be/81kGaOijhiA'''

import pygame
from pygame.locals import *
import os

# Game Initialization
pygame.init()

# Game Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Space Shooters")

isPlaying = True

#Background
background = pygame.image.load(os.path.join(os.path.dirname(__file__), 'space.png'))

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        playerImg = pygame.image.load(os.path.join(os.path.dirname(__file__), 'player.jpeg'))
        screen.blit(playerImg, (self.x, self.y))
    
player = Player(screen_width/2, screen_height-70)


while isPlaying:
    
    screen.blit(background, (0,0))
    player.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False
        
    pygame.display.update()
            

# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)


