#!/usr/bin/python3
#Ella Adam
#1/15/2021

import pygame
from pygame.locals import *
import os

#Importing other game files
 
from Pong import paddles
from Space_Shooters import *
from battleship import * 
from tkinter import *
import tkinter as tk
from tkinter import messagebox

#imports for Pong
from random import randint
import math



# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

#Music for game
pygame.mixer.music.load('Platformer2.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# Game Fonts
font = "Retro.ttf"


# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():
    menu = True
    selected ="start"
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                #If quit is not hit, loop music
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('Platformer2.mp3')
                pygame.mixer.music.play()
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP or event.key==pygame.K_1:
                    selected="start"
                elif event.key==pygame.K_DOWN or event.key==pygame.K_2:
                    selected="quit"
                    
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        game_library()
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        
        #Screen (AKA Background) 
        screen.fill(black)
        
        title=text_format("OddBall Gaming", font, 90, green)
        
        if selected=="start":
            text_start=text_format("START", font, 75, blue)
        else:
            text_start = text_format("START", font, 75, white)
            
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, blue)
        else:
            text_quit = text_format("QUIT", font, 75, white)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        
        #Title
        pygame.display.set_caption("OddBall Gaming")





#Game Selecting Screen
def game_library():
    #print("I'm switching screens!!!")
    print("""
    Use the number keys to select the game you want to play, then hit \"enter\":
    1 = Battleship
    2 = Pong
    3 = Space Shooters
    4 = Return""")
    
    library = True
    selected ="battleship"
    while library:
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                #If quit is not hit, loop music
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('Platformer2.mp3')
                pygame.mixer.music.play() 
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1 or event.key==pygame.K_UP:
                    selected="battleship"
                elif event.key==pygame.K_2 or event.key==pygame.K_DOWN:
                    selected="pong" 
                elif event.key==pygame.K_3 or event.key==pygame.K_DOWN:
                    selected="break"
                elif event.key==pygame.K_4 or event.key==pygame.K_DOWN:
                    selected="return"                
                    
                if event.key==pygame.K_RETURN:
                    if selected=="battleship":
                        #print("Battleship is running")
                        battleship()
                        
                    if selected=="pong":
                        #print("Pong is running")
                        #pygame.mixer.music.load('Platformer2.mp3')
                        pygame.mixer.music.stop()
                        pong()
                        
                    if selected=="break":
                        #print("Space Shooters is running")
                        pygame.mixer.music.stop()
                        space()
                    
                    if selected=="return":
                        main_menu()
                        

        # Main Menu UI
        
        #Screen (AKA Background) 
        screen.fill(black)
        
        title=text_format("SELECT A GAME", font, 90, green)
        
        if selected=="battleship":
            text_battle=text_format("BATTLESHIP", font, 75, blue)
        else:
            text_battle = text_format("BATTLESHIP", font, 75, white)
            
        if selected=="pong":
            text_pong=text_format("PONG", font, 75, blue)
        else:
            text_pong = text_format("PONG", font, 75, white)
            
        if selected=="break":
            text_space=text_format("BREAKOUT", font, 75, blue)
        else:
            text_space = text_format("BREAKOUT", font, 75, white)        
                
        if selected=="return":
            text_back=text_format("RETURN", font, 75, blue)
        else:
            text_back = text_format("RETURN", font, 75, white)
                    
            #Only for "Select a Game"
        title_rect=title.get_rect()
        
        battle_rect=text_battle.get_rect()
        pong_rect=text_pong.get_rect()
        space_rect=text_space.get_rect()
        back_rect=text_back.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        
        screen.blit(text_battle, (screen_width/2 - (battle_rect[2]/2), 210))
        screen.blit(text_pong, (screen_width/2 - (pong_rect[2]/2), 270))
        screen.blit(text_space, (screen_width/2 - (space_rect[2]/2), 330))
        
        screen.blit(text_back, (screen_width/2 - (back_rect[2]/2), 390))
        
        pygame.display.update()
        clock.tick(FPS)
        
        #Title
        pygame.display.set_caption("Game Library")
        
        
        
#---------------Gameing Screens------------------------------------------

