# from asyncio import events
import pygame
from tuner import Tuner
from pygame import mixer

class JOUENOTE():

    def __init__(self, screen, carryOn):
        count = 0
        instrument = False
        countButton = 0
        pygame.display.flip()

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
        self.eighth_up = pygame.image.load('images/Symbols/Eighth_note_up.png')
        self.eighth_up = pygame.transform.scale(self.eighth_up, (80, 112))
        self.eighth_down = pygame.image.load('images/Symbols/Eighth_note_down.png')
        self.eighth_down = pygame.transform.scale(self.eighth_down, (80, 112))

        #Button to click to play music
        self.button = 0
        mixer.init()

        self.do4 = pygame.image.load('images/Button/do4.png')
        self.do4 = pygame.transform.scale(self.do4, (180, 130))
        self.do4_rect = self.do4.get_rect()
        self.do4_rect.x = 18
        self.do4_rect.y = 480
        self.do4_pressed = pygame.image.load('images/Button/do4pressed.png')
        self.do4_pressed = pygame.transform.scale(self.do4_pressed, (180, 130))
        self.do4sound = pygame.mixer.Sound("piano-mp3/C4.wav")

        self.do5 = pygame.image.load('images/Button/do5.png')
        self.do5 = pygame.transform.scale(self.do5, (180, 130))
        self.do5_rect = self.do5.get_rect()
        self.do5_rect.x = 585
        self.do5_rect.y = 580
        self.do5_pressed = pygame.image.load('images/Button/do5pressed.png')
        self.do5_pressed = pygame.transform.scale(self.do5_pressed, (180, 130))
        self.do5sound = pygame.mixer.Sound("piano-mp3/C5.wav")
        
        self.fa4 = pygame.image.load('images/Button/fa4.png')
        self.fa4 = pygame.transform.scale(self.fa4, (180, 130))
        self.fa4_rect = self.fa4.get_rect()
        self.fa4_rect.x = 261
        self.fa4_rect.y = 580
        self.fa4_pressed = pygame.image.load('images/Button/fa4pressed.png')
        self.fa4_pressed = pygame.transform.scale(self.fa4_pressed, (180, 130))
        self.fa4sound = pygame.mixer.Sound("piano-mp3/F4.wav")
        
        self.fa5 = pygame.image.load('images/Button/fa5.png')
        self.fa5 = pygame.transform.scale(self.fa5, (180, 130))
        self.fa5_rect = self.fa5.get_rect()
        self.fa5_rect.x = 828
        self.fa5_rect.y = 480
        self.fa5_pressed = pygame.image.load('images/Button/fa5pressed.png')
        self.fa5_pressed = pygame.transform.scale(self.fa5_pressed, (180, 130))
        self.fa5sound = pygame.mixer.Sound("piano-mp3/F5.wav")
        
        self.fasharp4 = pygame.image.load('images/Button/fasharp4.png')
        self.fasharp4 = pygame.transform.scale(self.fasharp4, (180, 130))
        self.fasharp4_rect = self.fasharp4.get_rect()
        self.fasharp4_rect.x = 450
        self.fasharp4_rect.y = 360
        self.fasharp4_pressed = pygame.image.load('images/Button/fasharp4pressed.png')
        self.fasharp4_pressed = pygame.transform.scale(self.fasharp4_pressed, (180, 130))
        self.fasharp4sound = pygame.mixer.Sound("piano-mp3/Gb4.wav")
        
        self.fasharp5 = pygame.image.load('images/Button/fasharp5.png')
        self.fasharp5 = pygame.transform.scale(self.fasharp5, (180, 130))
        self.fasharp5_rect = self.fasharp5.get_rect()
        self.fasharp5_rect.x = 640
        self.fasharp5_rect.y = 360
        self.fasharp5_pressed = pygame.image.load('images/Button/fasharp5pressed.png')
        self.fasharp5_pressed = pygame.transform.scale(self.fasharp5_pressed, (180, 130))
        self.fasharp5sound = pygame.mixer.Sound("piano-mp3/Gb5.wav")
        
        self.la4 = pygame.image.load('images/Button/la4.png')
        self.la4 = pygame.transform.scale(self.la4, (180, 130))
        self.la4_rect = self.la4.get_rect()
        self.la4_rect.x = 423
        self.la4_rect.y = 580
        self.la4_pressed = pygame.image.load('images/Button/la4pressed.png')
        self.la4_pressed = pygame.transform.scale(self.la4_pressed, (180, 130))
        self.la4sound = pygame.mixer.Sound("piano-mp3/A4.wav")
        
        self.la5 = pygame.image.load('images/Button/la5.png')
        self.la5 = pygame.transform.scale(self.la5, (180, 130))
        self.la5_rect = self.la5.get_rect()
        self.la5_rect.x = 990
        self.la5_rect.y = 480
        self.la5_pressed = pygame.image.load('images/Button/la5pressed.png')
        self.la5_pressed = pygame.transform.scale(self.la5_pressed, (180, 130))
        self.la5sound = pygame.mixer.Sound("piano-mp3/A5.wav")
        
        self.mi4 = pygame.image.load('images/Button/mi4.png')
        self.mi4 = pygame.transform.scale(self.mi4, (180, 130))
        self.mi4_rect = self.mi4.get_rect()
        self.mi4_rect.x = 180
        self.mi4_rect.y = 480
        self.mi4_pressed = pygame.image.load('images/Button/mi4pressed.png')
        self.mi4_pressed = pygame.transform.scale(self.mi4_pressed, (180, 130))
        self.mi4sound = pygame.mixer.Sound("piano-mp3/E4.wav")
        
        self.mi5 = pygame.image.load('images/Button/mi5.png')
        self.mi5 = pygame.transform.scale(self.mi5, (180, 130))
        self.mi5_rect = self.mi5.get_rect()
        self.mi5_rect.x = 747
        self.mi5_rect.y = 580
        self.mi5_pressed = pygame.image.load('images/Button/mi5pressed.png')
        self.mi5_pressed = pygame.transform.scale(self.mi5_pressed, (180, 130))
        self.mi5sound = pygame.mixer.Sound("piano-mp3/E5.wav")
        
        self.re4 = pygame.image.load('images/Button/re4.png')
        self.re4 = pygame.transform.scale(self.re4, (180, 130))
        self.re4_rect = self.re4.get_rect()
        self.re4_rect.x = 99
        self.re4_rect.y = 580
        self.re4_pressed = pygame.image.load('images/Button/re4pressed.png')
        self.re4_pressed = pygame.transform.scale(self.re4_pressed, (180, 130))
        self.re4sound = pygame.mixer.Sound("piano-mp3/D4.wav")
        
        self.re5 = pygame.image.load('images/Button/re5.png')
        self.re5 = pygame.transform.scale(self.re5, (180, 130))
        self.re5_rect = self.re5.get_rect()
        self.re5_rect.x = 676
        self.re5_rect.y = 480
        self.re5_pressed = pygame.image.load('images/Button/re5pressed.png')
        self.re5_pressed = pygame.transform.scale(self.re5_pressed, (180, 130))
        self.re5sound = pygame.mixer.Sound("piano-mp3/D5.wav")
        
        self.si4 = pygame.image.load('images/Button/si4.png')
        self.si4 = pygame.transform.scale(self.si4, (180, 130))
        self.si4_rect = self.si4.get_rect()
        self.si4_rect.x = 504
        self.si4_rect.y = 480
        self.si4_pressed = pygame.image.load('images/Button/si4pressed.png')
        self.si4_pressed = pygame.transform.scale(self.si4_pressed, (180, 130))
        self.si4sound = pygame.mixer.Sound("piano-mp3/B4.wav")
        
        self.si5 = pygame.image.load('images/Button/si5.png')
        self.si5 = pygame.transform.scale(self.si5, (180, 130))
        self.si5_rect = self.si5.get_rect()
        self.si5_rect.x = 1071
        self.si5_rect.y = 580
        self.si5_pressed = pygame.image.load('images/Button/si5pressed.png')
        self.si5_pressed = pygame.transform.scale(self.si5_pressed, (180, 130))
        self.si5sound = pygame.mixer.Sound("piano-mp3/B5.wav")
        
        self.sol4 = pygame.image.load('images/Button/sol4.png')
        self.sol4 = pygame.transform.scale(self.sol4, (180, 130))
        self.sol4_rect = self.sol4.get_rect()
        self.sol4_rect.x = 342
        self.sol4_rect.y = 480
        self.sol4_pressed = pygame.image.load('images/Button/sol4pressed.png')
        self.sol4_pressed = pygame.transform.scale(self.sol4_pressed, (180, 130))
        self.sol4sound = pygame.mixer.Sound("piano-mp3/G4.wav")
        
        self.sol5 = pygame.image.load('images/Button/sol5.png')
        self.sol5 = pygame.transform.scale(self.sol5, (180, 130))
        self.sol5_rect = self.sol5.get_rect()
        self.sol5_rect.x = 909
        self.sol5_rect.y = 580
        self.sol5_pressed = pygame.image.load('images/Button/sol5pressed.png')
        self.sol5_pressed = pygame.transform.scale(self.sol5_pressed, (180, 130))
        self.sol5sound = pygame.mixer.Sound("piano-mp3/G5.wav")
        
        self.play = pygame.image.load('images/Button/play.png')
        self.play = pygame.transform.scale(self.play, (180, 130))
        self.play_rect = self.play.get_rect()
        self.play_rect.x = 550
        self.play_rect.y = 20
        self.play_pressed = pygame.image.load('images/Button/playpressed.png')
        self.play_pressed = pygame.transform.scale(self.play_pressed, (180, 130))

        self.zelda = pygame.mixer.Sound("music/ZeldasLullaby.wav")
        self.zelda.play()

        # The loop will carry on until the user exits the game (e.g. clicks the close button).
        carryOnThis = True
        stopGame = False

        # The clock will be used to control how fast the screen updates
        clock = pygame.time.Clock()

        while carryOnThis and carryOn:

            screen.fill([150, 150, 150])
            screen.fill([150, 150, 150])

            # Display which stays here
            screen.blit(self.bar, (0, 260))
            screen.blit(self.treble, (-38, 230))
            screen.blit(self.sharp, (0, 228))
            screen.blit(self.time, (33, 257))
            pygame.draw.line(screen, (0, 0, 0), (210, 293), (210, 338), 2)
            pygame.draw.line(screen, (0, 0, 0), (370, 293), (370, 338), 2)
            pygame.draw.line(screen, (0, 0, 0), (530, 293), (530, 338), 2)
            pygame.draw.line(screen, (0, 0, 0), (690, 293), (690, 338), 2)
            pygame.draw.line(screen, (0, 0, 0), (850, 293), (850, 338), 2)
            pygame.draw.line(screen, (0, 0, 0), (1010, 293), (1010, 338), 2)
            pygame.draw.line(screen, (0, 0, 0), (1170, 293), (1170, 338), 2)

            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    # Flag that we are done, so we can exit the while loop
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        carryOnThis = False
                elif event.type == pygame.MOUSEBUTTONDOWN:    
                    if not instrument:
                        if self.do4_rect.collidepoint(event.pos):
                            self.button = 1
                        elif self.re4_rect.collidepoint(event.pos):
                            self.button = 2
                        elif self.mi4_rect.collidepoint(event.pos):
                            self.button = 3
                        elif self.fa4_rect.collidepoint(event.pos):
                            self.button = 4
                        elif self.sol4_rect.collidepoint(event.pos):
                            self.button = 5
                            countButton = 4
                        elif self.la4_rect.collidepoint(event.pos):
                            self.button = 6
                            if count == 2:
                                countButton = 3
                            elif count == 4:
                                countButton = 5
                            elif count == 7:
                                countButton = 8
                            elif count == 15:
                                countButton = 16
                        elif self.si4_rect.collidepoint(event.pos):
                            self.button = 7
                            if count == 0:
                                countButton = 1
                            elif count == 5:
                                countButton = 6
                            elif count == 8:
                                countButton = 9
                            elif count == 14:
                                countButton = 15
                        elif self.do5_rect.collidepoint(event.pos):
                            self.button = 8
                            countButton = 14
                        elif self.re5_rect.collidepoint(event.pos):
                            self.button = 9
                            if count == 1:
                                countButton = 2
                            elif count == 6:
                                countButton = 7
                            elif count == 9:
                                countButton = 10
                            elif count == 12:
                                countButton = 13
                        elif self.mi5_rect.collidepoint(event.pos):
                            self.button = 10
                        elif self.fa5_rect.collidepoint(event.pos):
                            self.button = 11
                        elif self.sol5_rect.collidepoint(event.pos):
                            self.button = 12
                            countButton = 12
                        elif self.la5_rect.collidepoint(event.pos):
                            self.button = 13
                            countButton = 11
                        elif self.si5_rect.collidepoint(event.pos):
                            self.button = 14
                        elif self.fasharp4_rect.collidepoint(event.pos):
                            self.button = 15
                        elif self.fasharp5_rect.collidepoint(event.pos):
                            self.button = 16
                    if self.play_rect.collidepoint(event.pos):
                        self.button = 17
                        self.zelda.stop()
                        self.zelda.play()

            if not instrument:
                # Display the button
                if self.button == 1:
                    screen.blit(self.do4_pressed, self.do4_rect)
                    self.do4sound.play()
                else:
                    screen.blit(self.do4, self.do4_rect)

                if self.button == 2:
                    screen.blit(self.re4_pressed, self.re4_rect)
                    self.re4sound.play()
                else:
                    screen.blit(self.re4, self.re4_rect)

                if self.button == 3:
                    screen.blit(self.mi4_pressed, self.mi4_rect)
                    self.mi4sound.play()
                else:
                    screen.blit(self.mi4, self.mi4_rect)

                if self.button == 4:
                    screen.blit(self.fa4_pressed, self.fa4_rect)
                    self.fa4sound.play()
                else:
                    screen.blit(self.fa4, self.fa4_rect)

                if self.button == 5:
                    screen.blit(self.sol4_pressed, self.sol4_rect)
                    self.sol4sound.play()
                else:
                    screen.blit(self.sol4, self.sol4_rect)

                if self.button == 6:
                    screen.blit(self.la4_pressed, self.la4_rect)
                    self.la4sound.play()
                else:
                    screen.blit(self.la4, self.la4_rect)

                if self.button == 7:
                    screen.blit(self.si4_pressed, self.si4_rect)
                    self.si4sound.play()
                else:
                    screen.blit(self.si4, self.si4_rect)

                if self.button == 8:
                    screen.blit(self.do5_pressed, self.do5_rect)
                    self.do5sound.play()
                else:
                    screen.blit(self.do5, self.do5_rect)

                if self.button == 9:
                    screen.blit(self.re5_pressed, self.re5_rect)
                    self.re5sound.play()
                else:
                    screen.blit(self.re5, self.re5_rect)

                if self.button == 10:
                    screen.blit(self.mi5_pressed, self.mi5_rect)
                    self.mi5sound.play()
                else:
                    screen.blit(self.mi5, self.mi5_rect)

                if self.button == 11:
                    screen.blit(self.fa5_pressed, self.fa5_rect)
                    self.fa5sound.play()
                else:
                    screen.blit(self.fa5, self.fa5_rect)

                if self.button == 12:
                    screen.blit(self.sol5_pressed, self.sol5_rect)
                    self.sol5sound.play()
                else:
                    screen.blit(self.sol5, self.sol5_rect)

                if self.button == 13:
                    screen.blit(self.la5_pressed, self.la5_rect)
                    self.la5sound.play()
                else:
                    screen.blit(self.la5, self.la5_rect)

                if self.button == 14:
                    screen.blit(self.si5_pressed, self.si5_rect)
                    self.si5sound.play()
                else:
                    screen.blit(self.si5, self.si5_rect)

                if self.button == 15:
                    screen.blit(self.fasharp4_pressed, self.fasharp4_rect)
                    self.fasharp4sound.play()
                else:
                    screen.blit(self.fasharp4, self.fasharp4_rect)

                if self.button == 16:
                    screen.blit(self.fasharp5_pressed, self.fasharp5_rect)
                    self.fasharp5sound.play()
                else:
                    screen.blit(self.fasharp5, self.fasharp5_rect)

                if self.button == 17:
                    screen.blit(self.play_pressed, self.play_rect)
                else:
                    screen.blit(self.play, self.play_rect)

                if count == 0 and countButton == 1:
                    screen.blit(self.half_down, (65, 265))
                    count += 1
                elif count >= 1:
                    screen.blit(self.half_down, (65, 265))

                if count == 1 and countButton == 2:
                    screen.blit(self.quarter_down, (140, 260))
                    count += 1
                elif count >= 2:
                    screen.blit(self.quarter_down, (140, 260))

                if count == 2 and countButton == 3:
                    screen.blit(self.half_up, (197, 252))
                    count += 1
                elif count >= 3:
                    screen.blit(self.half_up, (197, 252))

                if count == 3 and countButton == 4:
                    screen.blit(self.eighth_up, (271, 260))
                    count += 1
                elif count == 4:
                    screen.blit(self.eighth_up, (271, 260))

                if count == 4 and countButton == 5:
                    count += 1
                    screen.blit(self.beam_up, (280, 258))
                elif count >= 5:
                    screen.blit(self.beam_up, (280, 258))

                if count == 5 and countButton == 6:
                    screen.blit(self.half_down, (365, 265))
                    count += 1
                elif count >= 6:
                    screen.blit(self.half_down, (365, 265))

                if count == 6 and countButton == 7:
                    screen.blit(self.quarter_down, (447, 260))
                    count += 1
                elif count >= 7:
                    screen.blit(self.quarter_down, (447, 260))

                if count == 7 and countButton == 8:
                    screen.blit(self.half_dotted, (520, 259))
                    count += 1
                elif count >= 8:
                    screen.blit(self.half_dotted, (520, 259))

                if count == 8 and countButton == 9:
                    screen.blit(self.half_down, (680, 265))
                    count += 1
                elif count >= 9:
                    screen.blit(self.half_down, (680, 265))

                if count == 9 and countButton == 10:
                    screen.blit(self.quarter_down, (770, 260))
                    count += 1
                elif count >= 10:
                    screen.blit(self.quarter_down, (770, 260))

                if count == 10 and countButton == 11:
                    screen.blit(self.half_cross, (850, 260))
                    count += 1
                elif count >= 11:
                    screen.blit(self.half_cross, (850, 260))

                if count == 11 and countButton == 12:
                    screen.blit(self.quarter_down, (930, 242))
                    count += 1
                elif count >= 12:
                    screen.blit(self.quarter_down, (930, 242))

                if count == 12 and countButton == 13:
                    screen.blit(self.half_down, (1000, 253))
                    count += 1
                elif count >= 13:
                    screen.blit(self.half_down, (1000, 253))

                if count == 13 and countButton == 14:
                    screen.blit(self.eighth_down, (1072, 266))
                    count += 1
                elif count == 14:
                    screen.blit(self.eighth_down, (1070, 266))

                if count == 14 and countButton == 15:
                    count += 1
                    screen.blit(self.beam_down, (1083, 259))
                elif count >= 15:
                    screen.blit(self.beam_down, (1083, 259))

                if count == 15 and countButton == 16:
                    screen.blit(self.half_dotted, (1160, 259))
                    count += 1
                elif count >= 16:
                    screen.blit(self.half_dotted, (1160, 259))

                self.button = 0
            else:
                # Charger the file musique if it's an instrument
                tuner = Tuner()
                # Start listening to the notes played
                carryOnThis = tuner.musique(carryOn, carryOnThis, screen)

            # Update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)
