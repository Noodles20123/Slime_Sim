# TODO
## - screen offset by ~35px (see how spike resets at 0px)
# - Background clipping
### - Hit boxes
#### - How to change spike levels and reset the speed at level 10 and so on.

# Import a library of functions called 'pygame'
import pygame
import pygame.mixer
import sys

# Music
pygame.init()
sound = pygame.mixer.Sound('slimeMusic.wav')
sound.play(1000)

# Initialize the game engine
pygame.init()
 
# Define some colours
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

# Spike Variables
SpikeY = 410
SpikeX = 800
spike_initial_speed = 2
speed_multiplier = 1

# Window header 
pygame.display.set_caption("SlimeSimulator 2016")

# Image Variables
red_slime = pygame.image.load("RedSlime.png")
blue_slime = pygame.image.load("BlueSlime.png")
Stub = pygame.image.load("Spike.png")
Big_Text = pygame.image.load("Title.png")
Spike = pygame.image.load("Spike.png") 
background = pygame.image.load("Land.png")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Transform.Scale
background = pygame.transform.scale(background,(800,600))
red_slime = pygame.transform.scale(red_slime,(70,70))
blue_slime = pygame.transform.scale(blue_slime,(70,70))
Spike = pygame.transform.scale(Spike,(100,100))

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

# Loop as long as done == False
while not done:
    # Background Movement
    screen.blit(background,background_rect)
    x1 -= 3
    x2 -= 3
    screen.blit(background,(x1,y4))
    screen.blit(background,(x2,y3))
    if x1 > w:
        x1 = -w
    if x2 > w:
        x2 = -w
    
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
   
	# Player 1 render
    screen.blit(red_slime,[p1x, p1_y_axis])
    # Player 2 render
    screen.blit(blue_slime,[p2x,p2_y_axis])
    # Title
    screen.blit(Big_Text,(TitleX,0))
	
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
   
    # Controls, ascend and descend rates
	# Player 1
    keys = pygame.key.get_pressed()
	# If player 1 is not on the starting point, allow jump
    if p1_y_axis == starting_point:
        if keys[pygame.K_w]:
            #p1_y_axis -= jump_height
            p1_jump = True
	# If player 1 has jumped and hasn't landed, fall
    #if p1_y_axis < starting_point:
    #    p1_y_axis += fall_rate
	
	# Player 2
    keys = pygame.key.get_pressed()
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
        p1_y_axis -= 50
        if p1_y_axis < starting_point - jump_height:
            p1_jump = False
    if p1_jump == False:
        if p1_y_axis < starting_point:
            p1_y_axis += fall_rate
		
    if p2_jump == True:
        p2_y_axis -= 50
        if p2_y_axis < starting_point - jump_height:
            p2_jump = False
    if p2_jump == False:
        if p2_y_axis < starting_point:
            p2_y_axis += fall_rate
		

	
    	
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
