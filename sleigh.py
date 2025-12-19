import pygame

class Sleigh:
    def __init__(self, amount, special_amount,  position=(0,0)):
        self.position = self.x, self.y = position
        self.storage = amount
        self.special_storage = special_amount
        self.used = False
        self.image = pygame.image.load('Assets/sleigh/full_sleigh_48x29.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def refill(self):
        self.used = True
        self.image = pygame.image.load('Assets/sleigh/empty_sleigh_48x27.png')
        #print("refilled")
        return self.storage
    
    def refill_special(self):
        return self.special_storage

    def reset(self):
        self.used = False
        self.image = pygame.image.load('Assets/sleigh/full_sleigh_48x29.png')
