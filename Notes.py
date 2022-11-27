# from asyncio import events
import pygame
from tuner import Tuner


class JOUENOTE():

    def __init__(self, screen, carryOn):
        self.bar = pygame.image.load('images/Symbols/Bar_lines.png')
        self.bar = pygame.transform.scale(self.bar, (1290, 110))
        self.treble = pygame.image.load('images/Symbols/Treble.png')
        self.treble = pygame.transform.scale(self.treble, (110, 150))
        self.sharp = pygame.image.load('images/Symbols/Sharp.png')
        self.sharp = pygame.transform.scale(self.sharp, (90, 130))
        self.time = pygame.image.load('images/Symbols/Time.png')
        self.time = pygame.transform.scale(self.time, (73, 113))

        # Display on each file with and without instrument
        self.half_down = pygame.image.load('images/Symbols/Half_note_down.png')
        self.half_down = pygame.transform.scale(self.half_down, (80, 112))
        self.quarter_down = pygame.image.load('images/Symbols/Quarter_note_down.png')
        self.quarter_down = pygame.transform.scale(self.quarter_down, (80, 112))
        self.half_up = pygame.image.load('images/Symbols/Half_note_up.png')
        self.half_up = pygame.transform.scale(self.half_up, (80, 112))
        self.quarter_up = pygame.image.load('images/Symbols/Quarter_note_up.png')
        self.quarter_up = pygame.transform.scale(self.quarter_up, (80, 112))
        self.beam_up = pygame.image.load('images/Symbols/Beam_note_sol_la.png')
        self.beam_up = pygame.transform.scale(self.beam_up, (80, 112))
        self.half_dotted = pygame.image.load('images/Symbols/Half_note_dotted.png')
        self.half_dotted = pygame.transform.scale(self.half_dotted, (80, 112))
        self.half_cross = pygame.image.load('images/Symbols/Half_note_la5.png')
        self.half_cross = pygame.transform.scale(self.half_cross, (80, 112))
        self.beam_down = pygame.image.load('images/Symbols/Beam_note_do_si.png')
        self.beam_down = pygame.transform.scale(self.beam_down, (80, 112))

        #Button to put in the file without instrument
        self.do4 = pygame.image.load('images/Button/do4.png')
        self.do4_pressed = pygame.image.load('images/Button/do4pressed.png')
        self.do5 = pygame.image.load('images/Button/do5.png')
        self.do5_pressed = pygame.image.load('images/Button/do5pressed.png')
        self.fa4 = pygame.image.load('images/Button/fa4.png')
        self.fa4_pressed = pygame.image.load('images/Button/fa4pressed.png')
        self.fa5 = pygame.image.load('images/Button/fa5.png')
        self.fa5_pressed = pygame.image.load('images/Button/fa5pressed.png')
        self.fasharp4 = pygame.image.load('images/Button/fasharp4.png')
        self.fasharp4_pressed = pygame.image.load('images/Button/fasharp4pressed.png')
        self.fasharp5 = pygame.image.load('images/Button/fasharp5.png')
        self.fasharp5_pressed = pygame.image.load('images/Button/fasharp5pressed.png')
        self.la4 = pygame.image.load('images/Button/la4.png')
        self.la4_pressed = pygame.image.load('images/Button/la4pressed.png')
        self.la5 = pygame.image.load('images/Button/la5.png')
        self.la5_pressed = pygame.image.load('images/Button/la5pressed.png')
        self.mi4 = pygame.image.load('images/Button/mi4.png')
        self.mi4_pressed = pygame.image.load('images/Button/mi4pressed.png')
        self.mi5 = pygame.image.load('images/Button/mi5.png')
        self.mi5_pressed = pygame.image.load('images/Button/mi5pressed.png')
        self.re4 = pygame.image.load('images/Button/re4.png')
        self.re4_pressed = pygame.image.load('images/Button/re4pressed.png')
        self.re5 = pygame.image.load('images/Button/re5.png')
        self.re5_pressed = pygame.image.load('images/Button/re5pressed.png')
        self.si4 = pygame.image.load('images/Button/si4.png')
        self.si4_pressed = pygame.image.load('images/Button/si4pressed.png')
        self.si5 = pygame.image.load('images/Button/si5.png')
        self.si5_pressed = pygame.image.load('images/Button/si5pressed.png')
        self.sol4 = pygame.image.load('images/Button/sol4.png')
        self.sol4_pressed = pygame.image.load('images/Button/sol4pressed.png')
        self.sol5 = pygame.image.load('images/Button/sol5.png')
        self.sol5_pressed = pygame.image.load('images/Button/sol5pressed.png')

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

            screen.fill([150, 150, 150])
            screen.fill([150, 150, 150])

            # Display which stays here
            screen.blit(self.bar, (0, 260))
            screen.blit(self.treble, (-38, 230))
            screen.blit(self.sharp, (0, 228))
            screen.blit(self.time, (33, 257))

            # Note displayed when player plays them
            screen.blit(self.half_down, (65, 265))
            screen.blit(self.quarter_down, (140, 260))
            pygame.draw.line(screen, (0, 0, 0), (210, 293), (210, 338), 2)
            screen.blit(self.half_up, (197, 252))
            screen.blit(self.quarter_up, (265, 247))
            screen.blit(self.beam_up, (280, 252))
            pygame.draw.line(screen, (0, 0, 0), (370, 293), (370, 338), 2)
            screen.blit(self.half_down, (365, 265))
            screen.blit(self.quarter_down, (447, 260))
            pygame.draw.line(screen, (0, 0, 0), (530, 293), (530, 338), 2)
            screen.blit(self.half_dotted, (520, 259))
            pygame.draw.line(screen, (0, 0, 0), (690, 293), (690, 338), 2)
            screen.blit(self.half_down, (680, 265))
            screen.blit(self.quarter_down, (770, 260))
            pygame.draw.line(screen, (0, 0, 0), (850, 293), (850, 338), 2)
            screen.blit(self.half_cross, (850, 260))
            screen.blit(self.quarter_down, (930, 242))
            pygame.draw.line(screen, (0, 0, 0), (1010, 293), (1010, 338), 2)
            screen.blit(self.half_down, (1000, 253))
            screen.blit(self.quarter_down, (1070, 266))
            screen.blit(self.beam_down, (1083, 259))
            pygame.draw.line(screen, (0, 0, 0), (1170, 293), (1170, 338), 2)
            screen.blit(self.half_dotted, (1160, 259))

            # Display if it's without instrument
            # Will need a file of its own
            screen.blit(self.la4, (0, 0))

            # Update the screen with what we've drawn.
            pygame.display.flip()

            # Charger the file musique if it's an instrument
            #tuner = Tuner()
            # Start listening to the notes played
            #carryOnThis = tuner.musique(carryOn, carryOnThis)

            # --- Limit to 60 frames per second
            clock.tick(60)
