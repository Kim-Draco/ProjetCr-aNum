#! /usr/bin/env python
######################################################################
# tuner.py - a minimal command-line guitar/ukulele tuner in Python.
# Requires numpy and pyaudio.
######################################################################
# Author:  Matt Zucker
# Date:    July 2016
# License: Creative Commons Attribution-ShareAlike 3.0
#          https://creativecommons.org/licenses/by-sa/3.0/us/
######################################################################

import numpy as np
import pyaudio
import datetime

import pygame


######################################################################
# Feel free to play with these numbers. Might want to change NOTE_MIN
# and NOTE_MAX especially for guitar/bass. Probably want to keep
# FRAME_SIZE and FRAMES_PER_FFT to be powers of two.
class Tuner:
    ######################################################################
    # Derived quantities from constants above. Note that as
    # SAMPLES_PER_FFT goes up, the frequency step size decreases (so
    # resolution increases); however, it will incur more delay to process
    # new sounds.

    ######################################################################

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

    ######################################################################
    # These three functions are based upon this very useful webpage:
    # https://newt.phys.unsw.edu.au/jw/notes.html

    def freq_to_number(self, f):
        return 69 + 12 * np.log2(f / 440.0)

    def number_to_freq(self, n):
        return 440 * 2.0 ** ((n - 69) / 12.0)

    def note_name(self, n):
        return self.note_names[n % 12] + str(n / 12 - 1)

    ######################################################################
    # Ok, ready to go now.

    # Get min/max index within FFT of notes we care about.
    # See docs for numpy.rfftfreq()
    def note_to_fftbin(self, n):
        return self.number_to_freq(n) / self.FREQ_STEP

    def musique(self, carryOn, carryOnThis, screen):

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
                        carryOnThis = False
                        return carryOnThis

            print('------------------------------')
            print(zelda_lullaby[note_valid])

            stream.start_stream()
            start_time = datetime.datetime.now()

            # Create Hanning window function
            window = 0.5 * (1 - np.cos(np.linspace(0, 2 * np.pi, self.samples_per_fft, False)))

            # Print initial text
            # print ('sampling at', FSAMP, 'Hz with max resolution of', FREQ_STEP, 'Hz')
            # print
            # As long as we are getting data:

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

                time_elapsed = datetime.datetime.now() - start_time
                if (zelda_lullaby[note_valid] == self.note_name(n0).split('.')[0] or time_elapsed > datetime.timedelta(seconds=5)):
                    stream.stop_stream()
                    if (zelda_lullaby[note_valid] == self.note_name(n0).split('.')[0]):
                        print('note found !!')
                        if note_valid == 0:
                            screen.blit(self.half_down, (65, 265))
                            pygame.display.flip()
                        if note_valid == 1:
                            screen.blit(self.quarter_down, (140, 260))
                            pygame.display.flip()
                        if note_valid == 2:
                            screen.blit(self.half_up, (197, 252))
                            pygame.display.flip()
                        if note_valid == 3:
                            screen.blit(self.quarter_up, (265, 247))
                            pygame.display.flip()
                        if note_valid == 4:
                            screen.blit(self.beam_up, (280, 252))
                            pygame.display.flip()
                        if note_valid == 5:
                            screen.blit(self.half_down, (365, 265))
                            pygame.display.flip()
                        if note_valid == 6:
                            screen.blit(self.quarter_down, (447, 260))
                            pygame.display.flip()
                        if note_valid == 7:
                            screen.blit(self.half_dotted, (520, 259))
                            pygame.display.flip()
                        if note_valid == 8:
                            screen.blit(self.half_down, (680, 265))
                            pygame.display.flip()
                        if note_valid == 9:
                            screen.blit(self.quarter_down, (770, 260))
                            pygame.display.flip()
                        if note_valid == 10:
                            screen.blit(self.half_cross, (850, 260))
                            pygame.display.flip()
                        if note_valid == 11:
                            screen.blit(self.quarter_down, (930, 242))
                            pygame.display.flip()
                        if note_valid == 12:
                            screen.blit(self.half_down, (1000, 253))
                            pygame.display.flip()
                        if note_valid == 13:
                            screen.blit(self.quarter_down, (1070, 266))
                            pygame.display.flip()
                        if note_valid == 14:
                            screen.blit(self.beam_down, (1083, 259))
                            pygame.display.flip()
                        if note_valid == 15:
                            screen.blit(self.half_dotted, (1160, 259))
                            pygame.display.flip()
                    else:
                        print('time out :(')
                    print('------------------------------')
                    break
            note_valid += 1
