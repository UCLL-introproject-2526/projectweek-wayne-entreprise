import pygame

class Goal:
    def __init__(self, scherm):
        self.image = pygame.image.load('Assets/flag/Flag_18x32.png')
        self.image = pygame.transform.scale_by(self.image, 0.1)
        self.screen = scherm
        
    def win(self):
        winsound = pygame.mixer.Sound('Assets/sound/win.mp3') 
        winsound.play(0)
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render("You delivered all the presents!!!", True, (0, 255, 0))
        text_width, text_height = font.size("You delivered all the presents!!!")
        self.screen.blit(text, ((320-text_width)//2, (320-text_height)//2))
        return False
    
    def place(self):
        """
        self.image = pygame.image.load('Assets/goal.png')
        self.image = pygame.transform.scale_by(self.image, 0.1)
        self.screen.blit(self.image, (250, 50))
    """
        rectangle = pygame.rect.Rect(150, 50, 32, 32)
        pygame.draw.rect(self.screen, (255, 0, 0), rectangle)

