# Drawing, Jaden H.
# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
width = 800
height = 600
SIZE = (width, height)
TITLE = "Night"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 150, 0)
RED = (200, 20, 20)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 200)
BROWN = (139, 69, 19)

''' Make Stars '''
stars = []
for i in range(300):
    x = random.randrange(1, width)
    y = random.randrange(1, height)
    r = random.randrange(2, 3)
    stars.append([x, y, r, r])
        
# Game loop
done = False
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Drawing code
    ''' sky '''
    screen.fill(BLACK)

    ''' stars '''
    for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)

    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' house '''
    pygame.draw.rect(screen, RED, [450, 360, 200, 100])
    pygame.draw.polygon(screen, RED,[[430, 360], [550, 300], [670, 360]])
    pygame.draw.rect(screen, BROWN, [540, 380, 45, 80])
    
    ''' fence '''
    y = 450
    for z in range(5, 800, 30):
            post = [[z + 5, y], [z + 10, y + 5], [z + 10, y + 40], [z, y + 40], [z, y + 5]]
            pygame.draw.polygon(screen, WHITE, post)


    pygame.draw.rect(screen, WHITE, [0, y + 10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y + 30, 800, 5])

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
