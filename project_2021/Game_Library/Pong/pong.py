#!/usr/bin/python3
#Ella Adam
#10/28/2020


'''This is a multiplayer pong game'''

#Import Section
import pygame
from paddles import Paddle
from random import randint
import math

pygame.init()


# --- Define some colors ----
BLACK = (0,0,0)
WHITE = (255,255,255)
#-ball---------------- Credit:https://www.101computing.net/pong-tutorial-using-pygame-adding-a-bouncing-ball/
class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)    
# --- Creating a new Window Screen ------

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
# Create a group of 1 ball (used in checking collisions)
ball.rect.x = 345
ball.rect.y = 195

#This list will contain all sprites we intend to use
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)


# ---- Game loop untill user closes program ----
carryOn = True

# ---Clock for screen updates ----
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while carryOn: 
    #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(6)
    if keys[pygame.K_s]:
        paddleA.moveDown(6)
    if keys[pygame.K_UP]:
        paddleB.moveUp(6)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(6) 
    
    if ball.rect.x>=690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]   
    
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
           

    # --- Main Event Loop ---------
    for event in pygame.event.get(): #If the user did something
        if event.type == pygame.QUIT: #If the user closes the app
            carryOn = False #Stops the program
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE: #Pressing the ESC Key will quit the game
                carryOn=False        
     
    
    # --- Game logic should go here --------
    all_sprites_list.update()
    # --- Drawing Code -----
    screen.fill(BLACK)
    #Drawing the Net
    pygame.draw.line(screen, WHITE, [349,0], [349, 500], 5)
    #Draw the sprites
    all_sprites_list.draw(screen) 
    
    # ---- Updating the Screen with the drawings ----
    pygame.display.flip()
    # --- Frames per Second -----
    clock.tick(60)

pygame.quit()