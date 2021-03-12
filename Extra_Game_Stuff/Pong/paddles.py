#!/usr/bin/python3
#Ella Adam
#10/28/2020

#Import Section
import pygame


# --- Define some colors ----
BLACK = (0,0,0)
WHITE = (255,255,255)

# --- This class represents a paddle
# --- It derives from the "Sprite" class in Pygame -----

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # --- Calls the parent class ---
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        # --- Drawing the Paddle ----
        pygame.draw.rect(self.image, color, [0,0, width, height])
        
        self.rect = self.image.get_rect()
        
    # ---- Paddle Movements ----
    def moveUp(self, pixels):
        self.rect.y -= pixels
            #Check that you are not going too far (off the screen)
        if self.rect.y < 0:
            self.rect.y = 0
    
    def moveDown(self, pixels):
        self.rect.y += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y > 400:
            self.rect.y = 400