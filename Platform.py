import pygame

class Platform:
    def __init__(self, x, y, width, height):
        self.image = pygame.image.load("Assets/Planks/32x16 wooden plank.png").convert_alpha()       
        self.image = pygame.transform.scale(self.image, (width, height))
    
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.hitbox=self.rect