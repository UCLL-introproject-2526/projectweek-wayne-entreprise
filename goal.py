import pygame

class Goal:
    def __init__(self, scherm):
        self.image = None
        self.screen = scherm
        
    def win(self):
        pygame.font.Font("aria", 32)
        text = pygame.font.render("You delivered all the presents!!!", True, (0, 255, 0), background=None)
        self.screen.blit(text, ((320-text.get_witdh())//2, (320-text.get_height())//2))


