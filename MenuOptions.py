import pygame
from Colors import COLORS

class MENU(pygame.sprite.Sprite):

    def __init__(self, color, size_x, size_y):

        super().__init__()

        self.image = pygame.Surface([size_x, size_y])
        self.image.fill([255,0,255])
        self.image.set_colorkey([255,0,255])

        pygame.draw.rect(self.image, color, [0, 0, size_x, size_y])
        
        self.rect = self.image.get_rect()

    def Select(self, color):
        pygame.draw.rect(self.image, color, [0, 0, self.rect.width, self.rect.height])

class CREA_MENU():

    NbMenu = 2
    Selection = 0

    list_Selections = pygame.sprite.Group()
    index_list_Selections = []
    index_list_Selections.append(pygame.image.load("images/Options/MenuOptionsBack.png"))
    index_list_Selections.append(pygame.image.load("images/Options/MenuOptionsClavier.png"))
    index_list_Selections.append(pygame.image.load("images/Options/MenuOptionsSouris.png"))

    RectMenu_list_Selections = []
    RectMenu_list_Selections.append(MENU(COLORS.YELLOW, 200, 560))
    RectMenu_list_Selections[0].rect.x = 350
    RectMenu_list_Selections[0].rect.y = 110
    RectMenu_list_Selections.append(MENU(COLORS.YELLOW, 200, 200))
    RectMenu_list_Selections[1].rect.x = 700
    RectMenu_list_Selections[1].rect.y = 110
    RectMenu_list_Selections.append(MENU(COLORS.YELLOW, 100, 50))
    RectMenu_list_Selections[2].rect.x = 500
    RectMenu_list_Selections[2].rect.y = 225
    RectMenu_list_Selections.append(MENU(COLORS.YELLOW, 100, 50))
    RectMenu_list_Selections[3].rect.x = 500
    RectMenu_list_Selections[3].rect.y = 225