# from asyncio import events
import pygame
from tuner import Tuner

class JOUENOTE():

    def __init__(self, screen, carryOn):
        self.bar = pygame.image.load('images/Symbols/Bar_lines.png')
        self.bar = pygame.transform.scale(self.bar, (1290, 220))
        self.treble = pygame.image.load('images/Symbols/Treble.png')
        self.treble = pygame.transform.scale(self.treble, (580, 620))
        # The loop will carry on until the user exits the game (e.g. clicks the close button).
        carryOnThis = True
        stopGame = False
    
        # The clock will be used to control how fast the screen updates
        clock = pygame.time.Clock()

        while carryOnThis and carryOn:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    # Flag that we are done, so we can exit the while loop
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        carryOnThis = False

            screen.fill([150,150,150])
            screen.fill([150, 150, 150])
            screen.blit(self.bar, (0, 250))
            screen.blit(self.treble, (-200, 60))

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Charge tuner
            tuner = Tuner()
            # Start listening to the notes played
            tuner.musique(carryOnThis, carryOn)
            
            # --- Limit to 60 frames per second
            clock.tick(60)
