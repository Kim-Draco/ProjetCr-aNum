import numpy as np
import pyaudio
import datetime
import time
import pygame


class Tuner:

    def __init__(self):
        self.image1 = pygame.image.load('images/Symbols/Flat.png')
        # For printing out notes
        self.note_names = 'C C# D D# E F F# G G# A A# B'.split()

        self.NOTE_MIN = 48  # C3
        self.NOTE_MAX = 81  # A5
        self.FSAMP = 22050  # Sampling frequency in Hz
        self.FRAME_SIZE = 1024  # How many samples per frame?
        self.FRAMES_PER_FFT = 16  # FFT takes average across how many frames?

        self.samples_per_fft = self.FRAME_SIZE * self.FRAMES_PER_FFT

        self.FREQ_STEP = float(self.FSAMP) / self.samples_per_fft

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

        self.button = 0
        self.play = pygame.image.load('images/Button/play.png')
        self.play = pygame.transform.scale(self.play, (180, 130))
        self.play_rect = self.play.get_rect()
        self.play_rect.x = 550
        self.play_rect.y = 20
        self.play_pressed = pygame.image.load('images/Button/playpressed.png')
        self.play_pressed = pygame.transform.scale(self.play_pressed, (180, 130))

        self.zelda = pygame.mixer.Sound("music/ZeldasLullaby.wav")
        self.zelda.play()

    def freq_to_number(self, f):
        return 69 + 12 * np.log2(f / 440.0)

    def number_to_freq(self, n):
        return 440 * 2.0 ** ((n - 69) / 12.0)

    def note_name(self, n):
        return self.note_names[n % 12] + str(n / 12 - 1)

    def note_to_fftbin(self, n):
        return self.number_to_freq(n) / self.FREQ_STEP

    def musique(self, carryOn, carryOnThis, screen):
        pygame.display.flip()
        self.zelda = pygame.mixer.Sound("music/ZeldasLullaby.wav")
        self.zelda.play()

        time.sleep(15)
        imin = max(0, int(np.floor(self.note_to_fftbin(self.NOTE_MIN - 1))))
        imax = min(self.samples_per_fft, int(np.ceil(self.note_to_fftbin(self.NOTE_MAX + 1))))

        # Allocate space to run an FFT.
        buf = np.zeros(self.samples_per_fft, dtype=np.float32)
        num_frames = 0

        # Initialize audio
        stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                        channels=1,
                                        rate=self.FSAMP,
                                        input=True,
                                        frames_per_buffer=self.FRAME_SIZE)

        zelda_lullaby = ['B4', 'D5', 'A4', 'G4', 'A4', 'B4', 'D5', 'A4', 'B4', 'D5', 'A5', 'G5', 'D5', 'C5', 'B4', 'A4']

        carry = True
        note_valid = 0

        while carryOn and carryOnThis and carry and note_valid < len(zelda_lullaby):

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    pygame.quit()
                    # Flag that we are done, so we can exit the while loop
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.zelda.stop()
                        carryOnThis = False
                        return carryOnThis
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_rect.collidepoint(event.pos):
                        self.button = 17
                        self.zelda.stop()
                        self.zelda.play()

            if self.button == 17:
                screen.blit(self.play_pressed, self.play_rect)
            else:
                screen.blit(self.play, self.play_rect)
            
            self.button = 0

            print('------------------------------')
            print(zelda_lullaby[note_valid])
            stream.start_stream()
            start_time = datetime.datetime.now()

            # Create Hanning window function
            window = 0.5 * (1 - np.cos(np.linspace(0, 2 * np.pi, self.samples_per_fft, False)))

            while stream.is_active() and carryOnThis:

                # Shift the buffer down and new data in
                buf[:-self.FRAME_SIZE] = buf[self.FRAME_SIZE:]
                buf[-self.FRAME_SIZE:] = np.fromstring(stream.read(self.FRAME_SIZE), np.int16)

                # Run the FFT on the windowed buffer
                fft = np.fft.rfft(buf * window)

                # Get frequency of maximum response in range
                freq = (np.abs(fft[imin:imax]).argmax() + imin) * self.FREQ_STEP

                # Get note number and nearest note
                n = self.freq_to_number(freq)
                n0 = int(round(n))

                # Console output once we have a full buffer
                num_frames += 1

                # if num_frames >= FRAMES_PER_FFT:
                #     print ('freq: {:7.2f} Hz\tnote: {:>3s} {:+.2f}'.format(freq, note_name(n0), n-n0))

                if (zelda_lullaby[note_valid] == self.note_name(n0).split('.')[0]):
                    stream.stop_stream()
                    print('note found !!')
                    if note_valid >= 0:
                        screen.blit(self.half_down, (65, 265))
                    if note_valid >= 1:
                        screen.blit(self.quarter_down, (140, 260))
                    if note_valid >= 2:
                        screen.blit(self.half_up, (197, 252))
                    if note_valid >= 3:
                        if note_valid == 3:
                            screen.blit(self.eighth_up, (271, 260))
                    if note_valid >= 4:
                        screen.blit(self.beam_up, (280, 258))
                    if note_valid >= 5:
                        screen.blit(self.half_down, (365, 265))
                    if note_valid >= 6:
                        screen.blit(self.quarter_down, (447, 260))
                    if note_valid >= 7:
                        screen.blit(self.half_dotted, (520, 259))
                    if note_valid >= 8:
                        screen.blit(self.half_down, (680, 265))
                    if note_valid >= 9:
                        screen.blit(self.quarter_down, (770, 260))
                    if note_valid >= 10:
                        screen.blit(self.half_cross, (850, 260))
                    if note_valid >= 11:
                        screen.blit(self.quarter_down, (930, 242))
                    if note_valid >= 12:
                        screen.blit(self.half_down, (1000, 253))
                    if note_valid >= 13:
                        if note_valid == 13:
                            screen.blit(self.eighth_down, (1070, 266))
                    if note_valid >= 14:
                        screen.blit(self.beam_down, (1083, 259))
                    if note_valid >= 15:
                        screen.blit(self.half_dotted, (1160, 259))
                        carryOnThis = False
                    break

                pygame.display.flip()

            note_valid += 1
