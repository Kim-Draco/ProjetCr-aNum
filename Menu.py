import pygame

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
