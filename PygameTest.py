from tkinter import CENTER
import pygame, random
from Menu import MENU, CREA_MENU
from Colors import COLORS
pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
background = pygame.image.load("images/background.jpg")
background = pygame.transform.scale(background, (700, 500))

index_list_Selections = CREA_MENU.index_list_Selections
list_Selections = CREA_MENU.list_Selections
NbMenu = CREA_MENU.NbMenu
Selection = CREA_MENU.Selection

pygame.display.set_caption("Mon Jeu")


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

            if event.key==pygame.K_RIGHT:
                if Selection < NbMenu:
                    Selection += 1                    
                else:
                    Selection = 0
            if event.key==pygame.K_LEFT:
                if Selection > 0:
                    Selection -= 1                    
                else:
                    Selection = NbMenu
            if event.key==pygame.K_RETURN and Selection == NbMenu:
                carryOn=False
    # --- Game logic should go here
    
    for i in index_list_Selections:
        if i == index_list_Selections[Selection]:
            i.Select(COLORS.GREEN)
        else:
            i.Select(COLORS.YELLOW)

    # --- Drawing code should go here
    # First, clear the screen to white. 
    # screen.fill([150,150,150])
    screen.blit(background, (0, 0))
    # The you can draw different shapes and lines or add text to your background stage.
    # coordonné : x, y, taille x, taille y !!!!
    list_Selections.draw(screen)
    #pygame.draw.rect(screen, GREEN, [100, 225, 100, 50],0)
    #pygame.draw.rect(screen, [255,255,0], [300, 225, 100, 50],0)
 
     # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
     # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
