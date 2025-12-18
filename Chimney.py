import pygame
class Chimney:
    def __init__(self, x, y, width, height):
        self.image=pygame.image.load("Assets/Chimney/chimney_26x31.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x, y)