import pygame

from random import randint

class Package:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.set_image()

    def __repr__(self):
        return f"Package(x={self.x}, y={self.y})"
    
    def set_image(self):
        rand = randint(1,3)
        if rand == 1:
            self.image = pygame.image.load("Assets/Presents/present_blue_25x24.png")
        elif rand == 2:
            self.image = pygame.image.load("Assets/Presents/present_green_25x24.png")
    
    def check_for_collission(self, place_coördinates):
        ...
    
    def place():
        ...

