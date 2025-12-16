import pygame

class Goal:
    def __init__(self, scherm):
        self.image = None
        self.screen = scherm
        self.place()
        
    def win(self):
        pygame.font.Font("aria", 32)
        text = pygame.font.render("You delivered all the presents!!!", True, (0, 255, 0), background=None)
        self.screen.blit(text, ((320-text.get_witdh())//2, (320-text.get_height())//2))
    
    def place(self):
        """
        self.image = pygame.image.load('Assets/goal.png')
        self.image = pygame.transform.scale_by(self.image, 0.1)
        self.screen.blit(self.image, (250, 50))
    """
        rectangle = pygame.rect.Rect(150, 50, 32, 32)
        pygame.draw.rect(self.screen, (255, 0, 0), rectangle)

