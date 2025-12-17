import pygame

from random import randint

class Package:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.set_image()
        self.speed_y = 0

    def __repr__(self):
        return f"Package(x={self.x}, y={self.y})"
    
    def set_image(self):
        rand = randint(1,2)
        
        if rand == 1:
            self.image = pygame.image.load("Assets/Presents/present_blue_25x24.png").convert_alpha()
            
        elif rand == 2:
            self.image = pygame.image.load("Assets/Presents/present_green_25x24.png").convert_alpha()
        else:
            self.image = pygame.image.load("").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,48))
    
    def check_for_collission(self, place_coördinates):
        ...
    
    def package_falling(self, dt):
        gravity = 0.001
        self.speed_y += gravity * dt
        increase = self.speed_y * dt
        self.y  += increase

