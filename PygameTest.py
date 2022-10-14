from tkinter import CENTER
import pygame, random
from Menu import MENU
pygame.init()

NbMenu = 2

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
CYAN = (0,255,255)

size = (700,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mon Jeu")


Selection = 0

list_Selections = pygame.sprite.Group()
index_list_Selections = []
index_list_Selections.append(MENU(YELLOW, 100, 50))
index_list_Selections[0].rect.x = 100
index_list_Selections[0].rect.y = 225
index_list_Selections.append(MENU(YELLOW, 100, 50))
index_list_Selections[1].rect.x = 300
index_list_Selections[1].rect.y = 225
index_list_Selections.append(MENU(YELLOW, 100, 50))
index_list_Selections[2].rect.x = 500
index_list_Selections[2].rect.y = 225

for i in index_list_Selections:
    list_Selections.add(i)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()



# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                carryOn=False
            if event.key==pygame.K_RIGHT:
                if Selection < NbMenu:
                    Selection += 1                    
                else:
                    Selection = 0
            if event.key==pygame.K_LEFT:
                if Selection > 0:
                    Selection -= 1                    
                else:
                    Selection = NbMenu - 1
            if event.key==pygame.K_RETURN and Selection == NbMenu:
                carryOn=False
    # --- Game logic should go here
    
    for i in index_list_Selections:
        if i == index_list_Selections[Selection]:
            i.Select(GREEN)
        else:
            i.Select(YELLOW)

    # --- Drawing code should go here
    # First, clear the screen to white. 
    screen.fill([150,150,150])
    #The you can draw different shapes and lines or add text to your background stage.
    #coordonné : x, y, taille x, taille y !!!!
    list_Selections.draw(screen)
    #pygame.draw.rect(screen, GREEN, [100, 225, 100, 50],0)
    #pygame.draw.rect(screen, [255,255,0], [300, 225, 100, 50],0)
 
     # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
     # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