def battleship():
    print("I'm Battleship!!!")
    battle = True
    selected ="return"
    while battle:
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                #If quit is not hit, loop music
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('Platformer2.mp3')
                pygame.mixer.music.play() 
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1 or event.key==pygame.K_UP:
                    selected="return"               
                    
                if event.key==pygame.K_RETURN:
                    if selected=="return":
                        game_library()
                        

        # Main Menu UI
        
        #Screen (AKA Background) 
        screen.fill(black)
        
        title=text_format("BATTLESHIP", font, 90, green)
             
        if selected=="return":
            text_back=text_format("RETURN", font, 75, blue)
        else:
            text_back = text_format("RETURN", font, 75, white)
                  
        #Only for "Title"
        title_rect=title.get_rect()
       
        back_rect=text_back.get_rect()
        
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        
        screen.blit(text_back, (screen_width/2 - (back_rect[2]/2), 390))
        
        pygame.display.update()
        clock.tick(FPS)
        
        #Title
        pygame.display.set_caption("Battleship")    
    

def pong():
    #print("I'm Pong!!!")
    print("\"Press the BACKSPACE key to return to the Game Library\"")
    
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
            pygame.init()
             
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
             
    # Open a new window
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")
     
    paddleA = Paddle(WHITE, 10, 100)
    paddleA.rect.x = 20
    paddleA.rect.y = 200
     
    paddleB = Paddle(WHITE, 10, 100)
    paddleB.rect.x = 670
    paddleB.rect.y = 200
     
    ball = Ball(WHITE,10,10)
    ball.rect.x = 345
    ball.rect.y = 195
     
    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
     
    # Add the car to the list of objects
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)
     
    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
     
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
     
    #Initialise player scores
    scoreA = 0
    scoreB = 0
     
    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): #If the user did something
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE: #If the user closes the app
                carryOn = False #Stops the program
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE: #Pressing the ESC Key will quit the game
                    screen_width=800
                    screen_height=600
                    screen=pygame.display.set_mode((screen_width, screen_height))
                    pygame.mixer.music.load('Platformer2.mp3')
                    pygame.mixer.music.play()                    
                    game_library()
     
        #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)    
     
        # --- Game logic should go here
        all_sprites_list.update()
        
        #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=690:
            scoreA+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            scoreB+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]     
     
        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            pygame.mixer.music.load('paddle.wav')
            pygame.mixer.music.play()            
            ball.bounce()
        
        # --- Drawing code should go here
        # First, clear the screen to black. 
        screen.fill(BLACK)
        #Draw the net
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        
        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen) 
     
        #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (250,10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (420,10))
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
         
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()    
    
