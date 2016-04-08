# -*- coding: utf-8 -*-
# TODO
## - screen offset by ~35px (see how spike resets at 
#### - How to change spike levels and reset the speed at level 15 and so on.
##### - How to make death screen once hit by a spike

# Import a library of functions called 'pygame'
import pygame
import pygame.mixer
import sys
import random
from random import randint
# Music
pygame.init()
sound = pygame.mixer.Sound('slimeMusic.wav')
sound.play(1000)
 
# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Global Mechanics
fall_rate = 10  
jump_height = 200                             
starting_point = 410
p1_y_axis = starting_point
p2_y_axis = starting_point
p1x = 100
p2x = 200
TitleX = 150
screen_width = 800
screen_height = 600
level = 1
start_screen = True
game = False
p1life = True
p2life = True
# Spike Variables
SpikeY = 410
SpikeX = 800
spike_initial_speed = 3
speed_multiplier = 1

SpikeY2 = 410
SpikeX2 = 800
spike_chance = 0
spike_generation = False




# Window header 
text_choice = random.randrange(1,26)
if text_choice == 1:
    pygame.display.set_caption('Slime Simulator 2016')
if text_choice == 2:
    pygame.display.set_caption('Slime Slimeulator 2016')
if text_choice == 3:
    pygame.display.set_caption('Slimeastic')
if text_choice == 4:
    pygame.display.set_caption('delete system32 for maximum gaming potentialism')
if text_choice == 5:
    pygame.display.set_caption('Dividing by zero')
if text_choice == 6:
    pygame.display.set_caption('Your life is a potato')
if text_choice == 7:
    pygame.display.set_caption('do something productive!')
if text_choice == 8:
    pygame.display.set_caption('not Not planes')
if text_choice == 9:
    pygame.display.set_caption('Cheeto dust')
if text_choice == 10:
    pygame.display.set_caption('overwrought turbine')
if text_choice == 11:
    pygame.display.set_caption('crumbled minima')
if text_choice == 12:
    pygame.display.set_caption('laggard tadpole')
if text_choice == 13:
    pygame.display.set_caption('creaky louse')
if text_choice == 14:
    pygame.display.set_caption('The factory flowers?')
if text_choice == 15:
    pygame.display.set_caption('A chair highlights a chocolate')
if text_choice == 16:
    pygame.display.set_caption('Better than life')
if text_choice == 17:
    pygame.display.set_caption('Now with SOUND')
if text_choice == 18:
    pygame.display.set_caption('Now with VISUALS')
if text_choice == 19:
    pygame.display.set_caption('Fix my tuna!')
if text_choice == 20:
    pygame.display.set_caption('One of a kind...')
if text_choice == 21:
    pygame.display.set_caption('Potato boiiiiiii')
if text_choice == 22:
    pygame.display.set_caption('ze Tiger H1 Tank')
if text_choice == 23:
    pygame.display.set_caption('ZE KING TIGEAAAAAA...r')
if text_choice == 24:
    pygame.display.set_caption('Chicken fingers are fruit')
if text_choice == 25:
    pygame.display.set_caption('DO NOT READ ME')
if text_choice == 26:
    pygame.display.set_caption('ヽ(⸟ᨎ⸟)ﾉ')


# Image Variables
#startbuttonhover = pygame.image.load("startHover")
startbutton = pygame.image.load("Start.png")
startup = pygame.image.load("Startmenu.png")
red_slime = pygame.image.load("RedSlime.png")
blue_slime = pygame.image.load("BlueSlime.png")
blueslime = pygame.image.load("blue_slime_win.png")
Stub = pygame.image.load("Spike.png")
Big_Text = pygame.image.load("Title.png")
Spike = pygame.image.load("Spike.png") 
background = pygame.image.load("Land.png")
LSpike = pygame.image.load("LSpike.png")
P1wins = pygame.image.load("p1won.png")
P2wins = pygame.image.load("p2won.png")
egg = pygame.image.load('face.png')

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Transform.Scale
background = pygame.transform.scale(background,(800,600))
red_slime = pygame.transform.scale(red_slime,(70,70))
blue_slime = pygame.transform.scale(blue_slime,(70,70))
Spike = pygame.transform.scale(Spike,(100,100))
LSpike = pygame.transform.scale(LSpike,(100,100))
egg = pygame.transform.scale(egg, (70, 70))

# Set the height and width of the screen
background_size = background.get_size()
background_rect = background.get_rect()
screen = pygame.display.set_mode((background_size))
w,h = background_size
x1 = 0
y4 = 0
x2 = +w
y3 = 0

#Jumping
p1_jump = False
p2_jump = False



          ###########
########## GAME LOOP ##########
          ###########

