from asyncio import events
import pygame

class JOUENOTE():

    def __init__(self, screen, carryOn):

        # The loop will carry on until the user exits the game (e.g. clicks the close button).
        carryOnThis = True
        stopGame = False
    
        # The clock will be used to control how fast the screen updates
        clock = pygame.time.Clock()

        while carryOnThis and carryOn:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit() # Flag that we are done so we can exit the while loop
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        carryOnThis = False
                        
            screen.fill([150,150,150])

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            
            # --- Limit to 60 frames per second
            clock.tick(60)
