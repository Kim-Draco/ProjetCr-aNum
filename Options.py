import pygame
from MenuOptions import MENU, CREA_MENU

class OPTIONS():
    def __init__(self):
        self.size = (1280, 720)
        self.screen = pygame.display.set_mode(self.size)
        self.background = pygame.image.load("images/Options/MenuOptionsBack.png")
        self.background = pygame.transform.scale(self.background, (1280, 720))

        self.index_list_Selections = CREA_MENU.index_list_Selections
        self.RectMenu_list_Selections = CREA_MENU.RectMenu_list_Selections
        self.list_Selections = CREA_MENU.list_Selections
        self.NbMenu = CREA_MENU.NbMenu
        self.Selection = CREA_MENU.Selection
        self.TestMenu = pygame.Surface((155, 180))
        self.TestMenu.set_alpha(160)
        self.TestMenu.fill((255, 0, 0))
        self.instrument = False
        self.temp = 0

        for i in self.RectMenu_list_Selections:
            self.list_Selections.add(i)

        # The loop will carry on until the user exits the game (e.g. clicks the close button).
        self.carryThis = True

        # The clock will be used to control how fast the screen updates
        self.clock = pygame.time.Clock()

    def Option(self, screen):
        # -------- Main Program Loop -----------
        while self.carryThis:
        # --- Main event loop

            if self.temp == 1:
                self.instrument = True
            elif self.temp == 2:
                self.instrument = False
            elif self.temp == 0:
                self.instrument = False

            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    # Flag that we are done, so we can exit the while loop
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.Selection < self.NbMenu:
                            self.Selection += 1
                        else:
                            self.Selection = 0
                    elif event.key == pygame.K_UP:
                        if self.Selection > 0:
                            self.Selection -= 1
                        else:
                            self.Selection = self.NbMenu

                    elif event.key == pygame.K_RETURN:
                        if self.Selection == 0:
                            return self.instrument
                            self.carryThis = False
                        if self.Selection == 1:
                            self.instrument = True
                            return self.instrument
                            self.carryThis = False
                        if self.Selection == 2:
                            self.instrument = False
                            return self.instrument
                            self.carryThis = False


                # Met à jour en fonction de la position de la souris
                elif event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pos()[0] >= 360 and pygame.mouse.get_pos()[0] <= 550 and pygame.mouse.get_pos()[1] >= 110 and pygame.mouse.get_pos()[1] <= 275:
                        self.Selection = 0

                    if pygame.mouse.get_pos()[0] >= 365 and pygame.mouse.get_pos()[0] <= 915 and pygame.mouse.get_pos()[1] >= 295 and pygame.mouse.get_pos()[1] <= 470:
                        self.Selection = 1
                        temp = 1

                    if pygame.mouse.get_pos()[0] >= 365 and pygame.mouse.get_pos()[0] <= 915 and pygame.mouse.get_pos()[1] >= 490 and pygame.mouse.get_pos()[1] <= 670:
                        Selection = 2
                        temp = 2

                #gère le click de la souris
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if Selection == 0 and event.button == 1:
                        return self.instrument
                        self.carryThis = False
                    if Selection == 1 and event.button == 1:
                        self.instrument = True
                        return self.instrument
                        self.carryThis = False
                    if Selection == 2 and event.button == 1:
                        self.instrument = False
                        return self.instrument
                        self.carryThis = False


            # --- Game logic should go here
            for i in self.index_list_Selections:
                if i == self.index_list_Selections[self.Selection]:
                    self.background = self.index_list_Selections[self.Selection]

        # --- Drawing code should go here
        # First, clear the screen to white.
        # screen.fill([150,150,150])
            screen.blit(self.background, (0, 0))
        # screen.blit(TestMenu, (760, 490))
        # The you can draw different shapes and lines or add text to your background stage.
        # coordonné : x, y, taille x, taille y !!!!

         # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

         # --- Limit to 60 frames per second
            self.clock.tick(60)