# Loop as long as done == False
while not done:
    # Background
    screen.blit(background,background_rect)
    if start_screen == True:
        screen.blit(startup, (0,0))    
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    #Startup controls
    if keys[pygame.K_SPACE]:
        start_screen= False
        game = True

    if p1life == False:
        screen.blit(P1wins,(0,0))
        screen.blit(blueslime, (400,410))
        if 400+70 > mouse[0] > 415 and 410+70 > mouse[1] > 410:
            if event.type == pygame.MOUSEBUTTONDOWN:
                 screen.blit(egg, (415, 412))
        game = False

    if p2life == False:
        screen.blit(P2wins,(0,0))
        game = False

    if game == True:
        
        # Player 1 render
        screen.blit(red_slime,[p1x, p1_y_axis])
        # Player 2 render
        screen.blit(blue_slime,[p2x,p2_y_axis])
        # Title
        screen.blit(Big_Text,(TitleX,0))

        #2nd Spike Generation
        if spike_generation == False:
            spike_chance += 1
            if spike_chance >60:
                spike_chance = randint(1,2)
                if spike_chance == 1:
                    spike_generation = True
                else:
                    spike_chance = 0


        if spike_generation == True:
            screen.blit(Spike, (SpikeX2, SpikeY2))
            if SpikeX2 >= -20:
                SpikeX2 -= spike_initial_speed*speed_multiplier
            else:
                spike_generation = False
                level += 1
                speed_multiplier += .5
                SpikeY2 = 410
                SpikeX2 = 800
	
        # Spike and Level Mechanics	
        # While spike is on screen move right
        if SpikeX >= 0:
            SpikeX -= spike_initial_speed*speed_multiplier
            screen.blit(Spike,(SpikeX,SpikeY))
        # If spike hits edge of screen (x = 0), reset to very right edge of screen
        else:
            SpikeX = screen_width
            screen.blit(Spike,(SpikeX,SpikeY))
            speed_multiplier += .5
            level += 1
        
        # Render Level Counter
        font=pygame.font.Font(None,30)
        leveltext=font.render("level:"+str(level), 1,(255,255,255))
        screen.blit(leveltext, (30, 550))
    

        if speed_multiplier >= 5.5:
            speed_multiplier = 3
            

        # Controls, ascend and descend rates
	    # Player 1

	    # If player 1 is not on the starting point, allow jump
        if p1_y_axis == starting_point:
            if keys[pygame.K_w]:
                #p1_y_axis -= jump_height
                p1_jump = True
	    # If player 1 has jumped and hasn't landed, fall
        #if p1_y_axis < starting_point:
        #    p1_y_axis += fall_rate
	
	    # Player 2
	    # If player 2 is not on the starting point, allow jump
        if p2_y_axis == starting_point:
            if keys[pygame.K_UP]:
                #p2_y_axis -= jump_height
	            p2_jump = True
        # If player 2 has jumped and hasn't landed, fall
        #if p2_y_axis < starting_point:
            #p2_y_axis += fall_rate
        

        #Jump speed
        if p1_jump == True:
            p1_y_axis -= 40
            if p1_y_axis < starting_point - jump_height:
                p1_jump = False
        if p1_jump == False:
            if p1_y_axis < starting_point:
                p1_y_axis += fall_rate
		
        if p2_jump == True:
            p2_y_axis -= 40
            if p2_y_axis < starting_point - jump_height:
                p2_jump = False
        if p2_jump == False:
            if p2_y_axis < starting_point:
                p2_y_axis += fall_rate
		

	    ###Hitboxes
        p1_hb = pygame.Rect(p1x, p1_y_axis, 31, 70)
        p2_hb = pygame.Rect(p2x,p2_y_axis, 31, 70)
        spike_hb = pygame.Rect(SpikeX + 36, SpikeY + 48, 20,20)
        spike_hb2 = pygame.Rect(SpikeX2 + 36, SpikeY2 +48, 20,20)
        #pygame.draw.rect(screen, RED,[p1x, p1_y_axis, 31 , 70])
        #pygame.draw.rect(screen, RED, [SpikeX + 36, SpikeY + 48, 20, 20])

        ###Hit Test
        if spike_hb.colliderect(p1_hb):
            p1life = False
        if spike_hb.colliderect(p2_hb):
            p2life = False
        if spike_hb2.colliderect(p1_hb):
            p1life = False
        if spike_hb2.colliderect(p2_hb):
            p2life = False
        	
        # Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Calibri', 25, True, False)
     
        # Render the text. "True" means anti-aliased text.
        # Black is the color. This creates an image of the
        # letters, but does not put it on the screen
        text = font.render(" ", True, WHITE)

     
        # Put the image of the text on the screen at 250x250
        screen.blit(text, [125, 50])


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()