def space():
    #print("I'm Space!!!")
    print("\"Press the BACKSPACE key to return to the Game Library\"")
    
    pygame.init()
 
    # Define some colors
    WHITE = (255,255,255)
    DARKBLUE = (36,90,190)
    LIGHTBLUE = (0,176,240)
    RED = (255,0,0)
    ORANGE = (255,100,0)
    YELLOW = (255,255,0)
    BLACK = (0,0,0)
     
    score = 0
    lives = 5
    
    #-----Paddles------
    class Paddle(pygame.sprite.Sprite):
        #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super().__init__()
    
            # Pass in the color of the paddle, and its x and y position, width and height.
            # Set the background color and set it to be transparent
            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)
            self.image.set_colorkey(BLACK)
    
            # Draw the paddle (a rectangle!)
            pygame.draw.rect(self.image, color, [0, 0, width, height])
    
            # Fetch the rectangle object that has the dimensions of the image.
            self.rect = self.image.get_rect()
    
    
        def moveLeft(self, pixels):
            self.rect.x -= pixels
                #Check that you are not going too far (off the screen)
            if self.rect.x < 0:
                self.rect.x = 0
    
        def moveRight(self, pixels):
            self.rect.x += pixels
            #Check that you are not going too far (off the screen)
            if self.rect.x > 700:
                self.rect.x = 700
                
    #---Ball----
    class Ball(pygame.sprite.Sprite):
        #This class represents a ball. It derives from the "Sprite" class in Pygame.
        
        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super().__init__()
            
            # Pass in the color of the ball, and its x and y position, width and height.
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
    
    #---Bricks----
    class Brick(pygame.sprite.Sprite):
        #This class represents a brick. It derives from the "Sprite" class in Pygame.
     
        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super().__init__()
     
            # Pass in the color of the brick, and its x and y position, width and height.
            # Set the background color and set it to be transparent
            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)
            self.image.set_colorkey(BLACK)
     
            # Draw the brick (a rectangle!)
            pygame.draw.rect(self.image, color, [0, 0, width, height])
     
            # Fetch the rectangle object that has the dimensions of the image.
            self.rect = self.image.get_rect()
    
     
    # Open a new window
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Breakout")
     
    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
     
    #Create the Paddle
    paddle = Paddle(LIGHTBLUE, 100, 10)
    paddle.rect.x = 350
    paddle.rect.y = 560
     
    #Create the ball sprite
    ball = Ball(WHITE,10,10)
    ball.rect.x = 345
    ball.rect.y = 195
     
    all_bricks = pygame.sprite.Group()
    for i in range(7):
        brick = Brick(RED,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 60
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(7):
        brick = Brick(ORANGE,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 100
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(7):
        brick = Brick(YELLOW,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 140
        all_sprites_list.add(brick)
        all_bricks.add(brick)
     
    # Add the paddle to the list of sprites
    all_sprites_list.add(paddle)
    all_sprites_list.add(ball)
     
    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
     
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
     
    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE: #Pressing the ESC Key will quit the game
                    screen_width=800
                    screen_height=600
                    screen=pygame.display.set_mode((screen_width, screen_height))
                    pygame.mixer.music.load('Platformer2.mp3')
                    pygame.mixer.music.play()                    
                    game_library()            
     
        #Moving the paddle when the use uses the arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            paddle.moveRight(5)
     
        # --- Game logic should go here
        all_sprites_list.update()
     
        #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=790:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>590:
            ball.velocity[1] = -ball.velocity[1]
            lives -= 1
            if lives == 0:
                pygame.mixer.music.load('wah-wah-wah-sound-effect.mp3')
                pygame.mixer.music.play()
                #Display Game Over Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, WHITE)
                screen.blit(text, (250,300))
                pygame.display.flip() 
                pygame.time.wait(2000)

                pygame.mixer.music.stop()                
                ReplayL()
                #messagebox.askyesno(title="Play Again?", message="Want to play again?")
                '''
                if messagebox.askyesno() == True:
                    Repl()
                    quit()
                else:
                    screen_width=800
                    screen_height=600                    
                    pygame.mixer.music.load('Platformer2.mp3')
                    pygame.mixer.music.play()                    
                    game_library()
                    quit()
                '''    
     
                #Stop the Game
                #carryOn=False
                '''
               # declare the window
                window = Tk()
                # set window title
                window.title("Play Again?")
                # set window width and height
                window.configure(width=500, height=300)
                # set window background color
                window.configure(bg='lightgray')
                
                button1 = Button(text="Yes")
                button2 = Button(text="No")
                
                window.mainloop()          
                '''
        if ball.rect.y<40:
            ball.velocity[1] = -ball.velocity[1]
     
        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            pygame.mixer.music.load('paddle.wav')
            pygame.mixer.music.play()            
            ball.bounce()
     
        #Check if there is the ball collides with any of bricks
        brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
        for brick in brick_collision_list:
            pygame.mixer.music.load('paddle.wav')
            pygame.mixer.music.play()            
            ball.bounce()
            score += 1
            brick.kill()
            if len(all_bricks)==0:
                pygame.mixer.music.load('Positive-game-notification.mp3')
                pygame.mixer.music.play()
                
               #Display Level Complete Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("LEVEL COMPLETE", 1, WHITE)
                screen.blit(text, (200,300))
                pygame.display.flip()
                pygame.time.wait(3)
                pygame.mixer.music.stop()
                ReplayW()
                
                #Stop the Game
                #carryOn=False
                #tk.messagebox.askyesno(title="Play Again?", message="Want to play again?", **options)
                '''
                messagebox.askyesno(title="Play Again?", message="Want to play again?")
                
                if messagebox.askyesno() == True:
                    space()
                    quit()
                else:
                    screen_width=800
                    screen_height=600                    
                    pygame.mixer.music.load('Platformer2.mp3')
                    pygame.mixer.music.play()                    
                    game_library()
                    quit()                
                
                
                #-----POPUP WINDOW----
                # declare the window
                window = Tk()
                # set window title
                window.title("Play Again?")
                # set window width and height
                window.configure(width=500, height=300)
                # set window background color
                window.configure(bg='lightgray')
                
                yes = button(text="yes")
            
                window.mainloop()        
                '''
        # --- Drawing code should go here
        # First, clear the screen to dark blue.
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
     
        #Display the score and the number of lives at the top of the screen
        font = pygame.font.Font(None, 34)
        text = font.render("Score: " + str(score), 1, WHITE)
        screen.blit(text, (20,10))
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (650,10))
     
        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()    
    
def ReplayL():
    #print("Replay Loser!!!")
    again = True
    selected ="yes"
    while again:
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                #If quit is not hit, loop music
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('Platformer2.mp3')
                pygame.mixer.music.play() 
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1 or event.key==pygame.K_UP:
                    selected="yes"
                elif event.key==pygame.K_2 or event.key==pygame.K_DOWN:
                    selected="no"                    
                    
                if event.key==pygame.K_RETURN:
                    if selected=="yes":
                        pygame.mixer.music.stop()                        
                        space()
                    if selected=="no":
                        pygame.mixer.music.load('Platformer2.mp3')
                        pygame.mixer.music.play()                        
                        game_library()
                            
    
            # Main Menu UI
            
            #Screen (AKA Background) 
            screen.fill(black)
            
            title=text_format("TRY AGAIN?", font, 90, green)
                 
            if selected=="yes":
                text_yes=text_format("YES", font, 75, blue)
            else:
                text_yes = text_format("YES", font, 75, white)
            
            if selected=="no":
                text_no=text_format("NO", font, 75, blue)
            else:
                text_no = text_format("NO", font, 75, white)            
                      
            #Only for "Title"
            title_rect=title.get_rect()
           
            yes_rect=text_yes.get_rect()
            no_rect=text_no.get_rect()
            
            # Main Menu Text
            screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
            
            screen.blit(text_yes, (screen_width/2 - (yes_rect[2]/2), 300))
            screen.blit(text_no, (screen_width/2 - (no_rect[2]/2), 390))
            
            pygame.display.update()
            clock.tick(FPS)
            
            #Title
            pygame.display.set_caption("Try Again?")            
                        
def ReplayW():
    print("Replay Winner!!!")
    again = True
    selected ="yes"
    while again:
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                #If quit is not hit, loop music
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('Platformer2.mp3')
                pygame.mixer.music.play() 
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1 or event.key==pygame.K_UP:
                    selected="yes"
                elif event.key==pygame.K_2 or event.key==pygame.K_DOWN:
                    selected="no"                    
                    
                if event.key==pygame.K_RETURN:
                    if selected=="yes":
                        pygame.mixer.music.stop()
                        space()
                    if selected=="no":
                        pygame.mixer.music.load('Platformer2.mp3')
                        pygame.mixer.music.play()                        
                        game_library()
                            
    
            # Main Menu UI
            
            #Screen (AKA Background) 
            screen.fill(black)
            
            title=text_format("PLAY AGAIN?", font, 90, green)
                 
            if selected=="yes":
                text_yes=text_format("YES", font, 75, blue)
            else:
                text_yes = text_format("YES", font, 75, white)
            
            if selected=="no":
                text_no=text_format("NO", font, 75, blue)
            else:
                text_no = text_format("NO", font, 75, white)            
                      
            #Only for "Title"
            title_rect=title.get_rect()
           
            yes_rect=text_yes.get_rect()
            no_rect=text_no.get_rect()
            
            # Main Menu Text
            screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
            
            screen.blit(text_yes, (screen_width/2 - (yes_rect[2]/2), 300))
            screen.blit(text_no, (screen_width/2 - (no_rect[2]/2), 390))
            
            pygame.display.update()
            clock.tick(FPS)
            
            #Title
            pygame.display.set_caption("Play Again?")    
        

    

#Initialize the Game
print("\"This is a arrow key and number based selector\"")

main_menu()
pygame.quit()
quit()
