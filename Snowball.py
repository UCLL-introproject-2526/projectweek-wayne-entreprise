import pygame
class Snowball:
    def __init__(self, x, y, width, height,speed_y):
        self.image=pygame.image.load("Assets/Snowball/Snowball14x14.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect=self.image.get_rect()
        self.startheight=y
        self.startspeed=speed_y
        self.x=x
        self.y=y
        self.rect.topleft=(self.x, self.y)
        self.gravity = 0.001
        self.speed_y = speed_y
        klok = pygame.time.Clock()
        dt = klok.tick(60)
        self.on_ground=False
        
    
    def Snowball_fall(self, dt):
            self.gravity = 0.001
            if self.startspeed>=0:
                self.speed_y += self.gravity
                increase = self.speed_y * dt
                self.y  += increase
                if self.y>=720:
                    self.y=self.startheight
                    self.speed_y=self.startspeed
                self.rect.topleft=(self.x, self.y)
                   