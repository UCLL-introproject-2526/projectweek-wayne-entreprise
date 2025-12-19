import pygame
class Snowball:
    def __init__(self, x, y, width, height):
        self.image=pygame.image.load("Assets/Snowball/Snowball14x14.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.topleft=(self.x, self.y)
        self.gravity = 0.001
        self.speed_y = 0
        klok = pygame.time.Clock()
        dt = klok.tick(60)
        self.on_ground=False
        
    
    def Snowball_fall(self, dt):
            print("check125")
            self.gravity = 0.001
            self.speed_y += self.gravity
            increase = self.speed_y * dt
            self.y  += increase
            if self.y>=720:
                 self.y=0
                 self.speed_y=0
            self.rect.topleft=(self.x, self.y)    